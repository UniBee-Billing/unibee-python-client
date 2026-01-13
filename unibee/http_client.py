# coding: utf-8
"""
UniBee SDK HTTP Client

Low-level HTTP client for making API requests.
"""

import json
import logging
from typing import Any, Dict, Optional, Union
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode

from unibee.configuration import Configuration
from unibee.exceptions import (
    APIError,
    AuthenticationError,
    NetworkError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
)

logger = logging.getLogger("unibee")


class HTTPClient:
    """
    Low-level HTTP client for making API requests to UniBee.
    """
    
    def __init__(self, config: Configuration):
        """
        Initialize HTTP client.
        
        Args:
            config: Configuration instance.
        """
        self.config = config
        
        if config.debug:
            logging.basicConfig(level=logging.DEBUG)
            logger.setLevel(logging.DEBUG)
    
    def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """
        Make an HTTP request to the API.
        
        Args:
            method: HTTP method (GET, POST, etc.).
            path: API endpoint path.
            params: Query parameters.
            data: Request body data.
            headers: Additional headers.
        
        Returns:
            Parsed JSON response.
        
        Raises:
            AuthenticationError: Authentication failed.
            ValidationError: Request validation failed.
            NotFoundError: Resource not found.
            RateLimitError: Rate limit exceeded.
            ServerError: Server error occurred.
            APIError: Other API error.
            NetworkError: Network error occurred.
        """
        # Build URL
        url = f"{self.config.base_url}{path}"
        if params:
            # Filter out None values
            filtered_params = {k: v for k, v in params.items() if v is not None}
            if filtered_params:
                url = f"{url}?{urlencode(filtered_params)}"
        
        # Build headers
        request_headers = self.config.get_auth_headers()
        if headers:
            request_headers.update(headers)
        
        # Build request body
        body = None
        if data:
            # Filter out None values
            filtered_data = self._filter_none(data)
            body = json.dumps(filtered_data).encode("utf-8")
        
        logger.debug(f"Request: {method} {url}")
        if body:
            logger.debug(f"Body: {body.decode('utf-8')}")
        
        try:
            request = Request(
                url,
                data=body,
                headers=request_headers,
                method=method,
            )
            
            with urlopen(request, timeout=self.config.timeout) as response:
                response_body = response.read().decode("utf-8")
                logger.debug(f"Response: {response_body}")
                
                result = json.loads(response_body) if response_body else {}
                return self._process_response(result)
        
        except HTTPError as e:
            return self._handle_http_error(e)
        
        except URLError as e:
            raise NetworkError(f"Network error: {e.reason}")
        
        except json.JSONDecodeError as e:
            raise APIError(
                f"Invalid JSON response: {e}",
                http_status=0,
            )
    
    def _filter_none(self, data: Union[Dict, list, Any]) -> Any:
        """Recursively filter out None values from data."""
        if isinstance(data, dict):
            return {k: self._filter_none(v) for k, v in data.items() if v is not None}
        elif isinstance(data, list):
            return [self._filter_none(item) for item in data if item is not None]
        return data
    
    def _process_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process API response and check for errors.
        
        Args:
            response: Parsed JSON response.
        
        Returns:
            Response data if successful.
        
        Raises:
            APIError: If response indicates an error.
        """
        # UniBee API uses 'code' field for status
        code = response.get("code", 0)
        message = response.get("message", "")
        request_id = response.get("requestId")
        
        # Code 0 typically means success in UniBee API
        if code != 0 and code != 200:
            raise APIError(
                message=message or "API error",
                http_status=200,  # HTTP was successful but API returned error
                code=code,
                request_id=request_id,
                response=response,
            )
        
        return response
    
    def _handle_http_error(self, error: HTTPError) -> Dict[str, Any]:
        """
        Handle HTTP error responses.
        
        Args:
            error: HTTPError exception.
        
        Raises:
            Appropriate exception based on status code.
        """
        status_code = error.code
        
        try:
            response_body = error.read().decode("utf-8")
            response = json.loads(response_body) if response_body else {}
        except (json.JSONDecodeError, UnicodeDecodeError):
            response = {}
        
        message = response.get("message", str(error.reason))
        code = response.get("code")
        request_id = response.get("requestId")
        
        if status_code == 400:
            raise ValidationError(
                message=message,
                code=code,
                request_id=request_id,
                response=response,
            )
        
        if status_code == 401 or status_code == 403:
            raise AuthenticationError(
                message=message or "Authentication failed",
                code=code,
                request_id=request_id,
                response=response,
            )
        
        if status_code == 404:
            raise NotFoundError(
                message=message or "Resource not found",
                code=code,
                request_id=request_id,
                response=response,
            )
        
        if status_code == 429:
            retry_after = error.headers.get("Retry-After")
            raise RateLimitError(
                message=message or "Rate limit exceeded",
                retry_after=int(retry_after) if retry_after else None,
                code=code,
                request_id=request_id,
                response=response,
            )
        
        if status_code >= 500:
            raise ServerError(
                message=message or f"Server error: {status_code}",
                code=code,
                request_id=request_id,
                response=response,
            )
        
        raise APIError(
            message=message or f"HTTP error: {status_code}",
            http_status=status_code,
            code=code,
            request_id=request_id,
            response=response,
        )
    
    def get(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """Make a GET request."""
        return self.request("GET", path, params=params, **kwargs)
    
    def post(
        self,
        path: str,
        data: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """Make a POST request."""
        return self.request("POST", path, data=data, **kwargs)
    
    def put(
        self,
        path: str,
        data: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """Make a PUT request."""
        return self.request("PUT", path, data=data, **kwargs)
    
    def delete(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """Make a DELETE request."""
        return self.request("DELETE", path, params=params, **kwargs)
