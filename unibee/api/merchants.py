# coding: utf-8
"""
UniBee Merchants API

Manage merchant profile and settings.
"""

from typing import Any, Dict, Optional

from unibee.api.base import BaseAPI


class MerchantsAPI(BaseAPI):
    """
    API for managing merchant profile and settings.
    
    Example:
        ```python
        from unibee import UniBeeClient
        
        client = UniBeeClient(api_key="your-api-key")
        
        # Get merchant profile
        profile = client.merchants.get_profile()
        
        # Update profile
        client.merchants.update_profile(
            company_name="My Company",
            company_logo="https://example.com/logo.png",
        )
        ```
    """
    
    def get_profile(self) -> Dict[str, Any]:
        """
        Get merchant profile information.
        
        Returns:
            Merchant profile details.
        """
        return self._get("/merchant/get")
    
    def update_profile(
        self,
        company_name: Optional[str] = None,
        company_logo: Optional[str] = None,
        home_url: Optional[str] = None,
        phone: Optional[str] = None,
        address: Optional[str] = None,
        timezone: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update merchant profile.
        
        Args:
            company_name: Company name.
            company_logo: URL to company logo.
            home_url: Company website URL.
            phone: Company phone number.
            address: Company address.
            timezone: Timezone (e.g., "UTC", "America/New_York").
            **kwargs: Additional profile fields.
        
        Returns:
            Updated profile details.
        """
        data = {
            "companyName": company_name,
            "companyLogo": company_logo,
            "homeUrl": home_url,
            "phone": phone,
            "address": address,
            "timezone": timezone,
            **kwargs,
        }
        return self._post("/merchant/update", data=data)
    
    def get_country_config_list(self) -> Dict[str, Any]:
        """
        Get country configuration list.
        
        Returns:
            List of country configurations.
        """
        return self._post("/merchant/country_config_list", data={})
    
    def edit_country_config(
        self,
        country_code: str,
        **config,
    ) -> Dict[str, Any]:
        """
        Edit country-specific configuration.
        
        Args:
            country_code: Country code (e.g., "US").
            **config: Configuration parameters.
        
        Returns:
            Updated country configuration.
        """
        data = {
            "countryCode": country_code,
            **config,
        }
        return self._post("/merchant/edit_country_config", data=data)
    
    def search(
        self,
        search_key: str,
    ) -> Dict[str, Any]:
        """
        Search across merchant data.
        
        Args:
            search_key: Search term.
        
        Returns:
            Search results across users, subscriptions, invoices, etc.
        """
        return self._post(
            "/merchant/search/key_search",
            data={"searchKey": search_key},
        )
    
    def get_license(self) -> Dict[str, Any]:
        """
        Get merchant license information.
        
        Returns:
            License details.
        """
        return self._get("/merchant/license")
    
    def generate_api_key(self) -> Dict[str, Any]:
        """
        Generate a new API key.
        
        Returns:
            New API key.
        """
        return self._post("/merchant/generate_apikey", data={})
