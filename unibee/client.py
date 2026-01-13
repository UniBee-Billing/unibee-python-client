# coding: utf-8
"""
UniBee Python SDK Client

Main entry point for the UniBee Python SDK.
"""

from typing import Optional

from unibee.configuration import Configuration
from unibee.http_client import HTTPClient
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


class UniBeeClient:
    """
    UniBee API Client.
    
    The main entry point for interacting with the UniBee API.
    Provides access to all API resources through a simple, unified interface.
    
    Example:
        ```python
        from unibee import UniBeeClient
        
        # Initialize with API key
        client = UniBeeClient(api_key="your-api-key")
        
        # Or use environment variable UNIBEE_API_KEY
        client = UniBeeClient()
        
        # Use sandbox environment for testing
        client = UniBeeClient.sandbox(api_key="your-api-key")
        
        # Access API resources
        users = client.users.list()
        subscription = client.subscriptions.get(subscription_id="sub_123")
        ```
    
    Attributes:
        subscriptions: Manage subscriptions.
        plans: Manage subscription plans.
        invoices: Manage invoices.
        payments: Manage payments and payment methods.
        users: Manage users (customers).
        webhooks: Manage webhook endpoints.
        merchants: Manage merchant profile and settings.
        discounts: Manage discount codes.
        products: Manage products.
        gateways: Manage payment gateways.
        checkout: Manage checkout sessions.
        credit: Manage credits and promo credits.
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: int = 30,
        debug: bool = False,
    ):
        """
        Initialize the UniBee client.
        
        Args:
            api_key: API key for authentication. If not provided,
                     reads from UNIBEE_API_KEY environment variable.
            base_url: Base URL for the API. Defaults to production URL.
                     Can also be set via UNIBEE_BASE_URL environment variable.
            timeout: Request timeout in seconds. Defaults to 30.
            debug: Enable debug logging. Defaults to False.
        
        Raises:
            ValueError: If API key is not configured when making API calls.
        """
        self._config = Configuration(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            debug=debug,
        )
        self._http = HTTPClient(self._config)
        
        # Initialize API resources
        self.subscriptions = SubscriptionsAPI(self._http)
        self.plans = PlansAPI(self._http)
        self.invoices = InvoicesAPI(self._http)
        self.payments = PaymentsAPI(self._http)
        self.users = UsersAPI(self._http)
        self.webhooks = WebhooksAPI(self._http)
        self.merchants = MerchantsAPI(self._http)
        self.discounts = DiscountsAPI(self._http)
        self.products = ProductsAPI(self._http)
        self.gateways = GatewaysAPI(self._http)
        self.checkout = CheckoutAPI(self._http)
        self.credit = CreditAPI(self._http)
    
    @classmethod
    def sandbox(
        cls,
        api_key: Optional[str] = None,
        **kwargs,
    ) -> "UniBeeClient":
        """
        Create a client configured for the sandbox environment.
        
        Use this for testing and development.
        
        Args:
            api_key: API key for sandbox environment.
            **kwargs: Additional configuration options.
        
        Returns:
            UniBeeClient instance configured for sandbox.
        
        Example:
            ```python
            client = UniBeeClient.sandbox(api_key="sandbox-api-key")
            ```
        """
        return cls(
            api_key=api_key,
            base_url=Configuration.SANDBOX_BASE_URL,
            **kwargs,
        )
    
    @classmethod
    def production(
        cls,
        api_key: Optional[str] = None,
        **kwargs,
    ) -> "UniBeeClient":
        """
        Create a client configured for the production environment.
        
        Args:
            api_key: API key for production environment.
            **kwargs: Additional configuration options.
        
        Returns:
            UniBeeClient instance configured for production.
        
        Example:
            ```python
            client = UniBeeClient.production(api_key="live-api-key")
            ```
        """
        return cls(
            api_key=api_key,
            base_url=Configuration.DEFAULT_BASE_URL,
            **kwargs,
        )
    
    @property
    def config(self) -> Configuration:
        """
        Get the current configuration.
        
        Returns:
            Configuration instance.
        """
        return self._config
    
    def __repr__(self) -> str:
        return f"UniBeeClient(base_url={self._config.base_url!r})"
