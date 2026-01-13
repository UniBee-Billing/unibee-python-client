# coding: utf-8
"""
Credit Resource

Provides methods for managing promo credits.
"""

from typing import Any, Dict, List, Optional

from openapi_client import ApiClient
from openapi_client.rest import ApiException

from unibee.resources.base import BaseResource


class CreditResource(BaseResource):
    """Promo credit management."""
    
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)
        # Credit API may be in different modules
        try:
            from openapi_client.api.credit import Credit as CreditApi
            self._api = CreditApi(api_client)
            self._available = True
        except ImportError:
            self._api = None
            self._available = False
    
    def get_config(self, **kwargs) -> Any:
        """Get promo credit configuration."""
        if not self._available:
            raise NotImplementedError("Credit API not available in current SDK version")
        try:
            response = self._api.credit_config_get()
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def list_accounts(
        self, 
        page: int = 0, 
        count: int = 20, 
        **kwargs
    ) -> Any:
        """List credit accounts."""
        if not self._available:
            raise NotImplementedError("Credit API not available in current SDK version")
        try:
            response = self._api.credit_account_list_get(page=page, count=count)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def get_account(self, user_id: int, **kwargs) -> Any:
        """Get user's credit account details."""
        if not self._available:
            raise NotImplementedError("Credit API not available in current SDK version")
        try:
            response = self._api.credit_account_detail_get(user_id=user_id)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
