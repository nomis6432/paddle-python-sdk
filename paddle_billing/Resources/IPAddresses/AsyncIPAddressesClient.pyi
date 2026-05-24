# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/IPAddresses/IPAddressesClient.py
# Regenerate with: python scripts/generate_async_stubs.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.IPAddresses import IPAddresses

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncIPAddressesClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def get_ip_addresses(self) -> IPAddresses: ...
