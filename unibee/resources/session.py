# coding: utf-8
"""
Session Resource

Provides methods for managing checkout and portal sessions.
"""

from typing import Any, Dict, List, Optional

from openapi_client import ApiClient
from openapi_client.api.session import Session as SessionApi
from openapi_client.rest import ApiException

from unibee.resources.base import BaseResource


class SessionResource(BaseResource):
    """Session management (checkout, user portal)."""
    
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)
        self._api = SessionApi(api_client)
    
    def create_portal(
        self,
        user_id: int,
        return_url: Optional[str] = None,
        **kwargs
    ) -> Any:
        """
        Create a new user portal session.
        
        Args:
            user_id: The user ID
            return_url: URL to return after portal session
            
        Returns:
            Session details with portal URL
            
        Example:
            >>> session = client.session.create_portal(
            ...     user_id=123,
            ...     return_url="https://example.com/account"
            ... )
            >>> print(f"Portal URL: {session.url}")
        """
        from openapi_client.models.unibee_api_merchant_session_new_req import (
            UnibeeApiMerchantSessionNewReq
        )
        
        try:
            req = UnibeeApiMerchantSessionNewReq(
                user_id=user_id,
                return_url=return_url,
            )
            response = self._api.session_new_session_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
