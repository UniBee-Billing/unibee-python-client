# coding: utf-8
"""
UniBee SDK Custom Exceptions

This module provides custom exception classes for the UniBee SDK,
making error handling more intuitive and Pythonic.
"""

from typing import Optional, Dict, Any


class UniBeeError(Exception):
    """Base exception for all UniBee SDK errors."""

    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        response_data: Optional[Dict[str, Any]] = None,
        request_id: Optional[str] = None,
    ):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response_data = response_data or {}
        self.request_id = request_id

    def __str__(self) -> str:
        parts = [self.message]
        if self.status_code:
            parts.append(f"(HTTP {self.status_code})")
        if self.request_id:
            parts.append(f"[Request ID: {self.request_id}]")
        return " ".join(parts)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.message!r}, status_code={self.status_code})"


class UniBeeAuthenticationError(UniBeeError):
    """
    Raised when authentication fails.
    
    This typically happens when:
    - API key is invalid or expired
    - API key is missing
    - Insufficient permissions
    """
    pass


class UniBeeAPIError(UniBeeError):
    """
    Raised when the API returns an error response.
    
    This is a general API error that doesn't fall into other categories.
    Check the status_code and response_data for more details.
    """
    pass


class UniBeeValidationError(UniBeeError):
    """
    Raised when request validation fails.
    
    This typically happens when:
    - Required parameters are missing
    - Parameter types are incorrect
    - Parameter values are out of range
    """
    
    def __init__(
        self,
        message: str,
        errors: Optional[Dict[str, Any]] = None,
        **kwargs
    ):
        super().__init__(message, **kwargs)
        self.errors = errors or {}


class UniBeeNotFoundError(UniBeeError):
    """
    Raised when a requested resource is not found.
    
    This typically happens when:
    - User ID doesn't exist
    - Subscription ID doesn't exist
    - Invoice ID doesn't exist
    """
    pass


class UniBeeRateLimitError(UniBeeError):
    """
    Raised when rate limit is exceeded.
    
    The retry_after attribute indicates how many seconds to wait
    before making another request.
    """
    
    def __init__(
        self,
        message: str,
        retry_after: Optional[int] = None,
        **kwargs
    ):
        super().__init__(message, **kwargs)
        self.retry_after = retry_after


class UniBeeConnectionError(UniBeeError):
    """
    Raised when a connection error occurs.
    
    This typically happens when:
    - Network is unavailable
    - DNS resolution fails
    - Connection timeout
    """
    pass


class UniBeeTimeoutError(UniBeeError):
    """
    Raised when a request times out.
    
    This typically happens when:
    - Server takes too long to respond
    - Network latency is too high
    """
    pass


def raise_for_status(
    status_code: int,
    message: str,
    response_data: Optional[Dict[str, Any]] = None,
    request_id: Optional[str] = None,
) -> None:
    """
    Raise appropriate exception based on HTTP status code.
    
    Args:
        status_code: HTTP status code
        message: Error message
        response_data: Response data from API
        request_id: Request ID for debugging
        
    Raises:
        UniBeeAuthenticationError: For 401 errors
        UniBeeNotFoundError: For 404 errors
        UniBeeValidationError: For 400/422 errors
        UniBeeRateLimitError: For 429 errors
        UniBeeAPIError: For other errors
    """
    kwargs = {
        "status_code": status_code,
        "response_data": response_data,
        "request_id": request_id,
    }
    
    if status_code == 401:
        raise UniBeeAuthenticationError(
            message or "Authentication failed. Check your API key.",
            **kwargs
        )
    elif status_code == 403:
        raise UniBeeAuthenticationError(
            message or "Permission denied. Check your API key permissions.",
            **kwargs
        )
    elif status_code == 404:
        raise UniBeeNotFoundError(
            message or "Resource not found.",
            **kwargs
        )
    elif status_code in (400, 422):
        errors = response_data.get("errors") if response_data else None
        raise UniBeeValidationError(
            message or "Validation failed.",
            errors=errors,
            **kwargs
        )
    elif status_code == 429:
        retry_after = None
        if response_data:
            retry_after = response_data.get("retry_after")
        raise UniBeeRateLimitError(
            message or "Rate limit exceeded. Please slow down your requests.",
            retry_after=retry_after,
            **kwargs
        )
    else:
        raise UniBeeAPIError(message or f"API error (HTTP {status_code})", **kwargs)
