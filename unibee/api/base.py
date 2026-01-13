# coding: utf-8
"""
Base API Resource Class

Provides common functionality for all API resource classes.
"""

from typing import Any, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from unibee.http_client import HTTPClient


class BaseAPI:
    """
    Base class for API resources.
    
    All API resource classes inherit from this class to get
    access to the HTTP client and common functionality.
    """
    
    def __init__(self, http_client: "HTTPClient"):
        """
        Initialize the API resource.
        
        Args:
            http_client: HTTP client instance for making requests.
        """
        self._http = http_client
    
    def _get(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make a GET request and return the data."""
        response = self._http.get(path, params=params)
        return response.get("data", response)
    
    def _post(
        self,
        path: str,
        data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make a POST request and return the data."""
        response = self._http.post(path, data=data)
        return response.get("data", response)
    
    def _put(
        self,
        path: str,
        data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make a PUT request and return the data."""
        response = self._http.put(path, data=data)
        return response.get("data", response)
    
    def _delete(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make a DELETE request and return the data."""
        response = self._http.delete(path, params=params)
        return response.get("data", response)
