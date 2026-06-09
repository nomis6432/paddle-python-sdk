"""
Contract test for the AsyncClient dynamic dispatch architecture.

AsyncClient reuses the sync resource clients; their methods must return the
result of self.client._get/_post/_patch/_delete directly so the coroutine
produced by AsyncClient's async dispatch methods reaches the caller.  A method
that calls a dispatch method without returning it silently discards the
coroutine and never sends the HTTP request (this bug shipped twice, in
PaymentMethodsClient.delete and NotificationSettingsClient.delete).

This test calls every public method of every resource client through an
AsyncClient whose dispatch methods are stubbed, and asserts the caller
receives the dispatch coroutine.
"""

import asyncio
import inspect
from unittest.mock import MagicMock

from pytest import mark

from paddle_billing import AsyncClient, Environment, Options

SENTINEL = object()


def make_client() -> AsyncClient:
    return AsyncClient("fake_api_key", options=Options(Environment.SANDBOX))


def collect_resource_methods() -> list[tuple[str, str]]:
    client = make_client()
    cases = []

    for attr_name, resource in sorted(vars(client).items()):
        # 'client' is the underlying httpx.AsyncClient, not a resource
        if attr_name.startswith("_") or attr_name == "client":
            continue
        if not type(resource).__name__.endswith("Client"):
            continue

        for method_name, _ in inspect.getmembers(type(resource), predicate=inspect.isfunction):
            if not method_name.startswith("_"):
                cases.append((attr_name, method_name))

    return cases


CASES = collect_resource_methods()


class TestAsyncDispatchContract:
    @mark.parametrize("resource_name, method_name", CASES, ids=[f"{r}.{m}" for r, m in CASES])
    async def test_method_returns_dispatch_coroutine(self, resource_name, method_name):
        client = make_client()

        async def fake_dispatch(*args, **kwargs):
            return SENTINEL

        client._get = fake_dispatch
        client._post = fake_dispatch
        client._patch = fake_dispatch
        client._delete = fake_dispatch

        try:
            method = getattr(getattr(client, resource_name), method_name)

            kwargs = {
                name: "fake_id" if param.annotation in (str, "str") else MagicMock()
                for name, param in inspect.signature(method).parameters.items()
                if param.default is inspect.Parameter.empty
                and param.kind in (inspect.Parameter.POSITIONAL_OR_KEYWORD, inspect.Parameter.KEYWORD_ONLY)
            }

            result = method(**kwargs)

            assert asyncio.iscoroutine(result), (
                f"{resource_name}.{method_name} did not return a coroutine when called through "
                f"AsyncClient — it must `return self.client._get/_post/_patch/_delete(...)` "
                f"so the dispatch coroutine reaches the caller"
            )
            assert await result is SENTINEL, (
                f"{resource_name}.{method_name} returned a coroutine that does not resolve to "
                f"the dispatch result — the dispatch call must be returned directly"
            )
        finally:
            await client.close()
