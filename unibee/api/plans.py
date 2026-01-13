# coding: utf-8
"""
UniBee Plans API

Manage subscription plans and pricing.
"""

from typing import Any, Dict, List, Optional

from unibee.api.base import BaseAPI


class PlansAPI(BaseAPI):
    """
    API for managing subscription plans.
    
    Plans define the pricing and billing cycle for subscriptions.
    
    Example:
        ```python
        from unibee import UniBeeClient
        
        client = UniBeeClient(api_key="your-api-key")
        
        # List all plans
        plans = client.plans.list()
        
        # Get plan details
        plan = client.plans.get(plan_id=123)
        
        # Create a new plan
        plan = client.plans.create(
            plan_name="Basic Plan",
            amount=999,  # $9.99
            currency="USD",
            interval_unit="month",
            interval_count=1,
        )
        ```
    """
    
    def list(
        self,
        product_id: Optional[int] = None,
        status: Optional[List[int]] = None,
        plan_type: Optional[List[int]] = None,
        currency: Optional[str] = None,
        published_status: Optional[int] = None,
        page: int = 0,
        count: int = 20,
        sort_field: Optional[str] = None,
        sort_type: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        List plans with optional filters.
        
        Args:
            product_id: Filter by product ID.
            status: Filter by status. 1=Editing, 2=Active, 3=Inactive, 4=Expired
            plan_type: Filter by type. 1=Main plan, 2=Addon, 3=One-time
            currency: Filter by currency code.
            published_status: Filter by publish status.
            page: Page number (0-indexed).
            count: Number of results per page.
            sort_field: Field to sort by.
            sort_type: Sort direction ('asc' or 'desc').
            **kwargs: Additional filter parameters.
        
        Returns:
            Dictionary containing 'plans' list and pagination info.
        """
        data = {
            "productId": product_id,
            "status": status,
            "type": plan_type,
            "currency": currency,
            "publishStatus": published_status,
            "page": page,
            "count": count,
            "sortField": sort_field,
            "sortType": sort_type,
            **kwargs,
        }
        return self._post("/merchant/plan/list", data=data)
    
    def get(
        self,
        plan_id: int,
    ) -> Dict[str, Any]:
        """
        Get plan details by ID.
        
        Args:
            plan_id: The plan ID.
        
        Returns:
            Plan details including pricing and configuration.
        """
        return self._post(
            "/merchant/plan/detail",
            data={"planId": plan_id},
        )
    
    def create(
        self,
        plan_name: str,
        amount: int,
        currency: str,
        interval_unit: str,
        interval_count: int = 1,
        product_id: Optional[int] = None,
        description: Optional[str] = None,
        plan_type: int = 1,
        external_plan_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        trial_amount: Optional[int] = None,
        trial_duration: Optional[int] = None,
        trial_duration_unit: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create a new plan.
        
        Args:
            plan_name: Name of the plan.
            amount: Price amount in smallest currency unit (e.g., cents).
            currency: Currency code (e.g., "USD", "EUR").
            interval_unit: Billing interval unit: "day", "week", "month", "year".
            interval_count: Number of interval units per billing cycle.
            product_id: ID of the product this plan belongs to.
            description: Plan description.
            plan_type: Plan type. 1=Main plan, 2=Addon, 3=One-time.
            external_plan_id: External reference ID.
            metadata: Additional metadata.
            trial_amount: Trial period amount (0 for free trial).
            trial_duration: Trial duration.
            trial_duration_unit: Trial duration unit.
            **kwargs: Additional parameters.
        
        Returns:
            Created plan details.
        """
        data = {
            "planName": plan_name,
            "amount": amount,
            "currency": currency,
            "intervalUnit": interval_unit,
            "intervalCount": interval_count,
            "productId": product_id,
            "description": description,
            "type": plan_type,
            "externalPlanId": external_plan_id,
            "metadata": metadata,
            "trialAmount": trial_amount,
            "trialDuration": trial_duration,
            "trialDurationUnit": trial_duration_unit,
            **kwargs,
        }
        return self._post("/merchant/plan/new", data=data)
    
    def edit(
        self,
        plan_id: int,
        plan_name: Optional[str] = None,
        description: Optional[str] = None,
        external_plan_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Edit an existing plan.
        
        Note: Pricing cannot be changed for active plans.
        
        Args:
            plan_id: The plan ID to edit.
            plan_name: New plan name.
            description: New description.
            external_plan_id: New external reference ID.
            metadata: New metadata.
            **kwargs: Additional parameters.
        
        Returns:
            Updated plan details.
        """
        data = {
            "planId": plan_id,
            "planName": plan_name,
            "description": description,
            "externalPlanId": external_plan_id,
            "metadata": metadata,
            **kwargs,
        }
        return self._post("/merchant/plan/edit", data=data)
    
    def delete(
        self,
        plan_id: int,
    ) -> Dict[str, Any]:
        """
        Delete a plan.
        
        Only plans that have not been activated can be deleted.
        
        Args:
            plan_id: The plan ID to delete.
        
        Returns:
            Deletion confirmation.
        """
        return self._post(
            "/merchant/plan/delete",
            data={"planId": plan_id},
        )
    
    def activate(
        self,
        plan_id: int,
    ) -> Dict[str, Any]:
        """
        Activate a plan (sync to payment gateway).
        
        Args:
            plan_id: The plan ID to activate.
        
        Returns:
            Activated plan details.
        """
        return self._post(
            "/merchant/plan/activate",
            data={"planId": plan_id},
        )
    
    def publish(
        self,
        plan_id: int,
    ) -> Dict[str, Any]:
        """
        Publish a plan (make visible in user portal).
        
        Args:
            plan_id: The plan ID to publish.
        
        Returns:
            Published plan details.
        """
        return self._post(
            "/merchant/plan/publish",
            data={"planId": plan_id},
        )
    
    def unpublish(
        self,
        plan_id: int,
    ) -> Dict[str, Any]:
        """
        Unpublish a plan (hide from user portal).
        
        Args:
            plan_id: The plan ID to unpublish.
        
        Returns:
            Unpublished plan details.
        """
        return self._post(
            "/merchant/plan/unpublished",
            data={"planId": plan_id},
        )
    
    def archive(
        self,
        plan_id: int,
    ) -> Dict[str, Any]:
        """
        Archive a plan (mark as expired/inactive).
        
        Args:
            plan_id: The plan ID to archive.
        
        Returns:
            Archived plan details.
        """
        return self._post(
            "/merchant/plan/expire",
            data={"planId": plan_id},
        )
    
    def copy(
        self,
        plan_id: int,
    ) -> Dict[str, Any]:
        """
        Copy a plan to create a new one with same settings.
        
        Args:
            plan_id: The plan ID to copy.
        
        Returns:
            New plan details.
        """
        return self._post(
            "/merchant/plan/copy",
            data={"planId": plan_id},
        )
    
    def bind_addons(
        self,
        plan_id: int,
        addon_ids: List[int],
    ) -> Dict[str, Any]:
        """
        Bind addon plans to a main plan.
        
        Args:
            plan_id: The main plan ID.
            addon_ids: List of addon plan IDs to bind.
        
        Returns:
            Updated plan details.
        """
        return self._post(
            "/merchant/plan/addons_binding",
            data={
                "planId": plan_id,
                "addonIds": addon_ids,
            },
        )
