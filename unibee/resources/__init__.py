# coding: utf-8
"""
UniBee API Resources

This module exports all API resource classes for the UniBee SDK.
Each resource provides methods for interacting with a specific API domain.
"""

from unibee.resources.base import BaseResource
from unibee.resources.subscription import SubscriptionResource
from unibee.resources.user import UserResource
from unibee.resources.invoice import InvoiceResource
from unibee.resources.payment import PaymentResource
from unibee.resources.plan import PlanResource
from unibee.resources.product import ProductResource
from unibee.resources.webhook import WebhookResource
from unibee.resources.gateway import GatewayResource
from unibee.resources.member import MemberResource
from unibee.resources.metric import MetricResource
from unibee.resources.discount import DiscountResource
from unibee.resources.session import SessionResource
from unibee.resources.credit import CreditResource
from unibee.resources.vat import VatResource
from unibee.resources.search import SearchResource
from unibee.resources.role import RoleResource

__all__ = [
    "BaseResource",
    "SubscriptionResource",
    "UserResource",
    "InvoiceResource",
    "PaymentResource",
    "PlanResource",
    "ProductResource",
    "WebhookResource",
    "GatewayResource",
    "MemberResource",
    "MetricResource",
    "DiscountResource",
    "SessionResource",
    "CreditResource",
    "VatResource",
    "SearchResource",
    "RoleResource",
]
