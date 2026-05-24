# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Addresses/AddressesClient.py
# Regenerate with: python scripts/generate_async_stubs.py
#
# This is a type-checker-only (.pyi) stub file. It is NOT importable at runtime.
# Import AsyncClient from paddle_billing.AsyncClient; do not import this file directly.
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Address import Address
from paddle_billing.Entities.Collections import AddressCollection
from paddle_billing.Entities.Shared import Status

from paddle_billing.Resources.Addresses.Operations import CreateAddress, ListAddresses, UpdateAddress

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncAddressesClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self, customer_id: str, operation: ListAddresses | None=None) -> AddressCollection: ...
    async def get(self, customer_id: str, address_id: str) -> Address: ...
    async def create(self, customer_id: str, operation: CreateAddress) -> Address: ...
    async def update(self, customer_id: str, address_id: str, operation: UpdateAddress) -> Address: ...
    async def archive(self, customer_id: str, address_id: str) -> Address: ...
