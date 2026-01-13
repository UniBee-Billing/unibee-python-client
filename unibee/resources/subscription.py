# coding: utf-8
"""
Subscription Resource

Provides methods for managing subscriptions in UniBee.
"""

from typing import Any, Dict, List, Optional

from openapi_client import ApiClient
from openapi_client.api.subscription import Subscription as SubscriptionApi
from openapi_client.rest import ApiException

from unibee.resources.base import BaseResource


class SubscriptionResource(BaseResource):
    """
    Subscription management resource.
    
    Provides methods for creating, updating, canceling, and querying subscriptions.
    
    Example:
        >>> # List all subscriptions
        >>> subs = client.subscription.list()
        >>> 
        >>> # Get subscription details
        >>> sub = client.subscription.get(subscription_id="sub_123")
        >>> 
        >>> # Create a new subscription
        >>> sub = client.subscription.create(
        ...     user_id=123,
        ...     plan_id=456,
        ...     gateway_id=789
        ... )
        >>> 
        >>> # Cancel subscription immediately
        >>> client.subscription.cancel(subscription_id="sub_123")
        >>> 
        >>> # Cancel at period end
        >>> client.subscription.cancel_at_period_end(subscription_id="sub_123")
    """
    
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)
        self._api = SubscriptionApi(api_client)
    
    def list(
        self,
        user_id: Optional[int] = None,
        status: Optional[List[int]] = None,
        plan_id: Optional[int] = None,
        page: int = 0,
        count: int = 20,
        sort_field: Optional[str] = None,
        sort_type: Optional[str] = None,
        **kwargs
    ) -> Any:
        """
        List subscriptions with optional filters.
        
        Args:
            user_id: Filter by user ID
            status: Filter by subscription status codes
            plan_id: Filter by plan ID
            page: Page number (0-indexed)
            count: Number of items per page
            sort_field: Field to sort by
            sort_type: Sort direction ("asc" or "desc")
            
        Returns:
            List of subscriptions
            
        Example:
            >>> # Get all active subscriptions
            >>> subs = client.subscription.list(status=[2])  # 2 = active
            >>> 
            >>> # Get subscriptions for a specific user
            >>> subs = client.subscription.list(user_id=123)
        """
        try:
            response = self._api.subscription_list_get(
                user_id=user_id,
                status=status,
                plan_id=plan_id,
                page=page,
                count=count,
                sort_field=sort_field,
                sort_type=sort_type,
            )
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def get(
        self,
        subscription_id: str,
        **kwargs
    ) -> Any:
        """
        Get subscription details.
        
        Args:
            subscription_id: The subscription ID
            
        Returns:
            Subscription details
            
        Example:
            >>> sub = client.subscription.get(subscription_id="sub_123")
            >>> print(sub.status, sub.plan_id)
        """
        try:
            response = self._api.subscription_detail_get(
                subscription_id=subscription_id,
            )
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def get_by_user(
        self,
        user_id: int,
        **kwargs
    ) -> Any:
        """
        Get user's current subscription details.
        
        Args:
            user_id: The user ID
            
        Returns:
            User's subscription details
            
        Example:
            >>> sub = client.subscription.get_by_user(user_id=123)
        """
        try:
            response = self._api.subscription_user_subscription_detail_get(
                user_id=user_id,
            )
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def create_preview(
        self,
        user_id: int,
        plan_id: int,
        gateway_id: int,
        quantity: int = 1,
        addon_params: Optional[List[Dict]] = None,
        discount_code: Optional[str] = None,
        **kwargs
    ) -> Any:
        """
        Preview subscription creation (get pricing without creating).
        
        Args:
            user_id: The user ID
            plan_id: The plan ID
            gateway_id: The payment gateway ID
            quantity: Subscription quantity
            addon_params: Optional addon configurations
            discount_code: Optional discount code
            
        Returns:
            Subscription preview with pricing details
            
        Example:
            >>> preview = client.subscription.create_preview(
            ...     user_id=123,
            ...     plan_id=456,
            ...     gateway_id=789
            ... )
            >>> print(f"Total: {preview.total_amount}")
        """
        from openapi_client.models.unibee_api_merchant_subscription_create_preview_req import (
            UnibeeApiMerchantSubscriptionCreatePreviewReq
        )
        
        try:
            req = UnibeeApiMerchantSubscriptionCreatePreviewReq(
                user_id=user_id,
                plan_id=plan_id,
                gateway_id=gateway_id,
                quantity=quantity,
                addon_params=addon_params,
                discount_code=discount_code,
            )
            response = self._api.subscription_create_preview_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def create(
        self,
        user_id: int,
        plan_id: int,
        gateway_id: int,
        quantity: int = 1,
        addon_params: Optional[List[Dict]] = None,
        discount_code: Optional[str] = None,
        return_url: Optional[str] = None,
        cancel_url: Optional[str] = None,
        trial_end: Optional[int] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Any:
        """
        Create a new subscription.
        
        Args:
            user_id: The user ID
            plan_id: The plan ID
            gateway_id: The payment gateway ID
            quantity: Subscription quantity
            addon_params: Optional addon configurations
            discount_code: Optional discount code
            return_url: URL to redirect after successful payment
            cancel_url: URL to redirect if payment is cancelled
            trial_end: Trial end timestamp (Unix timestamp)
            metadata: Additional metadata to store with subscription
            
        Returns:
            Created subscription details (may include payment link if payment required)
            
        Example:
            >>> sub = client.subscription.create(
            ...     user_id=123,
            ...     plan_id=456,
            ...     gateway_id=789,
            ...     return_url="https://example.com/success",
            ...     cancel_url="https://example.com/cancel"
            ... )
            >>> if sub.link:
            ...     print(f"Payment required: {sub.link}")
        """
        from openapi_client.models.unibee_api_merchant_subscription_create_req import (
            UnibeeApiMerchantSubscriptionCreateReq
        )
        
        try:
            req = UnibeeApiMerchantSubscriptionCreateReq(
                user_id=user_id,
                plan_id=plan_id,
                gateway_id=gateway_id,
                quantity=quantity,
                addon_params=addon_params,
                discount_code=discount_code,
                return_url=return_url,
                cancel_url=cancel_url,
                trial_end=trial_end,
                metadata=metadata,
            )
            response = self._api.subscription_create_submit_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def update_preview(
        self,
        subscription_id: str,
        new_plan_id: int,
        quantity: int = 1,
        addon_params: Optional[List[Dict]] = None,
        proration_date: Optional[int] = None,
        **kwargs
    ) -> Any:
        """
        Preview subscription update (plan change).
        
        Args:
            subscription_id: The subscription ID
            new_plan_id: The new plan ID
            quantity: New quantity
            addon_params: New addon configurations
            proration_date: Custom proration date
            
        Returns:
            Update preview with pricing details
            
        Example:
            >>> preview = client.subscription.update_preview(
            ...     subscription_id="sub_123",
            ...     new_plan_id=789
            ... )
            >>> print(f"Proration amount: {preview.proration_amount}")
        """
        from openapi_client.models.unibee_api_merchant_subscription_update_preview_req import (
            UnibeeApiMerchantSubscriptionUpdatePreviewReq
        )
        
        try:
            req = UnibeeApiMerchantSubscriptionUpdatePreviewReq(
                subscription_id=subscription_id,
                new_plan_id=new_plan_id,
                quantity=quantity,
                addon_params=addon_params,
                proration_date=proration_date,
            )
            response = self._api.subscription_update_preview_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def update(
        self,
        subscription_id: str,
        new_plan_id: int,
        quantity: int = 1,
        addon_params: Optional[List[Dict]] = None,
        proration_date: Optional[int] = None,
        **kwargs
    ) -> Any:
        """
        Update subscription (change plan).
        
        Args:
            subscription_id: The subscription ID
            new_plan_id: The new plan ID
            quantity: New quantity
            addon_params: New addon configurations
            proration_date: Custom proration date
            
        Returns:
            Updated subscription details
            
        Example:
            >>> sub = client.subscription.update(
            ...     subscription_id="sub_123",
            ...     new_plan_id=789
            ... )
        """
        from openapi_client.models.unibee_api_merchant_subscription_update_req import (
            UnibeeApiMerchantSubscriptionUpdateReq
        )
        
        try:
            req = UnibeeApiMerchantSubscriptionUpdateReq(
                subscription_id=subscription_id,
                new_plan_id=new_plan_id,
                quantity=quantity,
                addon_params=addon_params,
                proration_date=proration_date,
            )
            response = self._api.subscription_update_submit_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def cancel(
        self,
        subscription_id: str,
        prorate: bool = True,
        **kwargs
    ) -> Any:
        """
        Cancel subscription immediately.
        
        Args:
            subscription_id: The subscription ID
            prorate: Whether to prorate the cancellation
            
        Returns:
            Cancellation result
            
        Example:
            >>> client.subscription.cancel(subscription_id="sub_123")
        """
        from openapi_client.models.unibee_api_merchant_subscription_cancel_req import (
            UnibeeApiMerchantSubscriptionCancelReq
        )
        
        try:
            req = UnibeeApiMerchantSubscriptionCancelReq(
                subscription_id=subscription_id,
                prorate=prorate,
            )
            response = self._api.subscription_cancel_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def cancel_at_period_end(
        self,
        subscription_id: str,
        **kwargs
    ) -> Any:
        """
        Cancel subscription at the end of current billing period.
        
        Args:
            subscription_id: The subscription ID
            
        Returns:
            Cancellation result
            
        Example:
            >>> client.subscription.cancel_at_period_end(subscription_id="sub_123")
        """
        from openapi_client.models.unibee_api_merchant_subscription_cancel_at_period_end_req import (
            UnibeeApiMerchantSubscriptionCancelAtPeriodEndReq
        )
        
        try:
            req = UnibeeApiMerchantSubscriptionCancelAtPeriodEndReq(
                subscription_id=subscription_id,
            )
            response = self._api.subscription_cancel_at_period_end_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def revert_cancel(
        self,
        subscription_id: str,
        **kwargs
    ) -> Any:
        """
        Revert a pending cancellation (undo cancel_at_period_end).
        
        Args:
            subscription_id: The subscription ID
            
        Returns:
            Result
            
        Example:
            >>> client.subscription.revert_cancel(subscription_id="sub_123")
        """
        from openapi_client.models.unibee_api_merchant_subscription_cancel_last_cancel_at_period_end_req import (
            UnibeeApiMerchantSubscriptionCancelLastCancelAtPeriodEndReq
        )
        
        try:
            req = UnibeeApiMerchantSubscriptionCancelLastCancelAtPeriodEndReq(
                subscription_id=subscription_id,
            )
            response = self._api.subscription_cancel_last_cancel_at_period_end_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def suspend(
        self,
        subscription_id: str,
        **kwargs
    ) -> Any:
        """
        Suspend (pause) a subscription.
        
        Args:
            subscription_id: The subscription ID
            
        Returns:
            Result
            
        Example:
            >>> client.subscription.suspend(subscription_id="sub_123")
        """
        from openapi_client.models.unibee_api_merchant_subscription_suspend_req import (
            UnibeeApiMerchantSubscriptionSuspendReq
        )
        
        try:
            req = UnibeeApiMerchantSubscriptionSuspendReq(
                subscription_id=subscription_id,
            )
            response = self._api.subscription_suspend_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def resume(
        self,
        subscription_id: str,
        **kwargs
    ) -> Any:
        """
        Resume a suspended subscription.
        
        Args:
            subscription_id: The subscription ID
            
        Returns:
            Result
            
        Example:
            >>> client.subscription.resume(subscription_id="sub_123")
        """
        from openapi_client.models.unibee_api_merchant_subscription_resume_req import (
            UnibeeApiMerchantSubscriptionResumeReq
        )
        
        try:
            req = UnibeeApiMerchantSubscriptionResumeReq(
                subscription_id=subscription_id,
            )
            response = self._api.subscription_resume_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def change_gateway(
        self,
        subscription_id: str,
        gateway_id: int,
        **kwargs
    ) -> Any:
        """
        Change the payment gateway for a subscription.
        
        Args:
            subscription_id: The subscription ID
            gateway_id: The new gateway ID
            
        Returns:
            Result
            
        Example:
            >>> client.subscription.change_gateway(
            ...     subscription_id="sub_123",
            ...     gateway_id=456
            ... )
        """
        from openapi_client.models.unibee_api_merchant_subscription_change_gateway_req import (
            UnibeeApiMerchantSubscriptionChangeGatewayReq
        )
        
        try:
            req = UnibeeApiMerchantSubscriptionChangeGatewayReq(
                subscription_id=subscription_id,
                gateway_id=gateway_id,
            )
            response = self._api.subscription_change_gateway_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def add_trial(
        self,
        subscription_id: str,
        trial_hours: int,
        **kwargs
    ) -> Any:
        """
        Extend trial period for a subscription.
        
        Args:
            subscription_id: The subscription ID
            trial_hours: Number of hours to add to trial
            
        Returns:
            Result
            
        Example:
            >>> # Add 24 hours to trial
            >>> client.subscription.add_trial(
            ...     subscription_id="sub_123",
            ...     trial_hours=24
            ... )
        """
        from openapi_client.models.unibee_api_merchant_subscription_add_new_trial_start_req import (
            UnibeeApiMerchantSubscriptionAddNewTrialStartReq
        )
        
        try:
            req = UnibeeApiMerchantSubscriptionAddNewTrialStartReq(
                subscription_id=subscription_id,
                append_trial_end_hour=trial_hours,
            )
            response = self._api.subscription_add_new_trial_start_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def get_config(self, **kwargs) -> Any:
        """
        Get subscription configuration settings.
        
        Returns:
            Subscription config
            
        Example:
            >>> config = client.subscription.get_config()
        """
        try:
            response = self._api.subscription_config_get()
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
