# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/NotificationSettings/NotificationSettingsClient.py
# Regenerate with: python scripts/generate_async_stubs.py
#
# This is a type-checker-only (.pyi) stub file. It is NOT importable at runtime.
# Import AsyncClient from paddle_billing.AsyncClient; do not import this file directly.
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Collections import NotificationSettingCollection
from paddle_billing.Entities.NotificationSetting import NotificationSetting

from paddle_billing.Resources.NotificationSettings.Operations import (
    CreateNotificationSetting,
    UpdateNotificationSetting,
    ListNotificationSettings,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncNotificationSettingsClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self, operation: ListNotificationSettings | None=None) -> NotificationSettingCollection: ...
    async def get(self, notification_setting_id: str) -> NotificationSetting: ...
    async def create(self, operation: CreateNotificationSetting) -> NotificationSetting: ...
    async def update(self, notification_setting_id: str, operation: UpdateNotificationSetting) -> NotificationSetting: ...
    async def delete(self, notification_setting_id: str) -> None: ...
