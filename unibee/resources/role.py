# coding: utf-8
"""
Role Resource

Provides methods for managing admin roles.
"""

from typing import Any, Dict, List, Optional

from openapi_client import ApiClient
from openapi_client.api.role import Role as RoleApi
from openapi_client.rest import ApiException

from unibee.resources.base import BaseResource


class RoleResource(BaseResource):
    """Admin role management."""
    
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)
        self._api = RoleApi(api_client)
    
    def list(self, **kwargs) -> Any:
        """List all roles."""
        try:
            response = self._api.role_list_get()
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def create(
        self,
        role: str,
        permissions: Optional[List[str]] = None,
        **kwargs
    ) -> Any:
        """Create a new role."""
        from openapi_client.models.unibee_api_merchant_role_new_req import (
            UnibeeApiMerchantRoleNewReq
        )
        try:
            req = UnibeeApiMerchantRoleNewReq(role=role, permissions=permissions)
            response = self._api.role_new_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def edit(
        self,
        role_id: int,
        role: Optional[str] = None,
        permissions: Optional[List[str]] = None,
        **kwargs
    ) -> Any:
        """Edit a role."""
        from openapi_client.models.unibee_api_merchant_role_edit_req import (
            UnibeeApiMerchantRoleEditReq
        )
        try:
            req = UnibeeApiMerchantRoleEditReq(
                id=role_id, role=role, permissions=permissions
            )
            response = self._api.role_edit_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def delete(self, role_id: int, **kwargs) -> Any:
        """Delete a role."""
        from openapi_client.models.unibee_api_merchant_role_delete_req import (
            UnibeeApiMerchantRoleDeleteReq
        )
        try:
            req = UnibeeApiMerchantRoleDeleteReq(id=role_id)
            response = self._api.role_delete_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
