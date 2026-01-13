# coding: utf-8
"""
UniBee API Modules

This package contains all the API resource modules for the UniBee SDK.
"""

from unibee.api.subscriptions import SubscriptionsAPI
from unibee.api.plans import PlansAPI
from unibee.api.invoices import InvoicesAPI
from unibee.api.payments import PaymentsAPI
from unibee.api.users import UsersAPI
from unibee.api.webhooks import WebhooksAPI
from unibee.api.merchants import MerchantsAPI
from unibee.api.discounts import DiscountsAPI
from unibee.api.products import ProductsAPI
from unibee.api.gateway import GatewaysAPI
from unibee.api.checkout import CheckoutAPI
from unibee.api.credit import CreditAPI

__all__ = [
    "SubscriptionsAPI",
    "PlansAPI",
    "InvoicesAPI",
    "PaymentsAPI",
    "UsersAPI",
    "WebhooksAPI",
    "MerchantsAPI",
    "DiscountsAPI",
    "ProductsAPI",
    "GatewaysAPI",
    "CheckoutAPI",
    "CreditAPI",
]
