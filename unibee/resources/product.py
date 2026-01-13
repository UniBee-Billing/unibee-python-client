# coding: utf-8
"""
Product Resource

Provides methods for managing products in UniBee.
"""

from typing import Any, Dict, List, Optional

from openapi_client import ApiClient
from openapi_client.rest import ApiException

from unibee.resources.base import BaseResource


class ProductResource(BaseResource):
    """
    Product management resource.
    
    Products are containers for subscription plans.
    """
    
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)
        # Product API may be imported dynamically since it's a newer endpoint
        try:
            from openapi_client.api.product import Product as ProductApi
            self._api = ProductApi(api_client)
            self._available = True
        except ImportError:
            self._api = None
            self._available = False
    
    def list(
        self,
        status: Optional[List[int]] = None,
        page: int = 0,
        count: int = 20,
        **kwargs
    ) -> Any:
        """
        List products.
        
        Args:
            status: Filter by status
            page: Page number
            count: Items per page
            
        Returns:
            List of products
        """
        if not self._available:
            raise NotImplementedError("Product API not available in current SDK version")
        
        try:
            response = self._api.product_list_get(
                status=status,
                page=page,
                count=count,
            )
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def get(
        self,
        product_id: int,
        **kwargs
    ) -> Any:
        """
        Get product details.
        
        Args:
            product_id: The product ID
            
        Returns:
            Product details
        """
        if not self._available:
            raise NotImplementedError("Product API not available in current SDK version")
        
        try:
            response = self._api.product_detail_get(
                product_id=product_id,
            )
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
