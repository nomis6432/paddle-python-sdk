# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Businesses/BusinessesClient.py
# Regenerate with: python scripts/generate_async_stubs.py
#
# This is a type-checker-only (.pyi) stub file. It is NOT importable at runtime.
# Import AsyncClient from paddle_billing.AsyncClient; do not import this file directly.
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Business import Business
from paddle_billing.Entities.Collections import BusinessCollection
from paddle_billing.Entities.Shared import Status

from paddle_billing.Resources.Businesses.Operations import CreateBusiness, ListBusinesses, UpdateBusiness

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncBusinessesClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self, customer_id: str, operation: ListBusinesses | None=None) -> BusinessCollection: ...
    async def get(self, customer_id: str, business_id: str) -> Business: ...
    async def create(self, customer_id: str, operation: CreateBusiness) -> Business: ...
    async def update(self, customer_id: str, business_id: str, operation: UpdateBusiness) -> Business: ...
    async def archive(self, customer_id: str, business_id: str) -> Business: ...
