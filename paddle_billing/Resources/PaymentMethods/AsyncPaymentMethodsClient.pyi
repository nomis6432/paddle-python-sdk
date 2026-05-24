# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/PaymentMethods/PaymentMethodsClient.py
# Regenerate with: python scripts/generate_async_stubs.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import (
    PaymentMethodCollection,
)
from paddle_billing.Entities.PaymentMethod import PaymentMethod

from paddle_billing.Resources.PaymentMethods.Operations import (
    ListPaymentMethods,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncPaymentMethodsClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self, customer_id: str, operation: ListPaymentMethods | None=None) -> PaymentMethodCollection: ...
    async def get(self, customer_id: str, payment_method_id: str) -> PaymentMethod: ...
    async def delete(self, customer_id: str, payment_method_id: str) -> None: ...
