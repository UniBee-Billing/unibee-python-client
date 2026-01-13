# coding: utf-8
"""
UniBee Python SDK

A modern, easy-to-use Python client for the UniBee billing API.
This SDK provides a clean interface for managing subscriptions, invoices,
payments, and other billing operations.

Basic Usage:
    from unibee import UniBeeClient

    client = UniBeeClient(
        api_key="your_api_key_here",
        base_url="https://api.unibee.dev"  # or https://api-sandbox.unibee.top for sandbox
    )

    # List subscriptions
    subscriptions = client.subscription.list()

    # Get user details
    user = client.user.get(user_id=123)

For more information, visit: https://docs.unibee.dev/documentation
"""

__version__ = "2.0.0"
__author__ = "UniBee Team"
__email__ = "support@unibee.dev"

from unibee.client import UniBeeClient
from unibee.exceptions import (
    UniBeeError,
    UniBeeAuthenticationError,
    UniBeeAPIError,
    UniBeeValidationError,
    UniBeeNotFoundError,
    UniBeeRateLimitError,
)

# API resource classes for direct access
from unibee.resources import (
    SubscriptionResource,
    UserResource,
    InvoiceResource,
    PaymentResource,
    PlanResource,
    WebhookResource,
)

__all__ = [
    # Main client
    "UniBeeClient",
    # Exceptions
    "UniBeeError",
    "UniBeeAuthenticationError",
    "UniBeeAPIError",
    "UniBeeValidationError",
    "UniBeeNotFoundError",
    "UniBeeRateLimitError",
    # Resources
    "SubscriptionResource",
    "UserResource",
    "InvoiceResource",
    "PaymentResource",
    "PlanResource",
    "WebhookResource",
    # Version
    "__version__",
]
