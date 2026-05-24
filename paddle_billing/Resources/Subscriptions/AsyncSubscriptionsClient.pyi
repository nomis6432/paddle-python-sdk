# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: paddle_billing/Resources/Subscriptions/SubscriptionsClient.py
# Regenerate with: python scripts/generate_async_stubs.py
#
# This is a type-checker-only (.pyi) stub file. It is NOT importable at runtime.
# Import AsyncClient from paddle_billing.AsyncClient; do not import this file directly.
from paddle_billing.ResponseParser import ResponseParser

from paddle_billing.Entities.Subscription import Subscription
from paddle_billing.Entities.SubscriptionPreview import SubscriptionPreview
from paddle_billing.Entities.Transaction import Transaction
from paddle_billing.Entities.Collections import SubscriptionCollection

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Subscriptions.Operations import (
    CancelSubscription,
    CreateOneTimeCharge,
    SubscriptionIncludes,
    ListSubscriptions,
    PauseSubscription,
    PreviewOneTimeCharge,
    PreviewUpdateSubscription,
    ResumeSubscription,
    UpdateSubscription,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from paddle_billing.AsyncClient import AsyncClient

class AsyncSubscriptionsClient:
    def __init__(self, client: 'AsyncClient') -> None: ...
    async def list(self, operation: ListSubscriptions | None=None) -> SubscriptionCollection: ...
    async def get(self, subscription_id: str, includes=None) -> Subscription: ...
    async def update(self, subscription_id: str, operation: UpdateSubscription) -> Subscription: ...
    async def pause(self, subscription_id: str, operation: PauseSubscription) -> Subscription: ...
    async def resume(self, subscription_id: str, operation: ResumeSubscription) -> Subscription: ...
    async def cancel(self, subscription_id: str, operation: CancelSubscription) -> Subscription: ...
    async def get_payment_method_change_transaction(self, subscription_id: str) -> Transaction: ...
    async def activate(self, subscription_id: str) -> Subscription: ...
    async def create_one_time_charge(self, subscription_id: str, operation: CreateOneTimeCharge) -> Subscription: ...
    async def preview_update(self, subscription_id: str, operation: PreviewUpdateSubscription) -> SubscriptionPreview: ...
    async def preview_one_time_charge(self, subscription_id: str, operation: PreviewOneTimeCharge) -> SubscriptionPreview: ...
