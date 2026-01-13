# coding: utf-8
"""
VAT Resource

Provides methods for managing VAT/tax configuration.
"""

from typing import Any, Dict, List, Optional

from openapi_client import ApiClient
from openapi_client.api.vat import Vat as VatApi
from openapi_client.rest import ApiException

from unibee.resources.base import BaseResource


class VatResource(BaseResource):
    """VAT/tax configuration management."""
    
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)
        self._api = VatApi(api_client)
    
    def list_countries(self, **kwargs) -> Any:
        """List VAT country rates."""
        try:
            response = self._api.vat_country_list_get()
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def setup_gateway(
        self,
        gateway_name: str,
        data: Optional[Dict] = None,
        **kwargs
    ) -> Any:
        """Setup VAT gateway (e.g., TaxJar)."""
        from openapi_client.models.unibee_api_merchant_vat_setup_gateway_req import (
            UnibeeApiMerchantVatSetupGatewayReq
        )
        try:
            req = UnibeeApiMerchantVatSetupGatewayReq(
                gateway_name=gateway_name,
                data=data,
            )
            response = self._api.vat_setup_gateway_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def init_default(self, **kwargs) -> Any:
        """Initialize default VAT gateway."""
        try:
            response = self._api.vat_init_default_gateway_post()
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
