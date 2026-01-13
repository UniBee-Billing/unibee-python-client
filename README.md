# UniBee Python SDK

[![PyPI version](https://badge.fury.io/py/unibee.svg)](https://badge.fury.io/py/unibee)
[![Python](https://img.shields.io/pypi/pyversions/unibee.svg)](https://pypi.org/project/unibee/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

A modern, easy-to-use Python SDK for the [UniBee](https://unibee.dev) billing API. UniBee is an open-source billing platform designed for SaaS businesses, providing subscription management, invoicing, payment processing, and more.

## Features

- 🚀 **Simple & Intuitive API** - Pythonic interface with type hints
- 🔒 **Secure Authentication** - Bearer token authentication
- 📦 **Full API Coverage** - Access to all UniBee API endpoints
- 🧪 **Sandbox Support** - Test your integration safely
- 📝 **Well Documented** - Comprehensive examples and docstrings

## Installation

```bash
pip install git+https://github.com/UniBee-Billing/unibee-python-client.git
```

Or with Poetry:

```bash
poetry add git+https://github.com/UniBee-Billing/unibee-python-client.git
```

## Quick Start

### Initialize the Client

```python
from unibee import UniBeeClient

# Production environment
client = UniBeeClient(
    api_key="your_api_key_here",
    base_url="https://api.unibee.dev"
)

# Sandbox environment (for testing)
client = UniBeeClient(
    api_key="your_sandbox_api_key",
    base_url="https://api-sandbox.unibee.top"
)
```

### Get Your API Key

1. Log in to your [UniBee Dashboard](https://app.unibee.dev)
2. Navigate to **Settings** → **API Keys**
3. Generate a new API key

### Basic Usage Examples

#### List Subscriptions

```python
# Get all subscriptions
subscriptions = client.subscription.list()
print(f"Found {len(subscriptions.subscriptions)} subscriptions")

# Filter by user
user_subs = client.subscription.list(user_id=123)

# Filter by status (2 = active)
active_subs = client.subscription.list(status=[2])
```

#### Get Subscription Details

```python
# Get subscription by ID
subscription = client.subscription.get(subscription_id="sub_abc123")
print(f"Plan: {subscription.plan.plan_name}")
print(f"Status: {subscription.status}")
print(f"Next billing: {subscription.current_period_end}")
```

#### Create a Subscription

```python
# Preview subscription before creating (check pricing)
preview = client.subscription.create_preview(
    user_id=123,
    plan_id=456,
    gateway_id=789
)
print(f"Total amount: ${preview.total_amount / 100:.2f}")

# Create the subscription
subscription = client.subscription.create(
    user_id=123,
    plan_id=456,
    gateway_id=789,
    return_url="https://yourapp.com/success",
    cancel_url="https://yourapp.com/cancel"
)

# Check if payment is required
if subscription.link:
    print(f"Redirect user to: {subscription.link}")
else:
    print("Subscription created successfully!")
```

#### Manage Subscriptions

```python
# Cancel immediately
client.subscription.cancel(subscription_id="sub_abc123")

# Cancel at period end (user keeps access until billing period ends)
client.subscription.cancel_at_period_end(subscription_id="sub_abc123")

# Revert a pending cancellation
client.subscription.revert_cancel(subscription_id="sub_abc123")

# Suspend (pause) a subscription
client.subscription.suspend(subscription_id="sub_abc123")

# Resume a suspended subscription
client.subscription.resume(subscription_id="sub_abc123")

# Change plan (upgrade/downgrade)
client.subscription.update(
    subscription_id="sub_abc123",
    new_plan_id=999
)
```

#### User Management

```python
# List users
users = client.user.list(count=50)

# Get user profile
user = client.user.get(user_id=123)
print(f"Email: {user.email}")

# Search users
results = client.user.search(email="john@example.com")

# Update user
client.user.update(
    user_id=123,
    first_name="John",
    last_name="Doe"
)
```

#### Invoice Management

```python
# List invoices
invoices = client.invoice.list(user_id=123)

# Get invoice details
invoice = client.invoice.get(invoice_id="inv_abc123")
print(f"Total: ${invoice.total_amount / 100:.2f}")
print(f"Status: {invoice.status}")

# Create custom invoice
invoice = client.invoice.create(
    user_id=123,
    currency="USD",
    name="Custom Service Fee",
    lines=[
        {"description": "Consulting Hours", "amount": 15000, "quantity": 2}
    ]
)

# Finalize and send
result = client.invoice.finish(invoice_id=invoice.invoice_id)
print(f"Payment link: {result.link}")
```

#### Plan Management

```python
# List all plans
plans = client.plan.list()

# Get plan details
plan = client.plan.get(plan_id=123)
print(f"Name: {plan.plan_name}")
print(f"Price: ${plan.amount / 100:.2f}/{plan.interval_unit}")

# Create a new plan
plan = client.plan.create(
    plan_name="Pro Monthly",
    currency="USD",
    amount=9900,  # $99.00 in cents
    interval_unit="month",
    interval_count=1
)
```

#### Webhook Management

```python
# List webhook endpoints
endpoints = client.webhook.list_endpoints()

# Create new endpoint
endpoint = client.webhook.create_endpoint(
    url="https://yourapp.com/webhooks/unibee",
    events=["subscription.created", "subscription.cancelled", "payment.success"]
)

# List available events
events = client.webhook.list_events()
```

#### User Portal Session

```python
# Create a portal session for users to manage their subscription
session = client.session.create_portal(
    user_id=123,
    return_url="https://yourapp.com/account"
)
print(f"Redirect user to: {session.url}")
```

## API Resources

The SDK provides access to the following resources:

| Resource | Description |
|----------|-------------|
| `client.subscription` | Subscription lifecycle management |
| `client.user` | User profile management |
| `client.invoice` | Invoice creation and management |
| `client.payment` | Payment processing and methods |
| `client.plan` | Subscription plan management |
| `client.product` | Product catalog management |
| `client.webhook` | Webhook endpoint management |
| `client.gateway` | Payment gateway configuration |
| `client.member` | Admin member management |
| `client.metric` | Billable metrics |
| `client.discount` | Discount code management |
| `client.session` | Checkout and portal sessions |
| `client.credit` | Promo credit management |
| `client.vat` | VAT/tax configuration |
| `client.search` | Global search |
| `client.role` | Admin role management |

## Error Handling

The SDK provides specific exception types for different error scenarios:

```python
from unibee import (
    UniBeeClient,
    UniBeeError,
    UniBeeAuthenticationError,
    UniBeeAPIError,
    UniBeeValidationError,
    UniBeeNotFoundError,
    UniBeeRateLimitError,
)

try:
    subscription = client.subscription.get(subscription_id="invalid_id")
except UniBeeNotFoundError as e:
    print(f"Subscription not found: {e}")
except UniBeeAuthenticationError as e:
    print(f"Authentication failed: {e}")
except UniBeeValidationError as e:
    print(f"Validation error: {e}")
    print(f"Details: {e.errors}")
except UniBeeRateLimitError as e:
    print(f"Rate limited. Retry after: {e.retry_after} seconds")
except UniBeeAPIError as e:
    print(f"API error ({e.status_code}): {e.message}")
except UniBeeError as e:
    print(f"General error: {e}")
```

## Advanced Configuration

### Custom Timeout

```python
client = UniBeeClient(
    api_key="your_api_key",
    timeout=60  # seconds
)
```

### Debug Mode

```python
client = UniBeeClient(
    api_key="your_api_key",
    debug=True  # Enable debug logging
)
```

### Using the Low-Level API Client

For advanced use cases, you can access the underlying OpenAPI client:

```python
# Access raw API client for custom operations
api_client = client.api_client

# Use with specific API modules
from openapi_client.api.subscription import Subscription
sub_api = Subscription(api_client)
```

## Testing

We recommend using the sandbox environment for testing:

```python
# Use sandbox for testing
client = UniBeeClient(
    api_key="your_sandbox_api_key",
    base_url="https://api-sandbox.unibee.top"
)
```

For testing cards and test scenarios, see the [UniBee Testing Guide](https://docs.unibee.dev/documentation/quick-start/testing-cards-sandbox).

## Support

- 📖 [Documentation](https://docs.unibee.dev/documentation)
- 🐛 [Issue Tracker](https://github.com/UniBee-Billing/unibee-python-client/issues)
- 💬 [Discord Community](https://discord.gg/unibee)
- 📧 [Email Support](mailto:support@unibee.dev)

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

This SDK is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.

---

Built with ❤️ by the [UniBee Team](https://unibee.dev)
