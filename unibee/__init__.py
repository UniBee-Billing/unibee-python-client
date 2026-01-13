# coding: utf-8
"""
UniBee Python SDK

A Python SDK for interacting with the UniBee billing API.
UniBee is an open-source billing solution for SaaS businesses.

Documentation: https://docs.unibee.dev/
GitHub: https://github.com/UniBee-Billing/unibee-python-client
"""

__version__ = "1.1.0"

from unibee.client import UniBeeClient
from unibee.configuration import Configuration
from unibee.exceptions import (
    UniBeeError,
    AuthenticationError,
    APIError,
    NotFoundError,
    ValidationError,
    RateLimitError,
)

# Re-export the main client for convenience
Client = UniBeeClient

# API module imports
from unibee import api

__all__ = [
    # Main client
    "UniBeeClient",
    "Client",
    "Configuration",
    # Exceptions
    "UniBeeError",
    "AuthenticationError",
    "APIError",
    "NotFoundError",
    "ValidationError",
    "RateLimitError",
    # API modules
    "api",
    # Version
    "__version__",
]
