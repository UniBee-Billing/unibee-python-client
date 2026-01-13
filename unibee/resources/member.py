# coding: utf-8
"""
Member Resource

Provides methods for managing merchant members (admin users).
"""

from typing import Any, Dict, List, Optional

from openapi_client import ApiClient
from openapi_client.api.member import Member as MemberApi
from openapi_client.rest import ApiException

from unibee.resources.base import BaseResource


class MemberResource(BaseResource):
    """Merchant member (admin user) management."""
    
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)
        self._api = MemberApi(api_client)
    
    def list(self, **kwargs) -> Any:
        """List all merchant members."""
        try:
            response = self._api.member_list_get()
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def get_profile(self, **kwargs) -> Any:
        """Get current member's profile."""
        try:
            response = self._api.member_profile_get()
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def invite(self, email: str, role: str, **kwargs) -> Any:
        """Invite a new member."""
        from openapi_client.models.unibee_api_merchant_member_new_member_req import (
            UnibeeApiMerchantMemberNewMemberReq
        )
        try:
            req = UnibeeApiMerchantMemberNewMemberReq(email=email, role=role)
            response = self._api.member_new_member_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def reset_password(self, old_password: str, new_password: str, **kwargs) -> Any:
        """Reset member password."""
        from openapi_client.models.unibee_api_merchant_member_password_reset_req import (
            UnibeeApiMerchantMemberPasswordResetReq
        )
        try:
            req = UnibeeApiMerchantMemberPasswordResetReq(
                old_password=old_password, new_password=new_password
            )
            response = self._api.member_password_reset_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def logout(self, **kwargs) -> Any:
        """Logout current member."""
        try:
            response = self._api.member_logout_post()
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
