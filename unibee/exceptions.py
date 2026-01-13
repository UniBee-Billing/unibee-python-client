# coding: utf-8
"""
UniBee SDK Exceptions

Custom exception classes for the UniBee Python SDK.
"""

from typing import Any, Optional, Dict


class UniBeeError(Exception):
    """
    Base exception class for all UniBee SDK errors.
    """
    
    def __init__(
        self,
        message: str,
        code: Optional[int] = None,
        request_id: Optional[str] = None,
        response: Optional[Dict[str, Any]] = None,
    ):
        """
        Initialize UniBee error.
        
        Args:
            message: Error message.
            code: Error code from API response.
            request_id: Request ID for debugging.
            response: Full API response.
        """
        super().__init__(message)
        self.message = message
        self.code = code
        self.request_id = request_id
        self.response = response
    
    def __str__(self) -> str:
        parts = [self.message]
        if self.code:
            parts.append(f"(code: {self.code})")
        if self.request_id:
            parts.append(f"[request_id: {self.request_id}]")
        return " ".join(parts)
    
    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"message={self.message!r}, "
            f"code={self.code}, "
            f"request_id={self.request_id!r})"
        )


class AuthenticationError(UniBeeError):
    """
    Raised when authentication fails (401/403 errors).
    
    This typically occurs when:
    - API key is missing or invalid
    - API key has expired
    - API key lacks required permissions
    """
    pass


class APIError(UniBeeError):
    """
    Raised when the API returns an error response.
    
    This is the general error class for API errors that don't
    fit into more specific categories.
    """
    
    def __init__(
        self,
        message: str,
        http_status: int,
        code: Optional[int] = None,
        request_id: Optional[str] = None,
        response: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(message, code, request_id, response)
        self.http_status = http_status


class NotFoundError(UniBeeError):
    """
    Raised when a requested resource is not found (404 error).
    
    This typically occurs when:
    - Looking up a non-existent subscription, invoice, etc.
    - Using an invalid ID
    """
    pass


class ValidationError(UniBeeError):
    """
    Raised when request validation fails (400 error).
    
    This typically occurs when:
    - Required parameters are missing
    - Parameters have invalid values
    - Business logic validation fails
    """
    
    def __init__(
        self,
        message: str,
        errors: Optional[Dict[str, Any]] = None,
        code: Optional[int] = None,
        request_id: Optional[str] = None,
        response: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(message, code, request_id, response)
        self.errors = errors or {}


class RateLimitError(UniBeeError):
    """
    Raised when the API rate limit is exceeded (429 error).
    
    Contains retry information when available.
    """
    
    def __init__(
        self,
        message: str,
        retry_after: Optional[int] = None,
        code: Optional[int] = None,
        request_id: Optional[str] = None,
        response: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(message, code, request_id, response)
        self.retry_after = retry_after


class NetworkError(UniBeeError):
    """
    Raised when a network error occurs.
    
    This typically occurs when:
    - Connection times out
    - DNS resolution fails
    - Network is unreachable
    """
    pass


class ServerError(UniBeeError):
    """
    Raised when the API returns a server error (5xx).
    
    This indicates an issue on the UniBee server side.
    """
    pass
