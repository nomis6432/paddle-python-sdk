# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/DiscountGroups/DiscountGroupsClient.py
# Regenerate with: python scripts/generate_async_stubs.py
#
# This is a type-checker-only (.pyi) stub file. It is NOT importable at runtime.
# Import AsyncClient from paddle_billing.AsyncClient; do not import this file directly.
from paddle_billing.Resources.DiscountGroups.Operations import (
    CreateDiscountGroup,
    ListDiscountGroups,
    UpdateDiscountGroup,
)
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import DiscountGroupCollection
from paddle_billing.Entities.DiscountGroup import DiscountGroup, DiscountGroupStatus

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncDiscountGroupsClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self, operation: ListDiscountGroups | None=None) -> DiscountGroupCollection: ...
    async def get(self, discount_group_id: str) -> DiscountGroup: ...
    async def create(self, operation: CreateDiscountGroup) -> DiscountGroup: ...
    async def update(self, discount_group_id: str, operation: UpdateDiscountGroup) -> DiscountGroup: ...
    async def archive(self, discount_group_id: str) -> DiscountGroup: ...
