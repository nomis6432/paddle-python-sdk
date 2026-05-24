# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/ClientTokens/ClientTokensClient.py
# Regenerate with: python scripts/generate_async_stubs.py
#
# This is a type-checker-only (.pyi) stub file. It is NOT importable at runtime.
# Import AsyncClient from paddle_billing.AsyncClient; do not import this file directly.
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import ClientTokenCollection
from paddle_billing.Entities.ClientToken import ClientToken
from paddle_billing.Entities.ClientTokens import ClientTokenStatus

from paddle_billing.Resources.ClientTokens.Operations import CreateClientToken, ListClientTokens, UpdateClientToken

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncClientTokensClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self, operation: ListClientTokens | None=None) -> ClientTokenCollection: ...
    async def get(self, client_token_id: str) -> ClientToken: ...
    async def create(self, operation: CreateClientToken) -> ClientToken: ...
    async def update(self, client_token_id: str, operation: UpdateClientToken) -> ClientToken: ...
    async def revoke(self, client_token_id: str) -> ClientToken: ...
