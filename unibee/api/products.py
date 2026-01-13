# coding: utf-8
"""
UniBee Products API

Manage products.
"""

from typing import Any, Dict, List, Optional

from unibee.api.base import BaseAPI


class ProductsAPI(BaseAPI):
    """
    API for managing products.
    
    Products are containers for plans. Each product can have
    multiple plans associated with it.
    
    Example:
        ```python
        from unibee import UniBeeClient
        
        client = UniBeeClient(api_key="your-api-key")
        
        # List products
        products = client.products.list()
        
        # Create a new product
        product = client.products.create(
            product_name="Pro Plan",
            description="Our professional tier",
        )
        ```
    """
    
    def list(
        self,
        status: Optional[List[int]] = None,
        page: int = 0,
        count: int = 20,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        List products.
        
        Args:
            status: Filter by status.
                    Status: 1=Active, 2=Inactive
            page: Page number (0-indexed).
            count: Number of results per page.
            **kwargs: Additional filter parameters.
        
        Returns:
            List of products.
        """
        data = {
            "status": status,
            "page": page,
            "count": count,
            **kwargs,
        }
        return self._post("/merchant/product/list", data=data)
    
    def get(
        self,
        product_id: int,
    ) -> Dict[str, Any]:
        """
        Get product details.
        
        Args:
            product_id: The product ID.
        
        Returns:
            Product details.
        """
        return self._post(
            "/merchant/product/detail",
            data={"productId": product_id},
        )
    
    def create(
        self,
        product_name: str,
        description: Optional[str] = None,
        home_url: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create a new product.
        
        Args:
            product_name: Product name.
            description: Product description.
            home_url: Product home URL.
            metadata: Additional metadata.
            **kwargs: Additional parameters.
        
        Returns:
            Created product details.
        """
        data = {
            "productName": product_name,
            "description": description,
            "homeUrl": home_url,
            "metadata": metadata,
            **kwargs,
        }
        return self._post("/merchant/product/new", data=data)
    
    def edit(
        self,
        product_id: int,
        product_name: Optional[str] = None,
        description: Optional[str] = None,
        home_url: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Edit an existing product.
        
        Args:
            product_id: The product ID to edit.
            product_name: New product name.
            description: New description.
            home_url: New home URL.
            metadata: New metadata.
            **kwargs: Additional parameters.
        
        Returns:
            Updated product details.
        """
        data = {
            "productId": product_id,
            "productName": product_name,
            "description": description,
            "homeUrl": home_url,
            "metadata": metadata,
            **kwargs,
        }
        return self._post("/merchant/product/edit", data=data)
    
    def delete(
        self,
        product_id: int,
    ) -> Dict[str, Any]:
        """
        Delete a product.
        
        Args:
            product_id: The product ID to delete.
        
        Returns:
            Deletion confirmation.
        """
        return self._post(
            "/merchant/product/delete",
            data={"productId": product_id},
        )
    
    def activate(
        self,
        product_id: int,
    ) -> Dict[str, Any]:
        """
        Activate a product.
        
        Args:
            product_id: The product ID to activate.
        
        Returns:
            Activated product details.
        """
        return self._post(
            "/merchant/product/activate",
            data={"productId": product_id},
        )
    
    def inactivate(
        self,
        product_id: int,
    ) -> Dict[str, Any]:
        """
        Inactivate a product.
        
        Args:
            product_id: The product ID to inactivate.
        
        Returns:
            Inactivated product details.
        """
        return self._post(
            "/merchant/product/inactivate",
            data={"productId": product_id},
        )
    
    def copy(
        self,
        product_id: int,
    ) -> Dict[str, Any]:
        """
        Copy a product.
        
        Args:
            product_id: The product ID to copy.
        
        Returns:
            New product details.
        """
        return self._post(
            "/merchant/product/copy",
            data={"productId": product_id},
        )
