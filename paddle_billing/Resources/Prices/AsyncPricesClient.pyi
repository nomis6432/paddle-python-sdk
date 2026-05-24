# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Prices/PricesClient.py
# Regenerate with: python scripts/generate_async_stubs.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Price import Price
from paddle_billing.Entities.Collections import PriceCollection
from paddle_billing.Entities.Shared import Status

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Prices.Operations import CreatePrice, ListPrices, UpdatePrice, PriceIncludes

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncPricesClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self, operation: ListPrices | None=None) -> PriceCollection: ...
    async def get(self, price_id: str, includes=None) -> Price: ...
    async def create(self, operation: CreatePrice) -> Price: ...
    async def update(self, price_id: str, operation: UpdatePrice) -> Price: ...
    async def archive(self, price_id: str) -> Price: ...
