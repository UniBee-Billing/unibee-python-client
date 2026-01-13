# coding: utf-8
"""
UniBee Webhooks API

Manage webhook endpoints for event notifications.
"""

from typing import Any, Dict, List, Optional

from unibee.api.base import BaseAPI


class WebhooksAPI(BaseAPI):
    """
    API for managing webhook endpoints.
    
    Webhooks allow you to receive real-time notifications about
    events in your UniBee account.
    
    Example:
        ```python
        from unibee import UniBeeClient
        
        client = UniBeeClient(api_key="your-api-key")
        
        # List webhook endpoints
        endpoints = client.webhooks.list_endpoints()
        
        # Create a new webhook endpoint
        endpoint = client.webhooks.create_endpoint(
            url="https://your-server.com/webhooks/unibee",
            events=["subscription.created", "invoice.paid"],
        )
        
        # List available events
        events = client.webhooks.list_events()
        ```
    """
    
    def list_endpoints(self) -> Dict[str, Any]:
        """
        List all webhook endpoints.
        
        Returns:
            List of webhook endpoints.
        """
        return self._get("/merchant/webhook/endpoint_list")
    
    def create_endpoint(
        self,
        url: str,
        events: Optional[List[str]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create a new webhook endpoint.
        
        Args:
            url: The URL to receive webhook events.
            events: List of event types to subscribe to.
                   If not specified, subscribes to all events.
            **kwargs: Additional parameters.
        
        Returns:
            Created endpoint details.
        """
        data = {
            "url": url,
            "events": events,
            **kwargs,
        }
        return self._post("/merchant/webhook/new_endpoint", data=data)
    
    def update_endpoint(
        self,
        endpoint_id: int,
        url: Optional[str] = None,
        events: Optional[List[str]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update an existing webhook endpoint.
        
        Args:
            endpoint_id: The endpoint ID to update.
            url: New webhook URL.
            events: New list of event types to subscribe to.
            **kwargs: Additional parameters.
        
        Returns:
            Updated endpoint details.
        """
        data = {
            "endpointId": endpoint_id,
            "url": url,
            "events": events,
            **kwargs,
        }
        return self._post("/merchant/webhook/update_endpoint", data=data)
    
    def delete_endpoint(
        self,
        endpoint_id: int,
    ) -> Dict[str, Any]:
        """
        Delete a webhook endpoint.
        
        Args:
            endpoint_id: The endpoint ID to delete.
        
        Returns:
            Deletion confirmation.
        """
        return self._post(
            "/merchant/webhook/delete_endpoint",
            data={"endpointId": endpoint_id},
        )
    
    def list_events(self) -> Dict[str, Any]:
        """
        List all available webhook event types.
        
        Returns:
            List of event types with descriptions.
        """
        return self._get("/merchant/webhook/event_list")
    
    def list_logs(
        self,
        endpoint_id: int,
        page: int = 0,
        count: int = 20,
    ) -> Dict[str, Any]:
        """
        List webhook delivery logs for an endpoint.
        
        Args:
            endpoint_id: The endpoint ID.
            page: Page number (0-indexed).
            count: Number of results per page.
        
        Returns:
            List of webhook delivery logs.
        """
        return self._get(
            "/merchant/webhook/endpoint_log_list",
            params={
                "endpointId": endpoint_id,
                "page": page,
                "count": count,
            },
        )
    
    def resend(
        self,
        log_id: int,
    ) -> Dict[str, Any]:
        """
        Resend a failed webhook.
        
        Args:
            log_id: The webhook log ID to resend.
        
        Returns:
            Resend result.
        """
        return self._post(
            "/merchant/webhook/resend",
            data={"logId": log_id},
        )
    
    def get_secret(self) -> Dict[str, Any]:
        """
        Get the webhook signing secret.
        
        Use this secret to verify webhook signatures.
        
        Returns:
            Webhook secret.
        """
        return self._get("/merchant/webhook/secret")
