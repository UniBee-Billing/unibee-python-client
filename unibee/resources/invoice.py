# coding: utf-8
"""
Invoice Resource

Provides methods for managing invoices in UniBee.
"""

from typing import Any, Dict, List, Optional

from openapi_client import ApiClient
from openapi_client.api.invoice import Invoice as InvoiceApi
from openapi_client.rest import ApiException

from unibee.resources.base import BaseResource


class InvoiceResource(BaseResource):
    """
    Invoice management resource.
    
    Provides methods for creating, viewing, and managing invoices.
    
    Example:
        >>> # List invoices
        >>> invoices = client.invoice.list()
        >>> 
        >>> # Get invoice details
        >>> invoice = client.invoice.get(invoice_id="inv_123")
    """
    
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)
        self._api = InvoiceApi(api_client)
    
    def list(
        self,
        user_id: Optional[int] = None,
        status: Optional[List[int]] = None,
        page: int = 0,
        count: int = 20,
        sort_field: Optional[str] = None,
        sort_type: Optional[str] = None,
        **kwargs
    ) -> Any:
        """
        List invoices with optional filters.
        
        Args:
            user_id: Filter by user ID
            status: Filter by invoice status codes
            page: Page number (0-indexed)
            count: Number of items per page
            sort_field: Field to sort by
            sort_type: Sort direction ("asc" or "desc")
            
        Returns:
            List of invoices
        """
        try:
            response = self._api.invoice_list_get(
                user_id=user_id,
                status=status,
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
        invoice_id: str,
        **kwargs
    ) -> Any:
        """
        Get invoice details.
        
        Args:
            invoice_id: The invoice ID
            
        Returns:
            Invoice details
        """
        try:
            response = self._api.invoice_detail_get(
                invoice_id=invoice_id,
            )
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def create(
        self,
        user_id: int,
        currency: str,
        name: Optional[str] = None,
        lines: Optional[List[Dict]] = None,
        gateway_id: Optional[int] = None,
        tax_percentage: Optional[int] = None,
        finish: bool = False,
        **kwargs
    ) -> Any:
        """
        Create a new invoice.
        
        Args:
            user_id: The user ID
            currency: Currency code (e.g., "USD")
            name: Invoice name/description
            lines: Invoice line items
            gateway_id: Payment gateway ID
            tax_percentage: Tax percentage (scaled by 100)
            finish: Whether to finalize the invoice immediately
            
        Returns:
            Created invoice details
            
        Example:
            >>> invoice = client.invoice.create(
            ...     user_id=123,
            ...     currency="USD",
            ...     name="Custom Invoice",
            ...     lines=[
            ...         {"description": "Service Fee", "amount": 5000, "quantity": 1}
            ...     ]
            ... )
        """
        from openapi_client.models.unibee_api_merchant_invoice_new_req import (
            UnibeeApiMerchantInvoiceNewReq
        )
        
        try:
            req = UnibeeApiMerchantInvoiceNewReq(
                user_id=user_id,
                currency=currency,
                name=name,
                lines=lines,
                gateway_id=gateway_id,
                tax_percentage=tax_percentage,
                finish=finish,
            )
            response = self._api.invoice_new_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def edit(
        self,
        invoice_id: str,
        name: Optional[str] = None,
        lines: Optional[List[Dict]] = None,
        tax_percentage: Optional[int] = None,
        **kwargs
    ) -> Any:
        """
        Edit a pending invoice.
        
        Args:
            invoice_id: The invoice ID
            name: Invoice name/description
            lines: Invoice line items
            tax_percentage: Tax percentage
            
        Returns:
            Updated invoice details
        """
        from openapi_client.models.unibee_api_merchant_invoice_edit_req import (
            UnibeeApiMerchantInvoiceEditReq
        )
        
        try:
            req = UnibeeApiMerchantInvoiceEditReq(
                invoice_id=invoice_id,
                name=name,
                lines=lines,
                tax_percentage=tax_percentage,
            )
            response = self._api.invoice_edit_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def finish(
        self,
        invoice_id: str,
        gateway_id: Optional[int] = None,
        **kwargs
    ) -> Any:
        """
        Finalize a pending invoice and generate payment link.
        
        Args:
            invoice_id: The invoice ID
            gateway_id: Payment gateway ID
            
        Returns:
            Finalized invoice with payment link
        """
        from openapi_client.models.unibee_api_merchant_invoice_finish_req import (
            UnibeeApiMerchantInvoiceFinishReq
        )
        
        try:
            req = UnibeeApiMerchantInvoiceFinishReq(
                invoice_id=invoice_id,
                gateway_id=gateway_id,
            )
            response = self._api.invoice_finish_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def cancel(
        self,
        invoice_id: str,
        **kwargs
    ) -> Any:
        """
        Cancel a processing invoice.
        
        Args:
            invoice_id: The invoice ID
            
        Returns:
            Result
        """
        from openapi_client.models.unibee_api_merchant_invoice_cancel_req import (
            UnibeeApiMerchantInvoiceCancelReq
        )
        
        try:
            req = UnibeeApiMerchantInvoiceCancelReq(
                invoice_id=invoice_id,
            )
            response = self._api.invoice_cancel_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def delete(
        self,
        invoice_id: str,
        **kwargs
    ) -> Any:
        """
        Delete a pending invoice.
        
        Args:
            invoice_id: The invoice ID
            
        Returns:
            Result
        """
        from openapi_client.models.unibee_api_merchant_invoice_delete_req import (
            UnibeeApiMerchantInvoiceDeleteReq
        )
        
        try:
            req = UnibeeApiMerchantInvoiceDeleteReq(
                invoice_id=invoice_id,
            )
            response = self._api.invoice_delete_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def refund(
        self,
        invoice_id: str,
        refund_amount: int,
        reason: Optional[str] = None,
        **kwargs
    ) -> Any:
        """
        Create a refund for an invoice.
        
        Args:
            invoice_id: The invoice ID
            refund_amount: Amount to refund (in cents)
            reason: Refund reason
            
        Returns:
            Refund details
        """
        from openapi_client.models.unibee_api_merchant_invoice_refund_req import (
            UnibeeApiMerchantInvoiceRefundReq
        )
        
        try:
            req = UnibeeApiMerchantInvoiceRefundReq(
                invoice_id=invoice_id,
                refund_amount=refund_amount,
                reason=reason,
            )
            response = self._api.invoice_refund_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def send_email(
        self,
        invoice_id: str,
        **kwargs
    ) -> Any:
        """
        Send invoice email to user.
        
        Args:
            invoice_id: The invoice ID
            
        Returns:
            Result
        """
        from openapi_client.models.unibee_api_merchant_invoice_send_email_req import (
            UnibeeApiMerchantInvoiceSendEmailReq
        )
        
        try:
            req = UnibeeApiMerchantInvoiceSendEmailReq(
                invoice_id=invoice_id,
            )
            response = self._api.invoice_send_email_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def generate_pdf(
        self,
        invoice_id: str,
        **kwargs
    ) -> Any:
        """
        Generate PDF for an invoice.
        
        Args:
            invoice_id: The invoice ID
            
        Returns:
            Result with PDF URL
        """
        from openapi_client.models.unibee_api_merchant_invoice_pdf_generate_req import (
            UnibeeApiMerchantInvoicePdfGenerateReq
        )
        
        try:
            req = UnibeeApiMerchantInvoicePdfGenerateReq(
                invoice_id=invoice_id,
            )
            response = self._api.invoice_pdf_generate_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
