# coding: utf-8
"""
User Resource

Provides methods for managing users in UniBee.
"""

from typing import Any, Dict, List, Optional

from openapi_client import ApiClient
from openapi_client.api.user import User as UserApi
from openapi_client.rest import ApiException

from unibee.resources.base import BaseResource


class UserResource(BaseResource):
    """
    User management resource.
    
    Provides methods for creating, updating, and querying users.
    
    Example:
        >>> # List users
        >>> users = client.user.list()
        >>> 
        >>> # Get user profile
        >>> user = client.user.get(user_id=123)
        >>> 
        >>> # Search users by email
        >>> users = client.user.search(email="john@example.com")
    """
    
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)
        self._api = UserApi(api_client)
    
    def list(
        self,
        status: Optional[List[int]] = None,
        page: int = 0,
        count: int = 20,
        sort_field: Optional[str] = None,
        sort_type: Optional[str] = None,
        **kwargs
    ) -> Any:
        """
        List users with optional filters.
        
        Args:
            status: Filter by user status codes
            page: Page number (0-indexed)
            count: Number of items per page
            sort_field: Field to sort by
            sort_type: Sort direction ("asc" or "desc")
            
        Returns:
            List of users
            
        Example:
            >>> users = client.user.list(count=50)
            >>> for user in users.users:
            ...     print(user.email)
        """
        try:
            response = self._api.user_list_get(
                status=status,
                page=page,
                count=count,
                sort_field=sort_field,
                sort_type=sort_type,
            )
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def get(
        self,
        user_id: int,
        **kwargs
    ) -> Any:
        """
        Get user profile by ID.
        
        Args:
            user_id: The user ID
            
        Returns:
            User profile details
            
        Example:
            >>> user = client.user.get(user_id=123)
            >>> print(user.email, user.first_name)
        """
        try:
            response = self._api.user_get_get(
                user_id=user_id,
            )
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def search(
        self,
        email: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        page: int = 0,
        count: int = 20,
        **kwargs
    ) -> Any:
        """
        Search users by various criteria.
        
        Args:
            email: Search by email (partial match)
            first_name: Search by first name
            last_name: Search by last name
            page: Page number
            count: Items per page
            
        Returns:
            Search results
            
        Example:
            >>> results = client.user.search(email="john")
        """
        try:
            response = self._api.user_search_get(
                email=email,
                first_name=first_name,
                last_name=last_name,
                page=page,
                count=count,
            )
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def update(
        self,
        user_id: int,
        email: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[str] = None,
        address: Optional[str] = None,
        country_code: Optional[str] = None,
        vat_number: Optional[str] = None,
        **kwargs
    ) -> Any:
        """
        Update user profile.
        
        Args:
            user_id: The user ID
            email: New email address
            first_name: First name
            last_name: Last name
            phone: Phone number
            address: Address
            country_code: Country code (ISO 3166-1 alpha-2)
            vat_number: VAT number for business customers
            
        Returns:
            Updated user profile
            
        Example:
            >>> user = client.user.update(
            ...     user_id=123,
            ...     first_name="John",
            ...     last_name="Doe"
            ... )
        """
        from openapi_client.models.unibee_api_merchant_user_update_req import (
            UnibeeApiMerchantUserUpdateReq
        )
        
        try:
            req = UnibeeApiMerchantUserUpdateReq(
                user_id=user_id,
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                address=address,
                country_code=country_code,
                vat_number=vat_number,
            )
            response = self._api.user_update_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def suspend(
        self,
        user_id: int,
        **kwargs
    ) -> Any:
        """
        Suspend (freeze) a user account.
        
        Args:
            user_id: The user ID
            
        Returns:
            Result
            
        Example:
            >>> client.user.suspend(user_id=123)
        """
        from openapi_client.models.unibee_api_merchant_user_frozen_req import (
            UnibeeApiMerchantUserFrozenReq
        )
        
        try:
            req = UnibeeApiMerchantUserFrozenReq(
                user_id=user_id,
            )
            response = self._api.user_frozen_user_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def resume(
        self,
        user_id: int,
        **kwargs
    ) -> Any:
        """
        Resume a suspended user account.
        
        Args:
            user_id: The user ID
            
        Returns:
            Result
            
        Example:
            >>> client.user.resume(user_id=123)
        """
        from openapi_client.models.unibee_api_merchant_user_release_req import (
            UnibeeApiMerchantUserReleaseReq
        )
        
        try:
            req = UnibeeApiMerchantUserReleaseReq(
                user_id=user_id,
            )
            response = self._api.user_release_user_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
