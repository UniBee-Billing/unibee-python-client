# coding: utf-8
"""
UniBee Subscriptions API

Manage subscriptions for users.
"""

from typing import Any, Dict, List, Optional

from unibee.api.base import BaseAPI


class SubscriptionsAPI(BaseAPI):
    """
    API for managing subscriptions.
    
    Subscriptions represent recurring billing relationships between
    users and plans. This API allows you to create, update, cancel,
    and query subscriptions.
    
    Example:
        ```python
        from unibee import UniBeeClient
        
        client = UniBeeClient(api_key="your-api-key")
        
        # Get subscription details
        subscription = client.subscriptions.get(subscription_id="sub_123")
        
        # List subscriptions
        subscriptions = client.subscriptions.list(user_id=123)
        
        # Create a new subscription
        result = client.subscriptions.create(
            user_id=123,
            plan_id=456,
            gateway_id=1,
        )
        ```
    """
    
    def list(
        self,
        user_id: Optional[int] = None,
        status: Optional[List[int]] = None,
        plan_id: Optional[int] = None,
        page: int = 0,
        count: int = 20,
        sort_field: Optional[str] = None,
        sort_type: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        List subscriptions with optional filters.
        
        Args:
            user_id: Filter by user ID.
            status: Filter by subscription status(es).
                    Status values: 0=Init, 1=Pending, 2=Active, 3=PendingInActive,
                    4=Cancelled, 5=Expired, 6=Suspended, 7=Processing
            plan_id: Filter by plan ID.
            page: Page number (0-indexed).
            count: Number of results per page.
            sort_field: Field to sort by.
            sort_type: Sort direction ('asc' or 'desc').
            **kwargs: Additional filter parameters.
        
        Returns:
            Dictionary containing 'subscriptions' list and pagination info.
        """
        data = {
            "userId": user_id,
            "status": status,
            "planId": plan_id,
            "page": page,
            "count": count,
            "sortField": sort_field,
            "sortType": sort_type,
            **kwargs,
        }
        return self._post("/merchant/subscription/list", data=data)
    
    def get(
        self,
        subscription_id: str,
    ) -> Dict[str, Any]:
        """
        Get subscription details by ID.
        
        Args:
            subscription_id: The subscription ID.
        
        Returns:
            Subscription details including plan, user, and billing info.
        """
        return self._post(
            "/merchant/subscription/detail",
            data={"subscriptionId": subscription_id},
        )
    
    def get_by_user(
        self,
        user_id: int,
    ) -> Dict[str, Any]:
        """
        Get subscription details for a specific user.
        
        Args:
            user_id: The user ID.
        
        Returns:
            User's subscription details.
        """
        return self._post(
            "/merchant/subscription/user_subscription_detail",
            data={"userId": user_id},
        )
    
    def create_preview(
        self,
        plan_id: int,
        user_id: Optional[int] = None,
        email: Optional[str] = None,
        quantity: int = 1,
        gateway_id: Optional[int] = None,
        addon_params: Optional[List[Dict[str, Any]]] = None,
        discount_code: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Preview subscription creation (calculate amounts without creating).
        
        Args:
            plan_id: The plan ID to subscribe to.
            user_id: The user ID (provide either user_id or email).
            email: User email (provide either user_id or email).
            quantity: Plan quantity. Defaults to 1.
            gateway_id: Payment gateway ID.
            addon_params: List of addon parameters.
            discount_code: Discount code to apply.
            **kwargs: Additional parameters.
        
        Returns:
            Preview of subscription including calculated amounts and invoice.
        """
        data = {
            "planId": plan_id,
            "userId": user_id,
            "email": email,
            "quantity": quantity,
            "gatewayId": gateway_id,
            "addonParams": addon_params,
            "discountCode": discount_code,
            **kwargs,
        }
        return self._post("/merchant/subscription/create_preview", data=data)
    
    def create(
        self,
        plan_id: int,
        user_id: Optional[int] = None,
        email: Optional[str] = None,
        quantity: int = 1,
        gateway_id: Optional[int] = None,
        addon_params: Optional[List[Dict[str, Any]]] = None,
        discount_code: Optional[str] = None,
        return_url: Optional[str] = None,
        cancel_url: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create a new subscription for a user.
        
        Args:
            plan_id: The plan ID to subscribe to.
            user_id: The user ID (provide either user_id or email).
            email: User email (provide either user_id or email).
            quantity: Plan quantity. Defaults to 1.
            gateway_id: Payment gateway ID.
            addon_params: List of addon parameters with format:
                          [{"addonPlanId": 123, "quantity": 1}]
            discount_code: Discount code to apply.
            return_url: URL to redirect after successful payment.
            cancel_url: URL to redirect if payment is cancelled.
            metadata: Additional metadata for the subscription.
            **kwargs: Additional parameters.
        
        Returns:
            Created subscription details including payment link if applicable.
        """
        data = {
            "planId": plan_id,
            "userId": user_id,
            "email": email,
            "quantity": quantity,
            "gatewayId": gateway_id,
            "addonParams": addon_params,
            "discountCode": discount_code,
            "returnUrl": return_url,
            "cancelUrl": cancel_url,
            "metadata": metadata,
            **kwargs,
        }
        return self._post("/merchant/subscription/create_submit", data=data)
    
    def update_preview(
        self,
        subscription_id: str,
        new_plan_id: int,
        quantity: Optional[int] = None,
        addon_params: Optional[List[Dict[str, Any]]] = None,
        proration_date: Optional[int] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Preview subscription update (calculate prorated amounts).
        
        Args:
            subscription_id: The subscription ID to update.
            new_plan_id: The new plan ID.
            quantity: New quantity.
            addon_params: New addon parameters.
            proration_date: Unix timestamp for proration calculation.
            **kwargs: Additional parameters.
        
        Returns:
            Preview of subscription update including prorated amounts.
        """
        data = {
            "subscriptionId": subscription_id,
            "newPlanId": new_plan_id,
            "quantity": quantity,
            "addonParams": addon_params,
            "prorationDate": proration_date,
            **kwargs,
        }
        return self._post("/merchant/subscription/update_preview", data=data)
    
    def update(
        self,
        subscription_id: str,
        new_plan_id: int,
        quantity: Optional[int] = None,
        addon_params: Optional[List[Dict[str, Any]]] = None,
        proration_date: Optional[int] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update an existing subscription (change plan, quantity, etc.).
        
        Args:
            subscription_id: The subscription ID to update.
            new_plan_id: The new plan ID.
            quantity: New quantity.
            addon_params: New addon parameters.
            proration_date: Unix timestamp for proration calculation.
            **kwargs: Additional parameters.
        
        Returns:
            Updated subscription details.
        """
        data = {
            "subscriptionId": subscription_id,
            "newPlanId": new_plan_id,
            "quantity": quantity,
            "addonParams": addon_params,
            "prorationDate": proration_date,
            **kwargs,
        }
        return self._post("/merchant/subscription/update_submit", data=data)
    
    def cancel(
        self,
        subscription_id: str,
        prorate: bool = False,
    ) -> Dict[str, Any]:
        """
        Cancel a subscription immediately.
        
        Args:
            subscription_id: The subscription ID to cancel.
            prorate: Whether to prorate the cancellation.
        
        Returns:
            Cancelled subscription details.
        """
        return self._post(
            "/merchant/subscription/cancel",
            data={
                "subscriptionId": subscription_id,
                "prorate": prorate,
            },
        )
    
    def cancel_at_period_end(
        self,
        subscription_id: str,
    ) -> Dict[str, Any]:
        """
        Cancel a subscription at the end of the current billing period.
        
        The subscription will remain active until the period ends.
        
        Args:
            subscription_id: The subscription ID.
        
        Returns:
            Updated subscription details.
        """
        return self._post(
            "/merchant/subscription/cancel_at_period_end",
            data={"subscriptionId": subscription_id},
        )
    
    def resume_cancel_at_period_end(
        self,
        subscription_id: str,
    ) -> Dict[str, Any]:
        """
        Resume a subscription that was set to cancel at period end.
        
        Args:
            subscription_id: The subscription ID.
        
        Returns:
            Updated subscription details.
        """
        return self._post(
            "/merchant/subscription/cancel_last_cancel_at_period_end",
            data={"subscriptionId": subscription_id},
        )
    
    def suspend(
        self,
        subscription_id: str,
    ) -> Dict[str, Any]:
        """
        Suspend an active subscription.
        
        Args:
            subscription_id: The subscription ID.
        
        Returns:
            Updated subscription details.
        """
        return self._post(
            "/merchant/subscription/suspend",
            data={"subscriptionId": subscription_id},
        )
    
    def resume(
        self,
        subscription_id: str,
    ) -> Dict[str, Any]:
        """
        Resume a suspended subscription.
        
        Args:
            subscription_id: The subscription ID.
        
        Returns:
            Updated subscription details.
        """
        return self._post(
            "/merchant/subscription/resume",
            data={"subscriptionId": subscription_id},
        )
    
    def change_gateway(
        self,
        subscription_id: str,
        gateway_id: int,
    ) -> Dict[str, Any]:
        """
        Change the payment gateway for a subscription.
        
        Args:
            subscription_id: The subscription ID.
            gateway_id: The new gateway ID.
        
        Returns:
            Updated subscription details.
        """
        return self._post(
            "/merchant/subscription/change_gateway",
            data={
                "subscriptionId": subscription_id,
                "gatewayId": gateway_id,
            },
        )
    
    def renew(
        self,
        subscription_id: str,
    ) -> Dict[str, Any]:
        """
        Manually trigger subscription renewal.
        
        Args:
            subscription_id: The subscription ID.
        
        Returns:
            Renewal result.
        """
        return self._post(
            "/merchant/subscription/renew",
            data={"subscriptionId": subscription_id},
        )
    
    def add_trial(
        self,
        subscription_id: str,
        trial_hours: int,
    ) -> Dict[str, Any]:
        """
        Add trial time to a subscription.
        
        Args:
            subscription_id: The subscription ID.
            trial_hours: Number of trial hours to add.
        
        Returns:
            Updated subscription details.
        """
        return self._post(
            "/merchant/subscription/add_new_trial_start",
            data={
                "subscriptionId": subscription_id,
                "appendTrialEndHour": trial_hours,
            },
        )
    
    def get_timeline(
        self,
        subscription_id: str,
        page: int = 0,
        count: int = 20,
    ) -> Dict[str, Any]:
        """
        Get subscription timeline/history.
        
        Args:
            subscription_id: The subscription ID.
            page: Page number (0-indexed).
            count: Number of results per page.
        
        Returns:
            List of timeline events.
        """
        return self._post(
            "/merchant/subscription/timeline_list",
            data={
                "subscriptionId": subscription_id,
                "page": page,
                "count": count,
            },
        )
    
    def list_notes(
        self,
        subscription_id: str,
        page: int = 0,
        count: int = 20,
    ) -> Dict[str, Any]:
        """
        List admin notes for a subscription.
        
        Args:
            subscription_id: The subscription ID.
            page: Page number (0-indexed).
            count: Number of results per page.
        
        Returns:
            List of admin notes.
        """
        return self._post(
            "/merchant/subscription/admin_note_list",
            data={
                "subscriptionId": subscription_id,
                "page": page,
                "count": count,
            },
        )
    
    def add_note(
        self,
        subscription_id: str,
        note: str,
    ) -> Dict[str, Any]:
        """
        Add an admin note to a subscription.
        
        Args:
            subscription_id: The subscription ID.
            note: The note content.
        
        Returns:
            Created note details.
        """
        return self._post(
            "/merchant/subscription/new_admin_note",
            data={
                "subscriptionId": subscription_id,
                "note": note,
            },
        )
    
    def get_config(self) -> Dict[str, Any]:
        """
        Get merchant subscription configuration.
        
        Returns:
            Subscription configuration settings.
        """
        return self._get("/merchant/subscription/config")
    
    def update_config(
        self,
        **config,
    ) -> Dict[str, Any]:
        """
        Update merchant subscription configuration.
        
        Args:
            **config: Configuration parameters to update.
        
        Returns:
            Updated configuration.
        """
        return self._post("/merchant/subscription/config/update", data=config)
