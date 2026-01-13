# coding: utf-8
"""
Search Resource

Provides global search functionality.
"""

from typing import Any, Dict, List, Optional

from openapi_client import ApiClient
from openapi_client.api.search import Search as SearchApi
from openapi_client.rest import ApiException

from unibee.resources.base import BaseResource


class SearchResource(BaseResource):
    """Global search functionality."""
    
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)
        self._api = SearchApi(api_client)
    
    def search(self, search_key: str, **kwargs) -> Any:
        """
        Search across all resources.
        
        Args:
            search_key: Search query string
            
        Returns:
            Search results across users, subscriptions, invoices, etc.
        """
        try:
            response = self._api.search_key_search_get(search_key=search_key)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
