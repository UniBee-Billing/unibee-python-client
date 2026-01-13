# coding: utf-8
"""
Discount Resource

Provides methods for managing discount codes.
"""

from typing import Any, Dict, List, Optional

from openapi_client import ApiClient
from openapi_client.rest import ApiException

from unibee.resources.base import BaseResource


class DiscountResource(BaseResource):
    """Discount code management."""
    
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)
        # Discount API may be in a different module
        try:
            from openapi_client.api.discount import Discount as DiscountApi
            self._api = DiscountApi(api_client)
            self._available = True
        except ImportError:
            self._api = None
            self._available = False
    
    def list(self, page: int = 0, count: int = 20, **kwargs) -> Any:
        """List discount codes."""
        if not self._available:
            raise NotImplementedError("Discount API not available in current SDK version")
        try:
            response = self._api.discount_list_get(page=page, count=count)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def get(self, code: str, **kwargs) -> Any:
        """Get discount code details."""
        if not self._available:
            raise NotImplementedError("Discount API not available in current SDK version")
        try:
            response = self._api.discount_detail_get(code=code)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
