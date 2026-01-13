# coding: utf-8
"""
UniBee Checkout API

Manage checkout sessions and pages.
"""

from typing import Any, Dict, List, Optional

from unibee.api.base import BaseAPI


class CheckoutAPI(BaseAPI):
    """
    API for managing checkout sessions.
    
    Checkout sessions are used to create payment flows for
    subscriptions and one-time payments.
    
    Example:
        ```python
        from unibee import UniBeeClient
        
        client = UniBeeClient(api_key="your-api-key")
        
        # Create a new checkout session
        session = client.checkout.create_session(
            plan_id=123,
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
        )
        
        # Get checkout URL
        checkout_url = session.get("url")
        ```
    """
    
    def create_session(
        self,
        plan_id: int,
        success_url: str,
        cancel_url: str,
        user_id: Optional[int] = None,
        email: Optional[str] = None,
        quantity: int = 1,
        gateway_id: Optional[int] = None,
        discount_code: Optional[str] = None,
        addon_params: Optional[List[Dict[str, Any]]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create a new checkout session.
        
        Args:
            plan_id: The plan ID for the subscription.
            success_url: URL to redirect after successful payment.
            cancel_url: URL to redirect if checkout is cancelled.
            user_id: Existing user ID (optional).
            email: User email (creates new user if no user_id).
            quantity: Plan quantity.
            gateway_id: Payment gateway ID.
            discount_code: Discount code to apply.
            addon_params: List of addon parameters.
            metadata: Additional metadata for the subscription.
            **kwargs: Additional parameters.
        
        Returns:
            Checkout session with URL to redirect the user.
        """
        data = {
            "planId": plan_id,
            "successUrl": success_url,
            "cancelUrl": cancel_url,
            "userId": user_id,
            "email": email,
            "quantity": quantity,
            "gatewayId": gateway_id,
            "discountCode": discount_code,
            "addonParams": addon_params,
            "metadata": metadata,
            **kwargs,
        }
        return self._post("/merchant/session/new_session", data=data)
    
    def get_update_url(
        self,
        subscription_id: str,
        return_url: str,
    ) -> Dict[str, Any]:
        """
        Get URL for user to update their subscription.
        
        Args:
            subscription_id: The subscription ID.
            return_url: URL to redirect after update.
        
        Returns:
            Update page URL.
        """
        return self._post(
            "/merchant/session/subscription_update_url",
            data={
                "subscriptionId": subscription_id,
                "returnUrl": return_url,
            },
        )
    
    def list_checkouts(
        self,
        status: Optional[List[int]] = None,
        page: int = 0,
        count: int = 20,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        List merchant checkout configurations.
        
        Args:
            status: Filter by status.
            page: Page number (0-indexed).
            count: Number of results per page.
            **kwargs: Additional filter parameters.
        
        Returns:
            List of checkout configurations.
        """
        return self._post(
            "/merchant/checkout/list",
            data={
                "status": status,
                "page": page,
                "count": count,
                **kwargs,
            },
        )
    
    def get_checkout(
        self,
        checkout_id: int,
    ) -> Dict[str, Any]:
        """
        Get checkout configuration details.
        
        Args:
            checkout_id: The checkout configuration ID.
        
        Returns:
            Checkout configuration details.
        """
        return self._post(
            "/merchant/checkout/detail",
            data={"checkoutId": checkout_id},
        )
    
    def create_checkout(
        self,
        name: str,
        plan_ids: List[int],
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create a new checkout configuration.
        
        Args:
            name: Checkout name.
            plan_ids: List of plan IDs available in this checkout.
            **kwargs: Additional configuration parameters.
        
        Returns:
            Created checkout configuration.
        """
        data = {
            "name": name,
            "planIds": plan_ids,
            **kwargs,
        }
        return self._post("/merchant/checkout/new", data=data)
    
    def edit_checkout(
        self,
        checkout_id: int,
        name: Optional[str] = None,
        plan_ids: Optional[List[int]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Edit a checkout configuration.
        
        Args:
            checkout_id: The checkout configuration ID.
            name: New checkout name.
            plan_ids: New list of plan IDs.
            **kwargs: Additional parameters.
        
        Returns:
            Updated checkout configuration.
        """
        data = {
            "checkoutId": checkout_id,
            "name": name,
            "planIds": plan_ids,
            **kwargs,
        }
        return self._post("/merchant/checkout/edit", data=data)
    
    def archive_checkout(
        self,
        checkout_id: int,
    ) -> Dict[str, Any]:
        """
        Archive a checkout configuration.
        
        Args:
            checkout_id: The checkout configuration ID.
        
        Returns:
            Archived checkout configuration.
        """
        return self._post(
            "/merchant/checkout/archive",
            data={"checkoutId": checkout_id},
        )
    
    def get_checkout_link(
        self,
        checkout_id: int,
    ) -> Dict[str, Any]:
        """
        Get the checkout link for a configuration.
        
        Args:
            checkout_id: The checkout configuration ID.
        
        Returns:
            Checkout link details.
        """
        return self._get(
            "/merchant/checkout/link",
            params={"checkoutId": checkout_id},
        )
