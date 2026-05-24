# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Notifications/NotificationsClient.py
# Regenerate with: python scripts/generate_async_stubs.py
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import NotificationCollection
from paddle_billing.Entities.Notification import Notification

from paddle_billing.Resources.Notifications.Operations import ListNotifications

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncNotificationsClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self, operation: ListNotifications | None=None) -> NotificationCollection: ...
    async def get(self, notification_id: str) -> Notification: ...
    async def replay(self, notification_id: str) -> str: ...
