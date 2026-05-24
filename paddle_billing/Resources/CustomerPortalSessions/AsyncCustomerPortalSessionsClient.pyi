# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/CustomerPortalSessions/CustomerPortalSessionsClient.py
# Regenerate with: python scripts/generate_async_stubs.py
#
# This is a type-checker-only (.pyi) stub file. It is NOT importable at runtime.
# Import AsyncClient from paddle_billing.AsyncClient; do not import this file directly.
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.CustomerPortalSession import CustomerPortalSession

from paddle_billing.Resources.CustomerPortalSessions.Operations import (
    CreateCustomerPortalSession,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncCustomerPortalSessionsClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def create(self, customer_id: str, operation: CreateCustomerPortalSession) -> CustomerPortalSession: ...
