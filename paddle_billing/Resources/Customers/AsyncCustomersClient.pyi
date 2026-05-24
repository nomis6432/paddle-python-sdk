# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Customers/CustomersClient.py
# Regenerate with: python scripts/generate_async_stubs.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import (
    CreditBalanceCollection,
    CustomerCollection,
)
from paddle_billing.Entities.Customer import Customer
from paddle_billing.Entities.CustomerAuthToken import CustomerAuthToken
from paddle_billing.Entities.Shared import Status

from paddle_billing.Resources.Customers.Operations import (
    CreateCustomer,
    ListCreditBalances,
    ListCustomers,
    UpdateCustomer,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncCustomersClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self, operation: ListCustomers | None=None) -> CustomerCollection: ...
    async def get(self, customer_id: str) -> Customer: ...
    async def create(self, operation: CreateCustomer) -> Customer: ...
    async def update(self, customer_id: str, operation: UpdateCustomer) -> Customer: ...
    async def archive(self, customer_id: str) -> Customer: ...
    async def credit_balances(self, customer_id: str, operation: ListCreditBalances | None=None) -> CreditBalanceCollection: ...
    async def create_auth_token(self, customer_id: str) -> CustomerAuthToken: ...
