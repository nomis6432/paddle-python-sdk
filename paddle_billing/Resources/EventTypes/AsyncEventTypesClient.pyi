# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/EventTypes/EventTypesClient.py
# Regenerate with: python scripts/generate_async_stubs.py
from paddle_billing.ResponseParser import ResponseParser
from paddle_billing.Entities.Collections import EventTypeCollection

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncEventTypesClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self) -> EventTypeCollection: ...
