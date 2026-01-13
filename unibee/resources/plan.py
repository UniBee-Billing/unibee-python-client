# coding: utf-8
"""
Plan Resource

Provides methods for managing subscription plans in UniBee.
"""

from typing import Any, Dict, List, Optional

from openapi_client import ApiClient
from openapi_client.api.plan import Plan as PlanApi
from openapi_client.rest import ApiException

from unibee.resources.base import BaseResource


class PlanResource(BaseResource):
    """
    Plan management resource.
    
    Provides methods for creating, updating, and managing subscription plans.
    """
    
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)
        self._api = PlanApi(api_client)
    
    def list(
        self,
        product_id: Optional[int] = None,
        status: Optional[List[int]] = None,
        plan_type: Optional[List[int]] = None,
        page: int = 0,
        count: int = 20,
        **kwargs
    ) -> Any:
        """
        List plans with optional filters.
        
        Args:
            product_id: Filter by product ID
            status: Filter by plan status codes
            plan_type: Filter by plan type (1=main, 2=addon, 3=one-time)
            page: Page number
            count: Items per page
            
        Returns:
            List of plans
        """
        try:
            response = self._api.plan_list_get(
                product_id=product_id,
                status=status,
                type=plan_type,
                page=page,
                count=count,
            )
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def get(
        self,
        plan_id: int,
        **kwargs
    ) -> Any:
        """
        Get plan details.
        
        Args:
            plan_id: The plan ID
            
        Returns:
            Plan details
        """
        try:
            response = self._api.plan_detail_get(
                plan_id=plan_id,
            )
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def create(
        self,
        plan_name: str,
        currency: str,
        amount: int,
        interval_unit: str = "month",
        interval_count: int = 1,
        product_id: Optional[int] = None,
        description: Optional[str] = None,
        trial_duration_time: Optional[int] = None,
        **kwargs
    ) -> Any:
        """
        Create a new subscription plan.
        
        Args:
            plan_name: Plan name
            currency: Currency code (e.g., "USD")
            amount: Price in cents
            interval_unit: Billing interval unit ("day", "week", "month", "year")
            interval_count: Number of intervals between billings
            product_id: Product ID to associate with
            description: Plan description
            trial_duration_time: Trial duration in days
            
        Returns:
            Created plan details
            
        Example:
            >>> plan = client.plan.create(
            ...     plan_name="Pro Monthly",
            ...     currency="USD",
            ...     amount=9900,
            ...     interval_unit="month",
            ...     interval_count=1
            ... )
        """
        from openapi_client.models.unibee_api_merchant_plan_new_req import (
            UnibeeApiMerchantPlanNewReq
        )
        
        try:
            req = UnibeeApiMerchantPlanNewReq(
                plan_name=plan_name,
                currency=currency,
                amount=amount,
                interval_unit=interval_unit,
                interval_count=interval_count,
                product_id=product_id,
                description=description,
                trial_duration_time=trial_duration_time,
            )
            response = self._api.plan_new_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def edit(
        self,
        plan_id: int,
        plan_name: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ) -> Any:
        """
        Edit an existing plan.
        
        Args:
            plan_id: The plan ID
            plan_name: New plan name
            description: New description
            
        Returns:
            Updated plan details
        """
        from openapi_client.models.unibee_api_merchant_plan_edit_req import (
            UnibeeApiMerchantPlanEditReq
        )
        
        try:
            req = UnibeeApiMerchantPlanEditReq(
                plan_id=plan_id,
                plan_name=plan_name,
                description=description,
            )
            response = self._api.plan_edit_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def activate(
        self,
        plan_id: int,
        **kwargs
    ) -> Any:
        """
        Activate a plan.
        
        Args:
            plan_id: The plan ID
            
        Returns:
            Result
        """
        from openapi_client.models.unibee_api_merchant_plan_activate_req import (
            UnibeeApiMerchantPlanActivateReq
        )
        
        try:
            req = UnibeeApiMerchantPlanActivateReq(
                plan_id=plan_id,
            )
            response = self._api.plan_activate_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def publish(
        self,
        plan_id: int,
        **kwargs
    ) -> Any:
        """
        Publish a plan (make visible to users).
        
        Args:
            plan_id: The plan ID
            
        Returns:
            Result
        """
        from openapi_client.models.unibee_api_merchant_plan_publish_req import (
            UnibeeApiMerchantPlanPublishReq
        )
        
        try:
            req = UnibeeApiMerchantPlanPublishReq(
                plan_id=plan_id,
            )
            response = self._api.plan_publish_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def unpublish(
        self,
        plan_id: int,
        **kwargs
    ) -> Any:
        """
        Unpublish a plan (hide from users).
        
        Args:
            plan_id: The plan ID
            
        Returns:
            Result
        """
        from openapi_client.models.unibee_api_merchant_plan_un_publish_req import (
            UnibeeApiMerchantPlanUnPublishReq
        )
        
        try:
            req = UnibeeApiMerchantPlanUnPublishReq(
                plan_id=plan_id,
            )
            response = self._api.plan_unpublished_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def delete(
        self,
        plan_id: int,
        **kwargs
    ) -> Any:
        """
        Delete a plan (only before activation).
        
        Args:
            plan_id: The plan ID
            
        Returns:
            Result
        """
        from openapi_client.models.unibee_api_merchant_plan_delete_req import (
            UnibeeApiMerchantPlanDeleteReq
        )
        
        try:
            req = UnibeeApiMerchantPlanDeleteReq(
                plan_id=plan_id,
            )
            response = self._api.plan_delete_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def bind_addons(
        self,
        plan_id: int,
        addon_ids: List[int],
        **kwargs
    ) -> Any:
        """
        Bind addon plans to a main plan.
        
        Args:
            plan_id: The main plan ID
            addon_ids: List of addon plan IDs
            
        Returns:
            Result
        """
        from openapi_client.models.unibee_api_merchant_plan_addons_binding_req import (
            UnibeeApiMerchantPlanAddonsBindingReq
        )
        
        try:
            req = UnibeeApiMerchantPlanAddonsBindingReq(
                plan_id=plan_id,
                addon_ids=addon_ids,
            )
            response = self._api.plan_addons_binding_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
