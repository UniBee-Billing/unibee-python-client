# coding: utf-8
"""
UniBee Users API

Manage users and customers.
"""

from typing import Any, Dict, List, Optional

from unibee.api.base import BaseAPI


class UsersAPI(BaseAPI):
    """
    API for managing users (customers).
    
    Example:
        ```python
        from unibee import UniBeeClient
        
        client = UniBeeClient(api_key="your-api-key")
        
        # Get user details
        user = client.users.get(user_id=123)
        
        # List users
        users = client.users.list()
        
        # Create a new user
        user = client.users.create(email="user@example.com")
        
        # Search users
        results = client.users.search(email="user@example.com")
        ```
    """
    
    def list(
        self,
        status: Optional[List[int]] = None,
        sort_field: Optional[str] = None,
        sort_type: Optional[str] = None,
        page: int = 0,
        count: int = 20,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        List users with optional filters.
        
        Args:
            status: Filter by user status.
            sort_field: Field to sort by.
            sort_type: Sort direction ('asc' or 'desc').
            page: Page number (0-indexed).
            count: Number of results per page.
            **kwargs: Additional filter parameters.
        
        Returns:
            Dictionary containing 'users' list and pagination info.
        """
        data = {
            "status": status,
            "sortField": sort_field,
            "sortType": sort_type,
            "page": page,
            "count": count,
            **kwargs,
        }
        return self._post("/merchant/user/list", data=data)
    
    def get(
        self,
        user_id: Optional[int] = None,
        email: Optional[str] = None,
        external_user_id: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Get user details.
        
        Provide one of: user_id, email, or external_user_id.
        
        Args:
            user_id: The user ID.
            email: The user's email.
            external_user_id: External user ID.
        
        Returns:
            User details.
        """
        params = {
            "userId": user_id,
            "email": email,
            "externalUserId": external_user_id,
        }
        # Filter out None values
        params = {k: v for k, v in params.items() if v is not None}
        return self._get("/merchant/user/get", params=params)
    
    def create(
        self,
        email: str,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        external_user_id: Optional[str] = None,
        phone: Optional[str] = None,
        address: Optional[str] = None,
        city: Optional[str] = None,
        zip_code: Optional[str] = None,
        country_code: Optional[str] = None,
        country_name: Optional[str] = None,
        vat_number: Optional[str] = None,
        language: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create a new user.
        
        Args:
            email: User's email address.
            first_name: User's first name.
            last_name: User's last name.
            external_user_id: External user ID for integration.
            phone: Phone number.
            address: Street address.
            city: City.
            zip_code: Postal/ZIP code.
            country_code: Country code (e.g., "US").
            country_name: Country name.
            vat_number: VAT number for tax purposes.
            language: Preferred language code.
            metadata: Additional metadata.
            **kwargs: Additional parameters.
        
        Returns:
            Created user details.
        """
        data = {
            "email": email,
            "firstName": first_name,
            "lastName": last_name,
            "externalUserId": external_user_id,
            "phone": phone,
            "address": address,
            "city": city,
            "zipCode": zip_code,
            "countryCode": country_code,
            "countryName": country_name,
            "vATNumber": vat_number,
            "language": language,
            "metadata": metadata,
            **kwargs,
        }
        return self._post("/merchant/user/new", data=data)
    
    def update(
        self,
        user_id: int,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        external_user_id: Optional[str] = None,
        phone: Optional[str] = None,
        address: Optional[str] = None,
        city: Optional[str] = None,
        zip_code: Optional[str] = None,
        country_code: Optional[str] = None,
        country_name: Optional[str] = None,
        vat_number: Optional[str] = None,
        language: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update an existing user.
        
        Args:
            user_id: The user ID to update.
            first_name: User's first name.
            last_name: User's last name.
            external_user_id: External user ID.
            phone: Phone number.
            address: Street address.
            city: City.
            zip_code: Postal/ZIP code.
            country_code: Country code.
            country_name: Country name.
            vat_number: VAT number.
            language: Preferred language code.
            metadata: Additional metadata.
            **kwargs: Additional parameters.
        
        Returns:
            Updated user details.
        """
        data = {
            "userId": user_id,
            "firstName": first_name,
            "lastName": last_name,
            "externalUserId": external_user_id,
            "phone": phone,
            "address": address,
            "city": city,
            "zipCode": zip_code,
            "countryCode": country_code,
            "countryName": country_name,
            "vATNumber": vat_number,
            "language": language,
            "metadata": metadata,
            **kwargs,
        }
        return self._post("/merchant/user/update", data=data)
    
    def search(
        self,
        email: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        page: int = 0,
        count: int = 20,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Search for users.
        
        Args:
            email: Search by email.
            first_name: Search by first name.
            last_name: Search by last name.
            page: Page number (0-indexed).
            count: Number of results per page.
            **kwargs: Additional search parameters.
        
        Returns:
            Search results with matching users.
        """
        data = {
            "email": email,
            "firstName": first_name,
            "lastName": last_name,
            "page": page,
            "count": count,
            **kwargs,
        }
        return self._post("/merchant/user/search", data=data)
    
    def suspend(
        self,
        user_id: int,
    ) -> Dict[str, Any]:
        """
        Suspend a user (freeze account).
        
        Args:
            user_id: The user ID to suspend.
        
        Returns:
            Updated user details.
        """
        return self._post(
            "/merchant/user/frozen_user",
            data={"userId": user_id},
        )
    
    def resume(
        self,
        user_id: int,
    ) -> Dict[str, Any]:
        """
        Resume a suspended user (unfreeze account).
        
        Args:
            user_id: The user ID to resume.
        
        Returns:
            Updated user details.
        """
        return self._post(
            "/merchant/user/release_user",
            data={"userId": user_id},
        )
    
    def count(self) -> Dict[str, Any]:
        """
        Get total user count.
        
        Returns:
            User count information.
        """
        return self._get("/merchant/user/count")
    
    def change_email(
        self,
        user_id: int,
        new_email: str,
    ) -> Dict[str, Any]:
        """
        Change a user's email address.
        
        Args:
            user_id: The user ID.
            new_email: New email address.
        
        Returns:
            Updated user details.
        """
        return self._post(
            "/merchant/user/change_email",
            data={
                "userId": user_id,
                "newEmail": new_email,
            },
        )
    
    def change_gateway(
        self,
        user_id: int,
        gateway_id: int,
    ) -> Dict[str, Any]:
        """
        Change a user's default payment gateway.
        
        Args:
            user_id: The user ID.
            gateway_id: New default gateway ID.
        
        Returns:
            Updated user details.
        """
        return self._post(
            "/merchant/user/change_gateway",
            data={
                "userId": user_id,
                "gatewayId": gateway_id,
            },
        )
    
    def clear_payment_method(
        self,
        user_id: int,
    ) -> Dict[str, Any]:
        """
        Clear a user's saved payment method.
        
        Args:
            user_id: The user ID.
        
        Returns:
            Update confirmation.
        """
        return self._post(
            "/merchant/user/clear_autocharge_method",
            data={"userId": user_id},
        )
    
    def list_notes(
        self,
        user_id: int,
        page: int = 0,
        count: int = 20,
    ) -> Dict[str, Any]:
        """
        List admin notes for a user.
        
        Args:
            user_id: The user ID.
            page: Page number (0-indexed).
            count: Number of results per page.
        
        Returns:
            List of admin notes.
        """
        return self._post(
            "/merchant/user/admin_note_list",
            data={
                "userId": user_id,
                "page": page,
                "count": count,
            },
        )
    
    def add_note(
        self,
        user_id: int,
        note: str,
    ) -> Dict[str, Any]:
        """
        Add an admin note to a user.
        
        Args:
            user_id: The user ID.
            note: The note content.
        
        Returns:
            Created note details.
        """
        return self._post(
            "/merchant/user/new_admin_note",
            data={
                "userId": user_id,
                "note": note,
            },
        )
