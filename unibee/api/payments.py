# coding: utf-8
"""
UniBee Payments API

Manage payments and payment methods.
"""

from typing import Any, Dict, List, Optional

from unibee.api.base import BaseAPI


class PaymentsAPI(BaseAPI):
    """
    API for managing payments and payment methods.
    
    Example:
        ```python
        from unibee import UniBeeClient
        
        client = UniBeeClient(api_key="your-api-key")
        
        # Get payment details
        payment = client.payments.get(payment_id="pay_123")
        
        # List payments
        payments = client.payments.list(user_id=123)
        
        # Create a new payment
        result = client.payments.create(
            user_id=123,
            amount=1000,
            currency="USD",
        )
        ```
    """
    
    def list(
        self,
        user_id: Optional[int] = None,
        status: Optional[List[int]] = None,
        gateway_id: Optional[int] = None,
        currency: Optional[str] = None,
        amount_start: Optional[int] = None,
        amount_end: Optional[int] = None,
        page: int = 0,
        count: int = 20,
        sort_field: Optional[str] = None,
        sort_type: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        List payments with optional filters.
        
        Args:
            user_id: Filter by user ID.
            status: Filter by payment status(es).
                    Status: 0=Pending, 1=Success, 2=Failed, 3=Cancelled
            gateway_id: Filter by gateway ID.
            currency: Filter by currency code.
            amount_start: Filter by minimum amount.
            amount_end: Filter by maximum amount.
            page: Page number (0-indexed).
            count: Number of results per page.
            sort_field: Field to sort by.
            sort_type: Sort direction ('asc' or 'desc').
            **kwargs: Additional filter parameters.
        
        Returns:
            Dictionary containing 'paymentList' and pagination info.
        """
        data = {
            "userId": user_id,
            "status": status,
            "gatewayId": gateway_id,
            "currency": currency,
            "amountStart": amount_start,
            "amountEnd": amount_end,
            "page": page,
            "count": count,
            "sortField": sort_field,
            "sortType": sort_type,
            **kwargs,
        }
        return self._get("/merchant/payment/list", params=data)
    
    def get(
        self,
        payment_id: str,
    ) -> Dict[str, Any]:
        """
        Get payment details by ID.
        
        Args:
            payment_id: The payment ID.
        
        Returns:
            Payment details.
        """
        return self._get(
            "/merchant/payment/detail",
            params={"paymentId": payment_id},
        )
    
    def create(
        self,
        user_id: int,
        amount: int,
        currency: str,
        gateway_id: int,
        external_payment_id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        return_url: Optional[str] = None,
        cancel_url: Optional[str] = None,
        items: Optional[List[Dict[str, Any]]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create a new payment.
        
        Args:
            user_id: The user ID.
            amount: Payment amount in smallest currency unit.
            currency: Currency code (e.g., "USD").
            gateway_id: Payment gateway ID.
            external_payment_id: External reference ID.
            name: Payment name/title.
            description: Payment description.
            return_url: URL to redirect after payment.
            cancel_url: URL to redirect if payment cancelled.
            items: List of payment items.
            metadata: Additional metadata.
            **kwargs: Additional parameters.
        
        Returns:
            Created payment details with payment link.
        """
        data = {
            "userId": user_id,
            "totalAmount": amount,
            "currency": currency,
            "gatewayId": gateway_id,
            "externalPaymentId": external_payment_id,
            "name": name,
            "description": description,
            "returnUrl": return_url,
            "cancelUrl": cancel_url,
            "items": items,
            "metadata": metadata,
            **kwargs,
        }
        return self._post("/merchant/payment/new", data=data)
    
    def cancel(
        self,
        payment_id: str,
    ) -> Dict[str, Any]:
        """
        Cancel a pending payment.
        
        Args:
            payment_id: The payment ID.
        
        Returns:
            Cancelled payment details.
        """
        return self._post(
            "/merchant/payment/cancel",
            data={"paymentId": payment_id},
        )
    
    def capture(
        self,
        payment_id: str,
        amount: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Capture an authorized payment.
        
        Args:
            payment_id: The payment ID.
            amount: Amount to capture (optional, captures full amount if not specified).
        
        Returns:
            Captured payment details.
        """
        data = {"paymentId": payment_id}
        if amount is not None:
            data["amount"] = amount
        return self._post("/merchant/payment/capture", data=data)
    
    def get_timeline(
        self,
        payment_id: str,
        page: int = 0,
        count: int = 20,
    ) -> Dict[str, Any]:
        """
        Get payment timeline/history.
        
        Args:
            payment_id: The payment ID.
            page: Page number (0-indexed).
            count: Number of results per page.
        
        Returns:
            List of timeline events.
        """
        return self._get(
            "/merchant/payment/timeline/list",
            params={
                "paymentId": payment_id,
                "page": page,
                "count": count,
            },
        )
    
    def list_methods(
        self,
        user_id: int,
        gateway_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        List payment methods for a user.
        
        Args:
            user_id: The user ID.
            gateway_id: Filter by gateway ID.
        
        Returns:
            List of payment methods.
        """
        return self._get(
            "/merchant/payment/method_list",
            params={
                "userId": user_id,
                "gatewayId": gateway_id,
            },
        )
    
    def create_method(
        self,
        user_id: int,
        gateway_id: int,
        return_url: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create/setup a new payment method for a user.
        
        Args:
            user_id: The user ID.
            gateway_id: Payment gateway ID.
            return_url: URL to redirect after setup.
            **kwargs: Additional parameters.
        
        Returns:
            Setup link for adding payment method.
        """
        data = {
            "userId": user_id,
            "gatewayId": gateway_id,
            "returnUrl": return_url,
            **kwargs,
        }
        return self._post("/merchant/payment/method_new", data=data)
    
    def delete_method(
        self,
        user_id: int,
        payment_method_id: str,
    ) -> Dict[str, Any]:
        """
        Delete a payment method.
        
        Args:
            user_id: The user ID.
            payment_method_id: The payment method ID to delete.
        
        Returns:
            Deletion confirmation.
        """
        return self._post(
            "/merchant/payment/method_delete",
            data={
                "userId": user_id,
                "paymentMethodId": payment_method_id,
            },
        )
    
    # Refund methods
    def list_refunds(
        self,
        payment_id: Optional[str] = None,
        user_id: Optional[int] = None,
        status: Optional[List[int]] = None,
        page: int = 0,
        count: int = 20,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        List payment refunds.
        
        Args:
            payment_id: Filter by payment ID.
            user_id: Filter by user ID.
            status: Filter by refund status.
            page: Page number (0-indexed).
            count: Number of results per page.
            **kwargs: Additional filter parameters.
        
        Returns:
            List of refunds.
        """
        return self._get(
            "/merchant/payment/refund/list",
            params={
                "paymentId": payment_id,
                "userId": user_id,
                "status": status,
                "page": page,
                "count": count,
                **kwargs,
            },
        )
    
    def get_refund(
        self,
        refund_id: str,
    ) -> Dict[str, Any]:
        """
        Get refund details.
        
        Args:
            refund_id: The refund ID.
        
        Returns:
            Refund details.
        """
        return self._get(
            "/merchant/payment/refund/detail",
            params={"refundId": refund_id},
        )
    
    def create_refund(
        self,
        payment_id: str,
        refund_amount: int,
        reason: Optional[str] = None,
        external_refund_id: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create a refund for a payment.
        
        Args:
            payment_id: The payment ID to refund.
            refund_amount: Amount to refund (in smallest currency unit).
            reason: Reason for the refund.
            external_refund_id: External reference ID.
            **kwargs: Additional parameters.
        
        Returns:
            Created refund details.
        """
        data = {
            "paymentId": payment_id,
            "refundAmount": refund_amount,
            "reason": reason,
            "externalRefundId": external_refund_id,
            **kwargs,
        }
        return self._post("/merchant/payment/refund/new", data=data)
    
    def cancel_refund(
        self,
        refund_id: str,
    ) -> Dict[str, Any]:
        """
        Cancel a pending refund.
        
        Args:
            refund_id: The refund ID.
        
        Returns:
            Cancelled refund details.
        """
        return self._post(
            "/merchant/payment/refund/cancel",
            data={"refundId": refund_id},
        )
