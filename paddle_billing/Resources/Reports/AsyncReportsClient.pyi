# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Reports/ReportsClient.py
# Regenerate with: python scripts/generate_async_stubs.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Report import Report
from paddle_billing.Entities.ReportCSV import ReportCSV
from paddle_billing.Entities.Collections import ReportCollection

from paddle_billing.Resources.Reports.Operations import CreateReport, ListReports

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncReportsClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self, operation: ListReports | None=None) -> ReportCollection: ...
    async def get(self, report_id: str) -> Report: ...
    async def get_report_csv(self, report_id: str) -> ReportCSV: ...
    async def create(self, operation: CreateReport) -> Report: ...
