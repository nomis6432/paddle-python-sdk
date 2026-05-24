# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Discounts/DiscountsClient.py
# Regenerate with: python scripts/generate_async_stubs.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import DiscountCollection
from paddle_billing.Entities.Discount import Discount
from paddle_billing.Entities.Discounts import DiscountStatus

from paddle_billing.Resources.Discounts.Operations import CreateDiscount, GetDiscount, ListDiscounts, UpdateDiscount

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncDiscountsClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self, operation: ListDiscounts | None=None) -> DiscountCollection: ...
    async def get(self, discount_id: str, operation: GetDiscount | None=None) -> Discount: ...
    async def create(self, operation: CreateDiscount) -> Discount: ...
    async def update(self, discount_id: str, operation: UpdateDiscount) -> Discount: ...
    async def archive(self, discount_id: str) -> Discount: ...
