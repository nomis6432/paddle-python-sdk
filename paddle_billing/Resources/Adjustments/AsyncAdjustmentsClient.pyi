# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Adjustments/AdjustmentsClient.py
# Regenerate with: python scripts/generate_async_stubs.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Adjustment import Adjustment
from paddle_billing.Entities.AdjustmentCreditNote import AdjustmentCreditNote
from paddle_billing.Entities.Collections import AdjustmentCollection

from paddle_billing.Resources.Adjustments.Operations import CreateAdjustment, GetCreditNote, ListAdjustments

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncAdjustmentsClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self, operation: ListAdjustments | None=None) -> AdjustmentCollection: ...
    async def create(self, operation: CreateAdjustment) -> Adjustment: ...
    async def get_credit_note(self, adjustment_id: str, operation: GetCreditNote | None=None) -> AdjustmentCreditNote: ...
