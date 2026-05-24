# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/SimulationRuns/SimulationRunsClient.py
# Regenerate with: python scripts/generate_async_stubs.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.SimulationRun import SimulationRun
from paddle_billing.Entities.Collections import SimulationRunCollection
from paddle_billing.Resources.SimulationRuns.Operations import GetSimulationRun, ListSimulationRuns

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncSimulationRunsClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self, simulation_id: str, operation: ListSimulationRuns | None=None) -> SimulationRunCollection: ...
    async def get(self, simulation_id: str, simulation_run_id: str, operation: GetSimulationRun | None=None) -> SimulationRun: ...
    async def create(self, simulation_id: str) -> SimulationRun: ...
