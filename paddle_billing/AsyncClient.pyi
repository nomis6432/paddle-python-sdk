# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/AsyncClient.py
# Regenerate with: python scripts/generate_async_stubs.py
#
# This is a type-checker-only (.pyi) stub file. It is NOT importable at runtime.
# Import AsyncClient from paddle_billing.AsyncClient; do not import this file directly.
import asyncio
import contextvars
from json import dumps as json_dumps
from logging import Logger, getLogger
from typing import Any
from urllib.parse import urljoin, urlencode
from uuid import uuid4

import httpx

from paddle_billing.Json import PayloadEncoder
from paddle_billing.Operation import Operation
from paddle_billing.HasParameters import HasParameters
from paddle_billing.Options import Options
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Logger.NullHandler import NullHandler

from paddle_billing.Resources.Addresses.AsyncAddressesClient import AsyncAddressesClient
from paddle_billing.Resources.Adjustments.AsyncAdjustmentsClient import AsyncAdjustmentsClient
from paddle_billing.Resources.Businesses.AsyncBusinessesClient import AsyncBusinessesClient
from paddle_billing.Resources.ClientTokens.AsyncClientTokensClient import AsyncClientTokensClient
from paddle_billing.Resources.Customers.AsyncCustomersClient import AsyncCustomersClient
from paddle_billing.Resources.CustomerPortalSessions.AsyncCustomerPortalSessionsClient import AsyncCustomerPortalSessionsClient
from paddle_billing.Resources.DiscountGroups.AsyncDiscountGroupsClient import AsyncDiscountGroupsClient
from paddle_billing.Resources.Discounts.AsyncDiscountsClient import AsyncDiscountsClient
from paddle_billing.Resources.Events.AsyncEventsClient import AsyncEventsClient
from paddle_billing.Resources.EventTypes.AsyncEventTypesClient import AsyncEventTypesClient
from paddle_billing.Resources.IPAddresses.AsyncIPAddressesClient import AsyncIPAddressesClient
from paddle_billing.Resources.Notifications.AsyncNotificationsClient import AsyncNotificationsClient
from paddle_billing.Resources.NotificationLogs.AsyncNotificationLogsClient import AsyncNotificationLogsClient
from paddle_billing.Resources.NotificationSettings.AsyncNotificationSettingsClient import AsyncNotificationSettingsClient
from paddle_billing.Resources.PaymentMethods.AsyncPaymentMethodsClient import AsyncPaymentMethodsClient
from paddle_billing.Resources.Prices.AsyncPricesClient import AsyncPricesClient
from paddle_billing.Resources.PricingPreviews.AsyncPricingPreviewsClient import AsyncPricingPreviewsClient
from paddle_billing.Resources.Products.AsyncProductsClient import AsyncProductsClient
from paddle_billing.Resources.Reports.AsyncReportsClient import AsyncReportsClient
from paddle_billing.Resources.Simulations.AsyncSimulationsClient import AsyncSimulationsClient
from paddle_billing.Resources.SimulationRuns.AsyncSimulationRunsClient import AsyncSimulationRunsClient
from paddle_billing.Resources.SimulationRunEvents.AsyncSimulationRunEventsClient import AsyncSimulationRunEventsClient
from paddle_billing.Resources.SimulationTypes.AsyncSimulationTypesClient import AsyncSimulationTypesClient
from paddle_billing.Resources.Subscriptions.AsyncSubscriptionsClient import AsyncSubscriptionsClient
from paddle_billing.Resources.Transactions.AsyncTransactionsClient import AsyncTransactionsClient

class AsyncClient:
    def __init__(self, api_key: str, options: Options | None=None, http_client: httpx.AsyncClient | None=None, logger: Logger | None=None, retry_count: int=3, use_api_version: int=1, timeout: float=60.0) -> None: ...
    addresses: AsyncAddressesClient
    adjustments: AsyncAdjustmentsClient
    businesses: AsyncBusinessesClient
    client_tokens: AsyncClientTokensClient
    customer_portal_sessions: AsyncCustomerPortalSessionsClient
    customers: AsyncCustomersClient
    discount_groups: AsyncDiscountGroupsClient
    discounts: AsyncDiscountsClient
    event_types: AsyncEventTypesClient
    events: AsyncEventsClient
    ip_addresses: AsyncIPAddressesClient
    notification_logs: AsyncNotificationLogsClient
    notification_settings: AsyncNotificationSettingsClient
    notifications: AsyncNotificationsClient
    payment_methods: AsyncPaymentMethodsClient
    prices: AsyncPricesClient
    pricing_previews: AsyncPricingPreviewsClient
    products: AsyncProductsClient
    reports: AsyncReportsClient
    simulation_run_events: AsyncSimulationRunEventsClient
    simulation_runs: AsyncSimulationRunsClient
    simulation_types: AsyncSimulationTypesClient
    simulations: AsyncSimulationsClient
    subscriptions: AsyncSubscriptionsClient
    transactions: AsyncTransactionsClient
    async def __aenter__(self): ...
    async def __aexit__(self, *args): ...
    async def close(self): ...
    @staticmethod
    def null_logger() -> Logger: ...
    @property
    def payload(self) -> str | None: ...
    @payload.setter
    def payload(self, value: str | None) -> None: ...
    @property
    def status_code(self) -> int | None: ...
    @status_code.setter
    def status_code(self, value: int | None) -> None: ...
    async def _logging_hook(self, response: httpx.Response) -> None: ...
    @staticmethod
    def serialize_json_payload(payload: dict[str, Any] | Operation) -> str: ...
    async def _make_request(self, method: str, url: str, payload: dict[str, Any] | Operation | None=None) -> httpx.Response: ...
    @staticmethod
    def format_uri_parameters(uri: str, parameters: HasParameters | dict[str, str]) -> str: ...
    async def get_raw(self, url: str, parameters: HasParameters | dict[str, str] | None=None) -> httpx.Response: ...
    async def post_raw(self, url: str, payload: dict[str, str] | Operation | None=None, parameters: HasParameters | dict[str, str] | None=None) -> httpx.Response: ...
    async def patch_raw(self, url: str, payload: dict[str, str] | Operation | None) -> httpx.Response: ...
    async def delete_raw(self, url: str) -> httpx.Response: ...
    async def _get(self, url: str, params=None, parse_fn=None): ...
    async def _post(self, url: str, payload=None, parse_fn=None, params=None): ...
    async def _patch(self, url: str, payload=None, parse_fn=None): ...
    async def _delete(self, url: str, parse_fn=None): ...
    def _make_paginator(self, pagination, mapper): ...
    def build_async_client(self) -> httpx.AsyncClient: ...
