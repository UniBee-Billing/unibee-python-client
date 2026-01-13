"""
Tests for UniBee Python SDK Client
"""

import os
import pytest

from unibee import UniBeeClient, Configuration, __version__
from unibee.exceptions import (
    UniBeeError,
    AuthenticationError,
    APIError,
    ValidationError,
    NotFoundError,
)


class TestConfiguration:
    """Tests for Configuration class."""
    
    def test_default_configuration(self):
        """Test default configuration values."""
        config = Configuration(api_key="test-key")
        
        assert config.api_key == "test-key"
        assert config.base_url == Configuration.DEFAULT_BASE_URL
        assert config.timeout == 30
        assert config.verify_ssl is True
        assert config.debug is False
    
    def test_sandbox_configuration(self):
        """Test sandbox configuration."""
        config = Configuration.sandbox(api_key="test-key")
        
        assert config.base_url == Configuration.SANDBOX_BASE_URL
    
    def test_production_configuration(self):
        """Test production configuration."""
        config = Configuration.production(api_key="test-key")
        
        assert config.base_url == Configuration.DEFAULT_BASE_URL
    
    def test_custom_base_url(self):
        """Test custom base URL."""
        config = Configuration(
            api_key="test-key",
            base_url="https://custom.api.com",
        )
        
        assert config.base_url == "https://custom.api.com"
    
    def test_trailing_slash_removal(self):
        """Test that trailing slashes are removed from base URL."""
        config = Configuration(
            api_key="test-key",
            base_url="https://api.example.com/",
        )
        
        assert config.base_url == "https://api.example.com"
    
    def test_auth_headers(self):
        """Test authentication headers generation."""
        config = Configuration(api_key="my-api-key")
        headers = config.get_auth_headers()
        
        assert headers["Authorization"] == "Bearer my-api-key"
        assert headers["Content-Type"] == "application/json"
        assert headers["Accept"] == "application/json"
    
    def test_auth_headers_without_key_raises_error(self):
        """Test that missing API key raises ValueError."""
        config = Configuration()
        
        with pytest.raises(ValueError, match="API key is not configured"):
            config.get_auth_headers()
    
    def test_environment_variable_api_key(self):
        """Test reading API key from environment variable."""
        os.environ["UNIBEE_API_KEY"] = "env-api-key"
        try:
            config = Configuration()
            assert config.api_key == "env-api-key"
        finally:
            del os.environ["UNIBEE_API_KEY"]


class TestUniBeeClient:
    """Tests for UniBeeClient class."""
    
    def test_client_initialization(self):
        """Test client initialization with API key."""
        client = UniBeeClient(api_key="test-key")
        
        assert client.config.api_key == "test-key"
        assert client.config.base_url == Configuration.DEFAULT_BASE_URL
    
    def test_client_sandbox(self):
        """Test sandbox client creation."""
        client = UniBeeClient.sandbox(api_key="test-key")
        
        assert client.config.base_url == Configuration.SANDBOX_BASE_URL
    
    def test_client_production(self):
        """Test production client creation."""
        client = UniBeeClient.production(api_key="test-key")
        
        assert client.config.base_url == Configuration.DEFAULT_BASE_URL
    
    def test_client_has_all_resources(self):
        """Test that client has all API resources."""
        client = UniBeeClient(api_key="test-key")
        
        assert hasattr(client, "subscriptions")
        assert hasattr(client, "plans")
        assert hasattr(client, "invoices")
        assert hasattr(client, "payments")
        assert hasattr(client, "users")
        assert hasattr(client, "webhooks")
        assert hasattr(client, "merchants")
        assert hasattr(client, "discounts")
        assert hasattr(client, "products")
        assert hasattr(client, "gateways")
        assert hasattr(client, "checkout")
        assert hasattr(client, "credit")
    
    def test_client_repr(self):
        """Test client string representation."""
        client = UniBeeClient(api_key="test-key")
        
        assert "UniBeeClient" in repr(client)
        assert "api.unibee.dev" in repr(client)


class TestVersion:
    """Tests for version."""
    
    def test_version_exists(self):
        """Test that version is defined."""
        assert __version__ is not None
        assert isinstance(__version__, str)
    
    def test_version_format(self):
        """Test version format (semver)."""
        parts = __version__.split(".")
        assert len(parts) >= 2
        assert all(p.isdigit() for p in parts[:2])


class TestExceptions:
    """Tests for exception classes."""
    
    def test_unibee_error(self):
        """Test UniBeeError exception."""
        error = UniBeeError("Test error", code=123, request_id="req-123")
        
        assert str(error) == "Test error (code: 123) [request_id: req-123]"
        assert error.code == 123
        assert error.request_id == "req-123"
    
    def test_authentication_error(self):
        """Test AuthenticationError exception."""
        error = AuthenticationError("Auth failed")
        
        assert isinstance(error, UniBeeError)
        assert "Auth failed" in str(error)
    
    def test_api_error(self):
        """Test APIError exception."""
        error = APIError("API error", http_status=400)
        
        assert isinstance(error, UniBeeError)
        assert error.http_status == 400
    
    def test_validation_error(self):
        """Test ValidationError exception."""
        error = ValidationError(
            "Validation failed",
            errors={"field": "required"},
        )
        
        assert isinstance(error, UniBeeError)
        assert error.errors == {"field": "required"}
    
    def test_not_found_error(self):
        """Test NotFoundError exception."""
        error = NotFoundError("Resource not found")
        
        assert isinstance(error, UniBeeError)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
