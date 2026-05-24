# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Events/EventsClient.py
# Regenerate with: python scripts/generate_async_stubs.py
#
# This is a type-checker-only (.pyi) stub file. It is NOT importable at runtime.
# Import AsyncClient from paddle_billing.AsyncClient; do not import this file directly.
from paddle_billing.ResponseParser import ResponseParser
from paddle_billing.Entities.Collections import EventCollection
from paddle_billing.Resources.Events.Operations import ListEvents

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncEventsClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self, operation: ListEvents | None=None) -> EventCollection: ...
