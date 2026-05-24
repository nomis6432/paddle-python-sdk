# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Transactions/TransactionsClient.py
# Regenerate with: python scripts/generate_async_stubs.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Transaction import Transaction
from paddle_billing.Entities.TransactionData import TransactionData
from paddle_billing.Entities.TransactionPreview import TransactionPreview
from paddle_billing.Entities.Collections import TransactionCollection

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Transactions.Operations import (
    CreateTransaction,
    ListTransactions,
    UpdateTransaction,
    PreviewTransaction,
    PreviewTransactionByAddress,
    PreviewTransactionByCustomer,
    PreviewTransactionByIP,
    TransactionIncludes,
    GetTransactionInvoice,
    ReviseTransaction,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncTransactionsClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self, operation: ListTransactions | None=None) -> TransactionCollection: ...
    async def get(self, transaction_id: str, includes=None) -> Transaction: ...
    async def create(self, operation: CreateTransaction, includes=None) -> Transaction: ...
    async def update(self, transaction_id: str, operation: UpdateTransaction) -> Transaction: ...
    async def preview(self, operation: PreviewTransaction | PreviewTransactionByAddress | PreviewTransactionByCustomer | PreviewTransactionByIP) -> TransactionPreview: ...
    async def get_invoice_pdf(self, transaction_id: str, operation: GetTransactionInvoice | None=None) -> TransactionData: ...
    async def revise(self, transaction_id: str, operation: ReviseTransaction) -> Transaction: ...
