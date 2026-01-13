# coding: utf-8
"""
UniBee Client

The main client class for interacting with the UniBee API.
Provides a clean, Pythonic interface for all API operations.
"""

from typing import Optional, Dict, Any
import logging

from openapi_client import Configuration, ApiClient
from openapi_client.rest import ApiException

from unibee.resources import (
    SubscriptionResource,
    UserResource,
    InvoiceResource,
    PaymentResource,
    PlanResource,
    ProductResource,
    WebhookResource,
    GatewayResource,
    MemberResource,
    MetricResource,
    DiscountResource,
    SessionResource,
    CreditResource,
    VatResource,
    SearchResource,
    RoleResource,
)
from unibee.exceptions import (
    UniBeeError,
    UniBeeAuthenticationError,
    UniBeeConnectionError,
    raise_for_status,
)


logger = logging.getLogger("unibee")


class UniBeeClient:
    """
    UniBee API Client.
    
    This is the main entry point for interacting with the UniBee API.
    It provides access to all API resources through intuitive properties.
    
    Args:
        api_key: Your UniBee API key (Bearer token)
        base_url: API base URL. Defaults to production (https://api.unibee.dev)
                  Use https://api-sandbox.unibee.top for sandbox/testing
        timeout: Request timeout in seconds (default: 30)
        debug: Enable debug logging (default: False)
        
    Example:
        >>> from unibee import UniBeeClient
        >>> 
        >>> # Initialize client
        >>> client = UniBeeClient(api_key="your_api_key_here")
        >>> 
        >>> # Use sandbox for testing
        >>> sandbox_client = UniBeeClient(
        ...     api_key="your_api_key_here",
        ...     base_url="https://api-sandbox.unibee.top"
        ... )
        >>> 
        >>> # List subscriptions
        >>> subs = client.subscription.list()
        >>> 
        >>> # Get a specific user
        >>> user = client.user.get(user_id=123)
        >>> 
        >>> # Create a new subscription
        >>> sub = client.subscription.create(
        ...     user_id=123,
        ...     plan_id=456,
        ...     gateway_id=789
        ... )
    """
    
    # Default API URLs
    PRODUCTION_URL = "https://api.unibee.dev"
    SANDBOX_URL = "https://api-sandbox.unibee.top"
    
    def __init__(
        self,
        api_key: str,
        base_url: Optional[str] = None,
        timeout: int = 30,
        debug: bool = False,
    ):
        if not api_key:
            raise UniBeeAuthenticationError(
                "API key is required. Get your API key from the UniBee dashboard."
            )
        
        self._api_key = api_key
        self._base_url = base_url or self.PRODUCTION_URL
        self._timeout = timeout
        self._debug = debug
        
        # Configure logging
        if debug:
            logging.basicConfig(level=logging.DEBUG)
            logger.setLevel(logging.DEBUG)
        
        # Initialize the underlying API client
        self._configuration = Configuration(
            host=self._base_url,
        )
        self._configuration.debug = debug
        
        # Create the API client
        self._api_client = ApiClient(
            configuration=self._configuration,
            header_name="Authorization",
            header_value=f"Bearer {api_key}",
        )
        
        # Set timeout
        self._api_client.rest_client.pool_manager.connection_pool_kw["timeout"] = timeout
        
        # Initialize resource managers (lazy loading)
        self._subscription: Optional[SubscriptionResource] = None
        self._user: Optional[UserResource] = None
        self._invoice: Optional[InvoiceResource] = None
        self._payment: Optional[PaymentResource] = None
        self._plan: Optional[PlanResource] = None
        self._product: Optional[ProductResource] = None
        self._webhook: Optional[WebhookResource] = None
        self._gateway: Optional[GatewayResource] = None
        self._member: Optional[MemberResource] = None
        self._metric: Optional[MetricResource] = None
        self._discount: Optional[DiscountResource] = None
        self._session: Optional[SessionResource] = None
        self._credit: Optional[CreditResource] = None
        self._vat: Optional[VatResource] = None
        self._search: Optional[SearchResource] = None
        self._role: Optional[RoleResource] = None
    
    @property
    def api_client(self) -> ApiClient:
        """Get the underlying OpenAPI client for advanced usage."""
        return self._api_client
    
    @property
    def subscription(self) -> SubscriptionResource:
        """
        Subscription management operations.
        
        Example:
            >>> # List all subscriptions
            >>> subs = client.subscription.list()
            >>> 
            >>> # Get subscription details
            >>> sub = client.subscription.get(subscription_id="sub_123")
            >>> 
            >>> # Create subscription
            >>> sub = client.subscription.create(user_id=123, plan_id=456)
            >>> 
            >>> # Cancel subscription
            >>> client.subscription.cancel(subscription_id="sub_123")
        """
        if self._subscription is None:
            self._subscription = SubscriptionResource(self._api_client)
        return self._subscription
    
    @property
    def user(self) -> UserResource:
        """
        User management operations.
        
        Example:
            >>> # List users
            >>> users = client.user.list()
            >>> 
            >>> # Get user profile
            >>> user = client.user.get(user_id=123)
            >>> 
            >>> # Create new user
            >>> user = client.user.create(email="user@example.com")
            >>> 
            >>> # Update user
            >>> client.user.update(user_id=123, first_name="John")
        """
        if self._user is None:
            self._user = UserResource(self._api_client)
        return self._user
    
    @property
    def invoice(self) -> InvoiceResource:
        """
        Invoice management operations.
        
        Example:
            >>> # List invoices
            >>> invoices = client.invoice.list()
            >>> 
            >>> # Get invoice details
            >>> invoice = client.invoice.get(invoice_id="inv_123")
            >>> 
            >>> # Create new invoice
            >>> invoice = client.invoice.create(user_id=123)
        """
        if self._invoice is None:
            self._invoice = InvoiceResource(self._api_client)
        return self._invoice
    
    @property
    def payment(self) -> PaymentResource:
        """
        Payment management operations.
        
        Example:
            >>> # List payments
            >>> payments = client.payment.list()
            >>> 
            >>> # Get payment details
            >>> payment = client.payment.get(payment_id="pay_123")
            >>> 
            >>> # Create new payment
            >>> payment = client.payment.create(user_id=123, amount=1000)
        """
        if self._payment is None:
            self._payment = PaymentResource(self._api_client)
        return self._payment
    
    @property
    def plan(self) -> PlanResource:
        """
        Plan management operations.
        
        Example:
            >>> # List plans
            >>> plans = client.plan.list()
            >>> 
            >>> # Get plan details
            >>> plan = client.plan.get(plan_id=123)
            >>> 
            >>> # Create new plan
            >>> plan = client.plan.create(plan_name="Pro Plan", amount=9900)
        """
        if self._plan is None:
            self._plan = PlanResource(self._api_client)
        return self._plan
    
    @property
    def product(self) -> ProductResource:
        """
        Product management operations.
        
        Example:
            >>> # List products
            >>> products = client.product.list()
            >>> 
            >>> # Get product details
            >>> product = client.product.get(product_id=123)
        """
        if self._product is None:
            self._product = ProductResource(self._api_client)
        return self._product
    
    @property
    def webhook(self) -> WebhookResource:
        """
        Webhook endpoint management.
        
        Example:
            >>> # List webhook endpoints
            >>> endpoints = client.webhook.list_endpoints()
            >>> 
            >>> # Create new endpoint
            >>> endpoint = client.webhook.create_endpoint(
            ...     url="https://example.com/webhooks",
            ...     events=["subscription.created", "payment.completed"]
            ... )
        """
        if self._webhook is None:
            self._webhook = WebhookResource(self._api_client)
        return self._webhook
    
    @property
    def gateway(self) -> GatewayResource:
        """
        Payment gateway management.
        
        Example:
            >>> # List gateways
            >>> gateways = client.gateway.list()
            >>> 
            >>> # Setup a gateway
            >>> client.gateway.setup(gateway_name="stripe", api_key="sk_...")
        """
        if self._gateway is None:
            self._gateway = GatewayResource(self._api_client)
        return self._gateway
    
    @property
    def member(self) -> MemberResource:
        """
        Merchant member management (admin users).
        
        Example:
            >>> # List members
            >>> members = client.member.list()
            >>> 
            >>> # Get member profile
            >>> profile = client.member.get_profile()
        """
        if self._member is None:
            self._member = MemberResource(self._api_client)
        return self._member
    
    @property
    def metric(self) -> MetricResource:
        """
        Billable metrics management.
        
        Example:
            >>> # List metrics
            >>> metrics = client.metric.list()
            >>> 
            >>> # Create new metric
            >>> metric = client.metric.create(metric_name="API Calls")
        """
        if self._metric is None:
            self._metric = MetricResource(self._api_client)
        return self._metric
    
    @property
    def discount(self) -> DiscountResource:
        """
        Discount code management.
        
        Example:
            >>> # List discount codes
            >>> codes = client.discount.list()
            >>> 
            >>> # Create discount code
            >>> code = client.discount.create(code="SAVE20", discount_percentage=20)
        """
        if self._discount is None:
            self._discount = DiscountResource(self._api_client)
        return self._discount
    
    @property
    def session(self) -> SessionResource:
        """
        Session management (checkout sessions, user portal sessions).
        
        Example:
            >>> # Create checkout session
            >>> session = client.session.create_checkout(
            ...     user_id=123,
            ...     plan_id=456,
            ...     success_url="https://example.com/success",
            ...     cancel_url="https://example.com/cancel"
            ... )
        """
        if self._session is None:
            self._session = SessionResource(self._api_client)
        return self._session
    
    @property
    def credit(self) -> CreditResource:
        """
        Promo credit management.
        
        Example:
            >>> # Get user credit balance
            >>> credit = client.credit.get_balance(user_id=123)
            >>> 
            >>> # Add credit
            >>> client.credit.add(user_id=123, amount=1000)
        """
        if self._credit is None:
            self._credit = CreditResource(self._api_client)
        return self._credit
    
    @property
    def vat(self) -> VatResource:
        """
        VAT/Tax configuration.
        
        Example:
            >>> # Get VAT country list
            >>> countries = client.vat.list_countries()
            >>> 
            >>> # Validate VAT number
            >>> result = client.vat.validate_number(vat_number="DE123456789")
        """
        if self._vat is None:
            self._vat = VatResource(self._api_client)
        return self._vat
    
    @property
    def search(self) -> SearchResource:
        """
        Global search functionality.
        
        Example:
            >>> # Search across all resources
            >>> results = client.search.search(query="john@example.com")
        """
        if self._search is None:
            self._search = SearchResource(self._api_client)
        return self._search
    
    @property
    def role(self) -> RoleResource:
        """
        Admin role management.
        
        Example:
            >>> # List roles
            >>> roles = client.role.list()
            >>> 
            >>> # Create new role
            >>> role = client.role.create(role_name="Support", permissions=[...])
        """
        if self._role is None:
            self._role = RoleResource(self._api_client)
        return self._role
    
    def __enter__(self):
        """Context manager support."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager support - cleanup."""
        pass
    
    def __repr__(self) -> str:
        return f"UniBeeClient(base_url={self._base_url!r})"


# Convenience function for creating a client
def create_client(
    api_key: str,
    sandbox: bool = False,
    **kwargs
) -> UniBeeClient:
    """
    Create a UniBee client with common defaults.
    
    Args:
        api_key: Your UniBee API key
        sandbox: If True, use sandbox environment (default: False)
        **kwargs: Additional arguments passed to UniBeeClient
        
    Returns:
        Configured UniBeeClient instance
        
    Example:
        >>> from unibee import create_client
        >>> 
        >>> # Production client
        >>> client = create_client("your_api_key")
        >>> 
        >>> # Sandbox client for testing
        >>> test_client = create_client("your_api_key", sandbox=True)
    """
    base_url = UniBeeClient.SANDBOX_URL if sandbox else UniBeeClient.PRODUCTION_URL
    return UniBeeClient(api_key=api_key, base_url=base_url, **kwargs)
