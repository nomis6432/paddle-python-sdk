# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Simulations/SimulationsClient.py
# Regenerate with: python scripts/generate_async_stubs.py
#
# This is a type-checker-only (.pyi) stub file. It is NOT importable at runtime.
# Import AsyncClient from paddle_billing.AsyncClient; do not import this file directly.
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Simulation import Simulation
from paddle_billing.Entities.Collections import SimulationCollection
from paddle_billing.Resources.Simulations.Operations import CreateSimulation, ListSimulations, UpdateSimulation

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncSimulationsClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self, operation: ListSimulations | None=None) -> SimulationCollection: ...
    async def get(self, simulation_id: str) -> Simulation: ...
    async def create(self, operation: CreateSimulation) -> Simulation: ...
    async def update(self, simulation_id: str, operation: UpdateSimulation) -> Simulation: ...
