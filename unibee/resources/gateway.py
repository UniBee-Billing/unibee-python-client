# coding: utf-8
"""
Gateway Resource

Provides methods for managing payment gateways in UniBee.
"""

from typing import Any, Dict, List, Optional

from openapi_client import ApiClient
from openapi_client.api.gateway import Gateway as GatewayApi
from openapi_client.rest import ApiException

from unibee.resources.base import BaseResource


class GatewayResource(BaseResource):
    """
    Payment gateway management resource.
    
    Manage payment gateways like Stripe, PayPal, etc.
    """
    
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)
        self._api = GatewayApi(api_client)
    
    def list(self, **kwargs) -> Any:
        """
        List all configured payment gateways.
        
        Returns:
            List of gateways
        """
        try:
            response = self._api.gateway_list_get()
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def setup(
        self,
        gateway_name: str,
        gateway_key: str,
        gateway_secret: Optional[str] = None,
        **kwargs
    ) -> Any:
        """
        Setup a new payment gateway.
        
        Args:
            gateway_name: Gateway name (e.g., "stripe", "paypal")
            gateway_key: API key or public key
            gateway_secret: API secret key
            
        Returns:
            Gateway setup result
        """
        from openapi_client.models.unibee_api_merchant_gateway_setup_req import (
            UnibeeApiMerchantGatewaySetupReq
        )
        
        try:
            req = UnibeeApiMerchantGatewaySetupReq(
                gateway_name=gateway_name,
                gateway_key=gateway_key,
                gateway_secret=gateway_secret,
            )
            response = self._api.gateway_setup_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def edit(
        self,
        gateway_id: int,
        gateway_key: Optional[str] = None,
        gateway_secret: Optional[str] = None,
        **kwargs
    ) -> Any:
        """
        Edit gateway configuration.
        
        Args:
            gateway_id: The gateway ID
            gateway_key: New API key
            gateway_secret: New API secret
            
        Returns:
            Result
        """
        from openapi_client.models.unibee_api_merchant_gateway_edit_req import (
            UnibeeApiMerchantGatewayEditReq
        )
        
        try:
            req = UnibeeApiMerchantGatewayEditReq(
                gateway_id=gateway_id,
                gateway_key=gateway_key,
                gateway_secret=gateway_secret,
            )
            response = self._api.gateway_edit_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def setup_webhook(
        self,
        gateway_id: int,
        **kwargs
    ) -> Any:
        """
        Setup webhook for a gateway.
        
        Args:
            gateway_id: The gateway ID
            
        Returns:
            Webhook setup result with endpoint URL
        """
        from openapi_client.models.unibee_api_merchant_gateway_setup_webhook_req import (
            UnibeeApiMerchantGatewaySetupWebhookReq
        )
        
        try:
            req = UnibeeApiMerchantGatewaySetupWebhookReq(
                gateway_id=gateway_id,
            )
            response = self._api.gateway_setup_webhook_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
