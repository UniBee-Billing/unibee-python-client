# coding: utf-8
"""
UniBee Discounts API

Manage discount codes and promotions.
"""

from typing import Any, Dict, List, Optional

from unibee.api.base import BaseAPI


class DiscountsAPI(BaseAPI):
    """
    API for managing discount codes.
    
    Example:
        ```python
        from unibee import UniBeeClient
        
        client = UniBeeClient(api_key="your-api-key")
        
        # List discount codes
        discounts = client.discounts.list()
        
        # Create a new discount code
        discount = client.discounts.create(
            code="SUMMER20",
            name="Summer Sale",
            discount_type=1,  # Percentage
            discount_amount=20,  # 20%
        )
        ```
    """
    
    def list(
        self,
        status: Optional[List[int]] = None,
        discount_type: Optional[int] = None,
        currency: Optional[str] = None,
        page: int = 0,
        count: int = 20,
        sort_field: Optional[str] = None,
        sort_type: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        List discount codes.
        
        Args:
            status: Filter by status.
                    Status: 1=Editing, 2=Active, 3=Deactivated, 4=Expired
            discount_type: Filter by type.
                          Type: 1=Percentage, 2=Fixed Amount
            currency: Filter by currency (for fixed amount discounts).
            page: Page number (0-indexed).
            count: Number of results per page.
            sort_field: Field to sort by.
            sort_type: Sort direction ('asc' or 'desc').
            **kwargs: Additional filter parameters.
        
        Returns:
            List of discount codes.
        """
        return self._get(
            "/merchant/discount/list",
            params={
                "status": status,
                "discountType": discount_type,
                "currency": currency,
                "page": page,
                "count": count,
                "sortField": sort_field,
                "sortType": sort_type,
                **kwargs,
            },
        )
    
    def get(
        self,
        discount_id: Optional[int] = None,
        code: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Get discount code details.
        
        Args:
            discount_id: The discount ID.
            code: The discount code string.
        
        Returns:
            Discount code details.
        """
        return self._get(
            "/merchant/discount/detail",
            params={
                "id": discount_id,
                "code": code,
            },
        )
    
    def create(
        self,
        code: str,
        name: str,
        discount_type: int,
        discount_amount: int,
        currency: Optional[str] = None,
        billing_type: int = 1,
        cycle_limit: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        quantity: Optional[int] = None,
        plan_ids: Optional[List[int]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create a new discount code.
        
        Args:
            code: Discount code string (e.g., "SUMMER20").
            name: Display name for the discount.
            discount_type: Discount type. 1=Percentage, 2=Fixed Amount.
            discount_amount: Discount amount.
                            For percentage: 20 = 20%
                            For fixed: amount in smallest currency unit
            currency: Currency code (required for fixed amount discounts).
            billing_type: Billing type. 1=OneTime, 2=Recurring.
            cycle_limit: Number of billing cycles discount applies to.
            start_time: Unix timestamp when discount becomes active.
            end_time: Unix timestamp when discount expires.
            quantity: Maximum number of times discount can be used.
            plan_ids: List of plan IDs discount applies to (empty = all plans).
            metadata: Additional metadata.
            **kwargs: Additional parameters.
        
        Returns:
            Created discount code details.
        """
        data = {
            "code": code,
            "name": name,
            "discountType": discount_type,
            "discountAmount": discount_amount,
            "currency": currency,
            "billingType": billing_type,
            "cycleLimit": cycle_limit,
            "startTime": start_time,
            "endTime": end_time,
            "quantity": quantity,
            "planIds": plan_ids,
            "metadata": metadata,
            **kwargs,
        }
        return self._post("/merchant/discount/new", data=data)
    
    def edit(
        self,
        discount_id: int,
        name: Optional[str] = None,
        cycle_limit: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        quantity: Optional[int] = None,
        plan_ids: Optional[List[int]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Edit an existing discount code.
        
        Note: discount_type and discount_amount cannot be changed.
        
        Args:
            discount_id: The discount ID to edit.
            name: New display name.
            cycle_limit: New cycle limit.
            start_time: New start time.
            end_time: New end time.
            quantity: New quantity limit.
            plan_ids: New list of plan IDs.
            metadata: New metadata.
            **kwargs: Additional parameters.
        
        Returns:
            Updated discount code details.
        """
        data = {
            "id": discount_id,
            "name": name,
            "cycleLimit": cycle_limit,
            "startTime": start_time,
            "endTime": end_time,
            "quantity": quantity,
            "planIds": plan_ids,
            "metadata": metadata,
            **kwargs,
        }
        return self._post("/merchant/discount/edit", data=data)
    
    def delete(
        self,
        discount_id: int,
    ) -> Dict[str, Any]:
        """
        Delete a discount code.
        
        Args:
            discount_id: The discount ID to delete.
        
        Returns:
            Deletion confirmation.
        """
        return self._post(
            "/merchant/discount/delete",
            data={"id": discount_id},
        )
    
    def activate(
        self,
        discount_id: int,
    ) -> Dict[str, Any]:
        """
        Activate a discount code.
        
        Args:
            discount_id: The discount ID to activate.
        
        Returns:
            Activated discount code details.
        """
        return self._post(
            "/merchant/discount/activate",
            data={"id": discount_id},
        )
    
    def deactivate(
        self,
        discount_id: int,
    ) -> Dict[str, Any]:
        """
        Deactivate a discount code.
        
        Args:
            discount_id: The discount ID to deactivate.
        
        Returns:
            Deactivated discount code details.
        """
        return self._post(
            "/merchant/discount/deactivate",
            data={"id": discount_id},
        )
    
    def increment_quantity(
        self,
        discount_id: int,
        amount: int,
    ) -> Dict[str, Any]:
        """
        Increment the available quantity of a discount.
        
        Args:
            discount_id: The discount ID.
            amount: Amount to add to quantity.
        
        Returns:
            Updated discount code details.
        """
        return self._post(
            "/merchant/discount/quantity_increment",
            data={
                "id": discount_id,
                "amount": amount,
            },
        )
    
    def decrement_quantity(
        self,
        discount_id: int,
        amount: int,
    ) -> Dict[str, Any]:
        """
        Decrement the available quantity of a discount.
        
        Args:
            discount_id: The discount ID.
            amount: Amount to subtract from quantity.
        
        Returns:
            Updated discount code details.
        """
        return self._post(
            "/merchant/discount/quantity_decrement",
            data={
                "id": discount_id,
                "amount": amount,
            },
        )
    
    def preview_apply(
        self,
        code: str,
        plan_id: int,
        user_id: Optional[int] = None,
        email: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Preview applying a discount code to a plan.
        
        Args:
            code: Discount code string.
            plan_id: Plan ID to apply discount to.
            user_id: User ID (optional).
            email: User email (optional).
        
        Returns:
            Preview of discounted price.
        """
        return self._post(
            "/merchant/discount/plan_apply_preview",
            data={
                "code": code,
                "planId": plan_id,
                "userId": user_id,
                "email": email,
            },
        )
