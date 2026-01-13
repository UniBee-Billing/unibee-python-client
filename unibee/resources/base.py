# coding: utf-8
"""
Base Resource Class

Provides common functionality for all API resources.
"""

from typing import Any, Dict, Optional, TypeVar, Generic
import logging

from openapi_client import ApiClient
from openapi_client.rest import ApiException

from unibee.exceptions import (
    UniBeeError,
    UniBeeAuthenticationError,
    UniBeeAPIError,
    UniBeeConnectionError,
    raise_for_status,
)

logger = logging.getLogger("unibee")

T = TypeVar("T")


class BaseResource:
    """
    Base class for all API resources.
    
    Provides common error handling and request processing.
    """
    
    def __init__(self, api_client: ApiClient):
        """
        Initialize the resource with an API client.
        
        Args:
            api_client: The OpenAPI client instance
        """
        self._api_client = api_client
    
    def _handle_api_exception(self, e: ApiException) -> None:
        """
        Convert OpenAPI exceptions to UniBee exceptions.
        
        Args:
            e: The ApiException from the underlying client
            
        Raises:
            Appropriate UniBee exception based on the error
        """
        status_code = e.status
        message = str(e.reason) if e.reason else "API Error"
        response_data = None
        request_id = None
        
        # Try to parse response body
        if e.body:
            try:
                import json
                response_data = json.loads(e.body)
                message = response_data.get("message", message)
                request_id = response_data.get("requestId")
            except (json.JSONDecodeError, TypeError):
                pass
        
        raise_for_status(
            status_code=status_code,
            message=message,
            response_data=response_data,
            request_id=request_id,
        )
    
    def _extract_data(self, response: Any) -> Any:
        """
        Extract the data from API response.
        
        UniBee API responses typically have the structure:
        {
            "code": 0,
            "message": "success",
            "data": { ... actual data ... },
            "requestId": "..."
        }
        
        This method extracts the 'data' field for convenience.
        
        Args:
            response: The raw API response object
            
        Returns:
            The extracted data or the original response if not wrapped
        """
        if hasattr(response, "data") and response.data is not None:
            return response.data
        return response
    
    def _dict_to_model(self, data: Dict[str, Any], model_class: type) -> Any:
        """
        Convert a dictionary to a model instance.
        
        Args:
            data: Dictionary with model data
            model_class: The target model class
            
        Returns:
            Instance of the model class
        """
        if hasattr(model_class, "from_dict"):
            return model_class.from_dict(data)
        return model_class(**data)
