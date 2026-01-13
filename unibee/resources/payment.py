# coding: utf-8
"""
Payment Resource

Provides methods for managing payments in UniBee.
"""

from typing import Any, Dict, List, Optional

from openapi_client import ApiClient
from openapi_client.api.payment import Payment as PaymentApi
from openapi_client.rest import ApiException

from unibee.resources.base import BaseResource


class PaymentResource(BaseResource):
    """
    Payment management resource.
    
    Provides methods for creating, viewing, and managing payments.
    """
    
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)
        self._api = PaymentApi(api_client)
    
    def list(
        self,
        user_id: Optional[int] = None,
        status: Optional[int] = None,
        page: int = 0,
        count: int = 20,
        **kwargs
    ) -> Any:
        """
        List payments with optional filters.
        
        Args:
            user_id: Filter by user ID
            status: Filter by payment status
            page: Page number
            count: Items per page
            
        Returns:
            List of payments
        """
        try:
            response = self._api.payment_list_get(
                user_id=user_id,
                status=status,
                page=page,
                count=count,
            )
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def get(
        self,
        payment_id: str,
        **kwargs
    ) -> Any:
        """
        Get payment details.
        
        Args:
            payment_id: The payment ID
            
        Returns:
            Payment details
        """
        try:
            response = self._api.payment_detail_get(
                payment_id=payment_id,
            )
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def create(
        self,
        user_id: int,
        gateway_id: int,
        currency: str,
        total_amount: int,
        items: Optional[List[Dict]] = None,
        return_url: Optional[str] = None,
        cancel_url: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Any:
        """
        Create a new one-time payment.
        
        Args:
            user_id: The user ID
            gateway_id: Payment gateway ID
            currency: Currency code (e.g., "USD")
            total_amount: Total amount in cents
            items: Payment line items
            return_url: Success redirect URL
            cancel_url: Cancel redirect URL
            metadata: Additional metadata
            
        Returns:
            Payment details with payment link
            
        Example:
            >>> payment = client.payment.create(
            ...     user_id=123,
            ...     gateway_id=456,
            ...     currency="USD",
            ...     total_amount=9900,
            ...     return_url="https://example.com/success"
            ... )
            >>> print(f"Payment link: {payment.link}")
        """
        from openapi_client.models.unibee_api_merchant_payment_new_req import (
            UnibeeApiMerchantPaymentNewReq
        )
        
        try:
            req = UnibeeApiMerchantPaymentNewReq(
                user_id=user_id,
                gateway_id=gateway_id,
                currency=currency,
                total_amount=total_amount,
                items=items,
                return_url=return_url,
                cancel_url=cancel_url,
                metadata=metadata,
            )
            response = self._api.payment_new_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def cancel(
        self,
        payment_id: str,
        **kwargs
    ) -> Any:
        """
        Cancel a pending payment.
        
        Args:
            payment_id: The payment ID
            
        Returns:
            Result
        """
        from openapi_client.models.unibee_api_merchant_payment_cancel_req import (
            UnibeeApiMerchantPaymentCancelReq
        )
        
        try:
            req = UnibeeApiMerchantPaymentCancelReq(
                payment_id=payment_id,
            )
            response = self._api.payment_cancel_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def capture(
        self,
        payment_id: str,
        **kwargs
    ) -> Any:
        """
        Capture an authorized payment.
        
        Args:
            payment_id: The payment ID
            
        Returns:
            Result
        """
        from openapi_client.models.unibee_api_merchant_payment_capture_req import (
            UnibeeApiMerchantPaymentCaptureReq
        )
        
        try:
            req = UnibeeApiMerchantPaymentCaptureReq(
                payment_id=payment_id,
            )
            response = self._api.payment_capture_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def get_method(
        self,
        user_id: int,
        gateway_id: int,
        payment_method_id: str,
        **kwargs
    ) -> Any:
        """
        Get a specific payment method.
        
        Args:
            user_id: The user ID
            gateway_id: Gateway ID
            payment_method_id: Payment method ID
            
        Returns:
            Payment method details
        """
        try:
            response = self._api.payment_method_get_get(
                user_id=user_id,
                gateway_id=gateway_id,
                payment_method_id=payment_method_id,
            )
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def list_methods(
        self,
        user_id: int,
        gateway_id: Optional[int] = None,
        **kwargs
    ) -> Any:
        """
        List payment methods for a user.
        
        Args:
            user_id: The user ID
            gateway_id: Filter by gateway ID
            
        Returns:
            List of payment methods
        """
        try:
            response = self._api.payment_method_list_get(
                user_id=user_id,
                gateway_id=gateway_id,
            )
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def create_method(
        self,
        user_id: int,
        gateway_id: int,
        currency: str,
        return_url: Optional[str] = None,
        **kwargs
    ) -> Any:
        """
        Create a new payment method for a user.
        
        Args:
            user_id: The user ID
            gateway_id: Gateway ID
            currency: Currency code
            return_url: Return URL after setup
            
        Returns:
            Setup link for payment method
        """
        from openapi_client.models.unibee_api_merchant_payment_method_new_req import (
            UnibeeApiMerchantPaymentMethodNewReq
        )
        
        try:
            req = UnibeeApiMerchantPaymentMethodNewReq(
                user_id=user_id,
                gateway_id=gateway_id,
                currency=currency,
                return_url=return_url,
            )
            response = self._api.payment_method_new_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def create_refund(
        self,
        payment_id: str,
        refund_amount: int,
        currency: str,
        reason: Optional[str] = None,
        **kwargs
    ) -> Any:
        """
        Create a refund for a payment.
        
        Args:
            payment_id: The payment ID
            refund_amount: Amount to refund (in cents)
            currency: Currency code
            reason: Refund reason
            
        Returns:
            Refund details
        """
        from openapi_client.models.unibee_api_merchant_payment_new_payment_refund_req import (
            UnibeeApiMerchantPaymentNewPaymentRefundReq
        )
        
        try:
            req = UnibeeApiMerchantPaymentNewPaymentRefundReq(
                payment_id=payment_id,
                refund_amount=refund_amount,
                currency=currency,
                reason=reason,
            )
            response = self._api.payment_refund_new_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def get_refund(
        self,
        refund_id: str,
        **kwargs
    ) -> Any:
        """
        Get refund details.
        
        Args:
            refund_id: The refund ID
            
        Returns:
            Refund details
        """
        try:
            response = self._api.payment_refund_detail_get(
                refund_id=refund_id,
            )
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def list_refunds(
        self,
        payment_id: Optional[str] = None,
        user_id: Optional[int] = None,
        status: Optional[int] = None,
        page: int = 0,
        count: int = 20,
        **kwargs
    ) -> Any:
        """
        List refunds.
        
        Args:
            payment_id: Filter by payment ID
            user_id: Filter by user ID
            status: Filter by refund status
            page: Page number
            count: Items per page
            
        Returns:
            List of refunds
        """
        try:
            response = self._api.payment_refund_list_get(
                payment_id=payment_id,
                user_id=user_id,
                status=status,
                page=page,
                count=count,
            )
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def list_timeline(
        self,
        user_id: Optional[int] = None,
        page: int = 0,
        count: int = 20,
        **kwargs
    ) -> Any:
        """
        List payment timeline events.
        
        Args:
            user_id: Filter by user ID
            page: Page number
            count: Items per page
            
        Returns:
            Payment timeline
        """
        try:
            response = self._api.payment_timeline_list_get(
                user_id=user_id,
                page=page,
                count=count,
            )
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
