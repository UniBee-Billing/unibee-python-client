# coding: utf-8
"""
Webhook Resource

Provides methods for managing webhook endpoints in UniBee.
"""

from typing import Any, Dict, List, Optional

from openapi_client import ApiClient
from openapi_client.api.webhook import Webhook as WebhookApi
from openapi_client.rest import ApiException

from unibee.resources.base import BaseResource


class WebhookResource(BaseResource):
    """
    Webhook management resource.
    
    Manage webhook endpoints for receiving real-time event notifications.
    """
    
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)
        self._api = WebhookApi(api_client)
    
    def list_endpoints(
        self,
        **kwargs
    ) -> Any:
        """
        List all webhook endpoints.
        
        Returns:
            List of webhook endpoints
        """
        try:
            response = self._api.webhook_endpoint_list_get()
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def list_events(
        self,
        **kwargs
    ) -> Any:
        """
        List available webhook event types.
        
        Returns:
            List of event types
        """
        try:
            response = self._api.webhook_event_list_get()
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def create_endpoint(
        self,
        url: str,
        events: Optional[List[str]] = None,
        **kwargs
    ) -> Any:
        """
        Create a new webhook endpoint.
        
        Args:
            url: The endpoint URL
            events: List of event types to subscribe to
            
        Returns:
            Created endpoint details
            
        Example:
            >>> endpoint = client.webhook.create_endpoint(
            ...     url="https://example.com/webhooks",
            ...     events=["subscription.created", "payment.completed"]
            ... )
        """
        from openapi_client.models.unibee_api_merchant_webhook_new_endpoint_req import (
            UnibeeApiMerchantWebhookNewEndpointReq
        )
        
        try:
            req = UnibeeApiMerchantWebhookNewEndpointReq(
                url=url,
                events=events,
            )
            response = self._api.webhook_new_endpoint_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def update_endpoint(
        self,
        endpoint_id: int,
        url: Optional[str] = None,
        events: Optional[List[str]] = None,
        **kwargs
    ) -> Any:
        """
        Update a webhook endpoint.
        
        Args:
            endpoint_id: The endpoint ID
            url: New endpoint URL
            events: New list of events to subscribe to
            
        Returns:
            Updated endpoint details
        """
        from openapi_client.models.unibee_api_merchant_webhook_update_endpoint_req import (
            UnibeeApiMerchantWebhookUpdateEndpointReq
        )
        
        try:
            req = UnibeeApiMerchantWebhookUpdateEndpointReq(
                endpoint_id=endpoint_id,
                url=url,
                events=events,
            )
            response = self._api.webhook_update_endpoint_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def delete_endpoint(
        self,
        endpoint_id: int,
        **kwargs
    ) -> Any:
        """
        Delete a webhook endpoint.
        
        Args:
            endpoint_id: The endpoint ID
            
        Returns:
            Result
        """
        from openapi_client.models.unibee_api_merchant_webhook_delete_endpoint_req import (
            UnibeeApiMerchantWebhookDeleteEndpointReq
        )
        
        try:
            req = UnibeeApiMerchantWebhookDeleteEndpointReq(
                endpoint_id=endpoint_id,
            )
            response = self._api.webhook_delete_endpoint_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def list_logs(
        self,
        endpoint_id: int,
        page: int = 0,
        count: int = 20,
        **kwargs
    ) -> Any:
        """
        List webhook delivery logs for an endpoint.
        
        Args:
            endpoint_id: The endpoint ID
            page: Page number
            count: Items per page
            
        Returns:
            List of webhook logs
        """
        try:
            response = self._api.webhook_endpoint_log_list_get(
                endpoint_id=endpoint_id,
                page=page,
                count=count,
            )
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def resend(
        self,
        log_id: int,
        **kwargs
    ) -> Any:
        """
        Resend a failed webhook.
        
        Args:
            log_id: The webhook log ID
            
        Returns:
            Result
        """
        from openapi_client.models.unibee_api_merchant_webhook_resend_webhook_req import (
            UnibeeApiMerchantWebhookResendWebhookReq
        )
        
        try:
            req = UnibeeApiMerchantWebhookResendWebhookReq(
                log_id=log_id,
            )
            response = self._api.webhook_resend_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
