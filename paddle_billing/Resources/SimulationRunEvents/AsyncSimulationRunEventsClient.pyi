# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/SimulationRunEvents/SimulationRunEventsClient.py
# Regenerate with: python scripts/generate_async_stubs.py
#
# This is a type-checker-only (.pyi) stub file. It is NOT importable at runtime.
# Import AsyncClient from paddle_billing.AsyncClient; do not import this file directly.
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.SimulationRunEvent import SimulationRunEvent
from paddle_billing.Entities.Collections import SimulationRunEventCollection
from paddle_billing.Resources.SimulationRunEvents.Operations import ListSimulationRunEvents

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncSimulationRunEventsClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self, simulation_id: str, simulation_run_id: str, operation: ListSimulationRunEvents | None=None) -> SimulationRunEventCollection: ...
    async def get(self, simulation_id: str, simulation_run_id: str, simulation_event_id: str) -> SimulationRunEvent: ...
    async def replay(self, simulation_id: str, simulation_run_id: str, simulation_event_id: str) -> SimulationRunEvent: ...
