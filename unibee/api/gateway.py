# coding: utf-8
"""
UniBee Gateways API

Manage payment gateways.
"""

from typing import Any, Dict, List, Optional

from unibee.api.base import BaseAPI


class GatewaysAPI(BaseAPI):
    """
    API for managing payment gateways.
    
    Example:
        ```python
        from unibee import UniBeeClient
        
        client = UniBeeClient(api_key="your-api-key")
        
        # List payment gateways
        gateways = client.gateways.list()
        
        # Setup a new gateway
        gateway = client.gateways.setup(
            gateway_type="stripe",
            gateway_key="sk_live_xxx",
        )
        ```
    """
    
    def list(self) -> Dict[str, Any]:
        """
        List all configured payment gateways.
        
        Returns:
            List of payment gateways.
        """
        return self._get("/merchant/gateway/list")
    
    def get(
        self,
        gateway_id: int,
    ) -> Dict[str, Any]:
        """
        Get payment gateway details.
        
        Args:
            gateway_id: The gateway ID.
        
        Returns:
            Gateway details.
        """
        return self._post(
            "/merchant/gateway/detail",
            data={"gatewayId": gateway_id},
        )
    
    def setup(
        self,
        gateway_type: str,
        gateway_key: str,
        gateway_secret: Optional[str] = None,
        gateway_name: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Setup a new payment gateway.
        
        Args:
            gateway_type: Gateway type (e.g., "stripe", "paypal").
            gateway_key: Gateway API key or public key.
            gateway_secret: Gateway secret key (if required).
            gateway_name: Custom name for the gateway.
            **kwargs: Additional gateway-specific parameters.
        
        Returns:
            Created gateway details.
        """
        data = {
            "gatewayType": gateway_type,
            "gatewayKey": gateway_key,
            "gatewaySecret": gateway_secret,
            "gatewayName": gateway_name,
            **kwargs,
        }
        return self._post("/merchant/gateway/setup", data=data)
    
    def edit(
        self,
        gateway_id: int,
        gateway_name: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Edit gateway settings.
        
        Args:
            gateway_id: The gateway ID to edit.
            gateway_name: New gateway name.
            **kwargs: Additional parameters.
        
        Returns:
            Updated gateway details.
        """
        data = {
            "gatewayId": gateway_id,
            "gatewayName": gateway_name,
            **kwargs,
        }
        return self._post("/merchant/gateway/edit", data=data)
    
    def archive(
        self,
        gateway_id: int,
    ) -> Dict[str, Any]:
        """
        Archive a payment gateway.
        
        Args:
            gateway_id: The gateway ID to archive.
        
        Returns:
            Archived gateway details.
        """
        return self._post(
            "/merchant/gateway/archive",
            data={"gatewayId": gateway_id},
        )
    
    def restore(
        self,
        gateway_id: int,
    ) -> Dict[str, Any]:
        """
        Restore an archived payment gateway.
        
        Args:
            gateway_id: The gateway ID to restore.
        
        Returns:
            Restored gateway details.
        """
        return self._post(
            "/merchant/gateway/restore",
            data={"gatewayId": gateway_id},
        )
    
    def set_default(
        self,
        gateway_id: int,
    ) -> Dict[str, Any]:
        """
        Set a gateway as the default.
        
        Args:
            gateway_id: The gateway ID to set as default.
        
        Returns:
            Updated gateway details.
        """
        return self._post(
            "/merchant/gateway/set_default",
            data={"gatewayId": gateway_id},
        )
    
    def setup_webhook(
        self,
        gateway_id: int,
    ) -> Dict[str, Any]:
        """
        Setup webhook for a payment gateway.
        
        This registers the webhook endpoint with the payment gateway.
        
        Args:
            gateway_id: The gateway ID.
        
        Returns:
            Webhook setup result.
        """
        return self._post(
            "/merchant/gateway/setup_webhook",
            data={"gatewayId": gateway_id},
        )
    
    def edit_country_config(
        self,
        gateway_id: int,
        country_config: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        Edit country-specific gateway configuration.
        
        Args:
            gateway_id: The gateway ID.
            country_config: List of country configurations.
        
        Returns:
            Updated gateway details.
        """
        return self._post(
            "/merchant/gateway/edit_country_config",
            data={
                "gatewayId": gateway_id,
                "countryConfig": country_config,
            },
        )
    
    def edit_sort(
        self,
        gateway_ids: List[int],
    ) -> Dict[str, Any]:
        """
        Edit the sort order of gateways.
        
        Args:
            gateway_ids: List of gateway IDs in desired order.
        
        Returns:
            Update confirmation.
        """
        return self._post(
            "/merchant/gateway/edit_sort",
            data={"gatewayIds": gateway_ids},
        )
    
    def get_setup_list(self) -> Dict[str, Any]:
        """
        Get list of available gateway types for setup.
        
        Returns:
            List of available gateway types.
        """
        return self._get("/merchant/gateway/setup_list")
