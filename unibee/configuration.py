# coding: utf-8
"""
UniBee SDK Configuration

This module provides configuration settings for the UniBee API client.
"""

import os
from typing import Optional


class Configuration:
    """
    Configuration settings for the UniBee API client.
    
    Attributes:
        api_key: The API key for authentication (Bearer token).
        base_url: The base URL for the API. Defaults to production.
        timeout: Request timeout in seconds.
        verify_ssl: Whether to verify SSL certificates.
        debug: Enable debug logging.
    
    Example:
        ```python
        from unibee import Configuration
        
        # Using environment variable
        config = Configuration()
        
        # Or explicit configuration
        config = Configuration(
            api_key="your-api-key",
            base_url="https://api.unibee.dev"
        )
        ```
    """
    
    # Production API URL
    DEFAULT_BASE_URL = "https://api.unibee.dev"
    
    # Sandbox API URL for testing
    SANDBOX_BASE_URL = "https://api-sandbox.unibee.top"
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: int = 30,
        verify_ssl: bool = True,
        debug: bool = False,
    ):
        """
        Initialize configuration.
        
        Args:
            api_key: API key for authentication. If not provided, reads from
                     UNIBEE_API_KEY environment variable.
            base_url: Base URL for the API. If not provided, reads from
                      UNIBEE_BASE_URL environment variable or uses production URL.
            timeout: Request timeout in seconds. Defaults to 30.
            verify_ssl: Whether to verify SSL certificates. Defaults to True.
            debug: Enable debug logging. Defaults to False.
        """
        self.api_key = api_key or os.environ.get("UNIBEE_API_KEY")
        self.base_url = (
            base_url 
            or os.environ.get("UNIBEE_BASE_URL") 
            or self.DEFAULT_BASE_URL
        )
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        self.debug = debug
        
        # Remove trailing slash from base URL
        if self.base_url and self.base_url.endswith("/"):
            self.base_url = self.base_url[:-1]
    
    @classmethod
    def sandbox(cls, api_key: Optional[str] = None, **kwargs) -> "Configuration":
        """
        Create a configuration for the sandbox environment.
        
        Args:
            api_key: API key for authentication.
            **kwargs: Additional configuration options.
        
        Returns:
            Configuration instance configured for sandbox.
        """
        return cls(api_key=api_key, base_url=cls.SANDBOX_BASE_URL, **kwargs)
    
    @classmethod
    def production(cls, api_key: Optional[str] = None, **kwargs) -> "Configuration":
        """
        Create a configuration for the production environment.
        
        Args:
            api_key: API key for authentication.
            **kwargs: Additional configuration options.
        
        Returns:
            Configuration instance configured for production.
        """
        return cls(api_key=api_key, base_url=cls.DEFAULT_BASE_URL, **kwargs)
    
    def get_auth_headers(self) -> dict:
        """
        Get authentication headers for API requests.
        
        Returns:
            Dictionary containing Authorization header.
        
        Raises:
            ValueError: If API key is not configured.
        """
        if not self.api_key:
            raise ValueError(
                "API key is not configured. Set it via Configuration(api_key='...') "
                "or the UNIBEE_API_KEY environment variable."
            )
        
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
    
    def __repr__(self) -> str:
        return (
            f"Configuration(base_url={self.base_url!r}, "
            f"timeout={self.timeout}, debug={self.debug})"
        )
