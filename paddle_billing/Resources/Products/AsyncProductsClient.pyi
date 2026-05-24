# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Products/ProductsClient.py
# Regenerate with: python scripts/generate_async_stubs.py
#
# This is a type-checker-only (.pyi) stub file. It is NOT importable at runtime.
# Import AsyncClient from paddle_billing.AsyncClient; do not import this file directly.
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import ProductCollection
from paddle_billing.Entities.Product import Product
from paddle_billing.Entities.Shared import Status

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Products.Operations import CreateProduct, ListProducts, UpdateProduct, ProductIncludes

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncProductsClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self, operation: ListProducts | None=None) -> ProductCollection: ...
    async def get(self, product_id: str, includes=None) -> Product | Product: ...
    async def create(self, operation: CreateProduct) -> Product: ...
    async def update(self, product_id: str, operation: UpdateProduct) -> Product: ...
    async def archive(self, product_id: str) -> Product: ...
