# coding: utf-8
"""
UniBee Invoices API

Manage invoices and billing.
"""

from typing import Any, Dict, List, Optional

from unibee.api.base import BaseAPI


class InvoicesAPI(BaseAPI):
    """
    API for managing invoices.
    
    Invoices represent billing documents generated for subscriptions
    and one-time payments.
    
    Example:
        ```python
        from unibee import UniBeeClient
        
        client = UniBeeClient(api_key="your-api-key")
        
        # Get invoice details
        invoice = client.invoices.get(invoice_id="inv_123")
        
        # List invoices for a user
        invoices = client.invoices.list(user_id=123)
        
        # Send invoice email
        client.invoices.send_email(invoice_id="inv_123")
        ```
    """
    
    def list(
        self,
        user_id: Optional[int] = None,
        status: Optional[List[int]] = None,
        subscription_id: Optional[str] = None,
        currency: Optional[str] = None,
        amount_start: Optional[int] = None,
        amount_end: Optional[int] = None,
        send_status: Optional[int] = None,
        page: int = 0,
        count: int = 20,
        sort_field: Optional[str] = None,
        sort_type: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        List invoices with optional filters.
        
        Args:
            user_id: Filter by user ID.
            status: Filter by invoice status(es).
                    Status: 0=Init, 1=Pending, 2=Processing, 3=Paid, 4=Failed,
                    5=Cancelled, 6=Reversed
            subscription_id: Filter by subscription ID.
            currency: Filter by currency code.
            amount_start: Filter by minimum amount.
            amount_end: Filter by maximum amount.
            send_status: Filter by email send status.
            page: Page number (0-indexed).
            count: Number of results per page.
            sort_field: Field to sort by.
            sort_type: Sort direction ('asc' or 'desc').
            **kwargs: Additional filter parameters.
        
        Returns:
            Dictionary containing 'invoices' list and pagination info.
        """
        data = {
            "userId": user_id,
            "status": status,
            "subscriptionId": subscription_id,
            "currency": currency,
            "amountStart": amount_start,
            "amountEnd": amount_end,
            "sendStatus": send_status,
            "page": page,
            "count": count,
            "sortField": sort_field,
            "sortType": sort_type,
            **kwargs,
        }
        return self._post("/merchant/invoice/list", data=data)
    
    def get(
        self,
        invoice_id: str,
    ) -> Dict[str, Any]:
        """
        Get invoice details by ID.
        
        Args:
            invoice_id: The invoice ID.
        
        Returns:
            Invoice details including items, amounts, and payment info.
        """
        return self._post(
            "/merchant/invoice/detail",
            data={"invoiceId": invoice_id},
        )
    
    def create(
        self,
        user_id: int,
        currency: str,
        lines: List[Dict[str, Any]],
        name: Optional[str] = None,
        gateway_id: Optional[int] = None,
        tax_percentage: Optional[float] = None,
        discount_code: Optional[str] = None,
        send_invoice: bool = False,
        finish: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create a new invoice.
        
        Args:
            user_id: The user ID for the invoice.
            currency: Currency code (e.g., "USD").
            lines: List of invoice line items. Each item should have:
                   {"description": "...", "amount": 1000, "quantity": 1}
            name: Invoice name/title.
            gateway_id: Payment gateway ID.
            tax_percentage: Tax percentage to apply.
            discount_code: Discount code to apply.
            send_invoice: Whether to send invoice email.
            finish: Whether to finalize the invoice immediately.
            **kwargs: Additional parameters.
        
        Returns:
            Created invoice details.
        """
        data = {
            "userId": user_id,
            "currency": currency,
            "lines": lines,
            "name": name,
            "gatewayId": gateway_id,
            "taxPercentage": tax_percentage,
            "discountCode": discount_code,
            "sendInvoice": send_invoice,
            "finish": finish,
            **kwargs,
        }
        return self._post("/merchant/invoice/new", data=data)
    
    def edit(
        self,
        invoice_id: str,
        lines: Optional[List[Dict[str, Any]]] = None,
        name: Optional[str] = None,
        tax_percentage: Optional[float] = None,
        discount_code: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Edit a pending invoice.
        
        Only invoices in pending status can be edited.
        
        Args:
            invoice_id: The invoice ID to edit.
            lines: New list of invoice line items.
            name: New invoice name/title.
            tax_percentage: New tax percentage.
            discount_code: New discount code.
            **kwargs: Additional parameters.
        
        Returns:
            Updated invoice details.
        """
        data = {
            "invoiceId": invoice_id,
            "lines": lines,
            "name": name,
            "taxPercentage": tax_percentage,
            "discountCode": discount_code,
            **kwargs,
        }
        return self._post("/merchant/invoice/edit", data=data)
    
    def delete(
        self,
        invoice_id: str,
    ) -> Dict[str, Any]:
        """
        Delete a pending invoice.
        
        Only invoices in pending status can be deleted.
        
        Args:
            invoice_id: The invoice ID to delete.
        
        Returns:
            Deletion confirmation.
        """
        return self._post(
            "/merchant/invoice/delete",
            data={"invoiceId": invoice_id},
        )
    
    def cancel(
        self,
        invoice_id: str,
    ) -> Dict[str, Any]:
        """
        Cancel a processing invoice.
        
        Args:
            invoice_id: The invoice ID to cancel.
        
        Returns:
            Cancelled invoice details.
        """
        return self._post(
            "/merchant/invoice/cancel",
            data={"invoiceId": invoice_id},
        )
    
    def finish(
        self,
        invoice_id: str,
    ) -> Dict[str, Any]:
        """
        Finish/finalize an invoice and generate payment link.
        
        Args:
            invoice_id: The invoice ID to finish.
        
        Returns:
            Finalized invoice details with payment link.
        """
        return self._post(
            "/merchant/invoice/finish",
            data={"invoiceId": invoice_id},
        )
    
    def refund(
        self,
        invoice_id: str,
        refund_amount: int,
        reason: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Create a refund for a paid invoice.
        
        Args:
            invoice_id: The invoice ID to refund.
            refund_amount: Amount to refund (in smallest currency unit).
            reason: Reason for the refund.
        
        Returns:
            Refund details.
        """
        return self._post(
            "/merchant/invoice/refund",
            data={
                "invoiceId": invoice_id,
                "refundAmount": refund_amount,
                "reason": reason,
            },
        )
    
    def mark_refund(
        self,
        invoice_id: str,
        refund_amount: int,
        reason: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Mark an invoice as refunded (offline refund).
        
        Args:
            invoice_id: The invoice ID.
            refund_amount: Amount refunded (in smallest currency unit).
            reason: Reason for the refund.
        
        Returns:
            Updated invoice details.
        """
        return self._post(
            "/merchant/invoice/mark_refund",
            data={
                "invoiceId": invoice_id,
                "refundAmount": refund_amount,
                "reason": reason,
            },
        )
    
    def send_email(
        self,
        invoice_id: str,
    ) -> Dict[str, Any]:
        """
        Send invoice email to the user.
        
        Args:
            invoice_id: The invoice ID.
        
        Returns:
            Email send confirmation.
        """
        return self._post(
            "/merchant/invoice/send_email",
            data={"invoiceId": invoice_id},
        )
    
    def generate_pdf(
        self,
        invoice_id: str,
    ) -> Dict[str, Any]:
        """
        Generate PDF for an invoice.
        
        Args:
            invoice_id: The invoice ID.
        
        Returns:
            PDF generation result with URL.
        """
        return self._post(
            "/merchant/invoice/pdf_generate",
            data={"invoiceId": invoice_id},
        )
    
    def mark_wire_transfer_success(
        self,
        invoice_id: str,
        transfer_number: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Mark a wire transfer invoice as successfully paid.
        
        Args:
            invoice_id: The invoice ID.
            transfer_number: Wire transfer reference number.
        
        Returns:
            Updated invoice details.
        """
        return self._post(
            "/merchant/invoice/mark_wire_transfer_success",
            data={
                "invoiceId": invoice_id,
                "transferNumber": transfer_number,
            },
        )
