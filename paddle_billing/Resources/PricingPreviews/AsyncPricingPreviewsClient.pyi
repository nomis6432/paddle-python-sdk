# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/PricingPreviews/PricingPreviewsClient.py
# Regenerate with: python scripts/generate_async_stubs.py
from paddle_billing.ResponseParser import ResponseParser
from paddle_billing.Entities.PricePreview import PricePreview
from paddle_billing.Resources.PricingPreviews.Operations import PreviewPrice

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncPricingPreviewsClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def preview_prices(self, operation: PreviewPrice) -> PricePreview: ...
