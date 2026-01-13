# UniBee Python SDK

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A Python SDK for interacting with the [UniBee](https://unibee.dev) billing API. UniBee is an open-source billing solution for SaaS businesses, providing subscription management, invoicing, payment processing, and more.

## Features

- 🚀 Simple, intuitive API
- 🔐 Bearer token authentication
- 📦 Full API coverage for subscriptions, plans, invoices, payments, users, webhooks, and more
- 🧪 Sandbox environment support for testing
- 📝 Type hints for better IDE support
- 🔧 Minimal dependencies

## Installation

### From GitHub (recommended for now)

```bash
pip install git+https://github.com/UniBee-Billing/unibee-python-client.git
```

### From source

```bash
git clone https://github.com/UniBee-Billing/unibee-python-client.git
cd unibee-python-client
pip install -e .
```

## Quick Start

### Initialize the Client

```python
from unibee import UniBeeClient

# Initialize with API key
client = UniBeeClient(api_key="your-api-key")

# Or use environment variable UNIBEE_API_KEY
import os
os.environ["UNIBEE_API_KEY"] = "your-api-key"
client = UniBeeClient()

# Use sandbox environment for testing
client = UniBeeClient.sandbox(api_key="your-sandbox-api-key")
```

### Basic Examples

#### List Users

```python
# List all users
users = client.users.list()
print(f"Found {len(users.get('users', []))} users")

# Get a specific user
user = client.users.get(user_id=123)
print(f"User email: {user.get('user', {}).get('email')}")

# Create a new user
new_user = client.users.create(
    email="customer@example.com",
    first_name="John",
    last_name="Doe",
)
```

#### Manage Plans

```python
# List all plans
plans = client.plans.list()

# Get plan details
plan = client.plans.get(plan_id=123)

# Create a new plan
plan = client.plans.create(
    plan_name="Pro Plan",
    amount=1999,  # $19.99 in cents
    currency="USD",
    interval_unit="month",
    interval_count=1,
    description="Professional tier with advanced features",
)

# Activate the plan
client.plans.activate(plan_id=plan["plan"]["id"])

# Publish the plan (make visible to users)
client.plans.publish(plan_id=plan["plan"]["id"])
```

#### Manage Subscriptions

```python
# List all subscriptions
subscriptions = client.subscriptions.list()

# Get subscription details
subscription = client.subscriptions.get(subscription_id="sub_123")

# Create a subscription preview (calculate amounts)
preview = client.subscriptions.create_preview(
    plan_id=123,
    user_id=456,
    quantity=1,
)
print(f"Total amount: {preview.get('totalAmount')}")

# Create a subscription
result = client.subscriptions.create(
    plan_id=123,
    user_id=456,
    gateway_id=1,
    return_url="https://yoursite.com/success",
    cancel_url="https://yoursite.com/cancel",
)

# If payment is required, redirect user to the payment link
payment_link = result.get("link")
if payment_link:
    print(f"Redirect user to: {payment_link}")

# Cancel at period end
client.subscriptions.cancel_at_period_end(subscription_id="sub_123")

# Cancel immediately
client.subscriptions.cancel(subscription_id="sub_123")
```

#### Handle Invoices

```python
# List invoices
invoices = client.invoices.list(user_id=123)

# Get invoice details
invoice = client.invoices.get(invoice_id="inv_123")

# Create a custom invoice
invoice = client.invoices.create(
    user_id=123,
    currency="USD",
    lines=[
        {"description": "Consulting Services", "amount": 10000, "quantity": 1},
        {"description": "Support Hours", "amount": 5000, "quantity": 2},
    ],
)

# Finalize and send
client.invoices.finish(invoice_id=invoice["invoice"]["invoiceId"])
client.invoices.send_email(invoice_id=invoice["invoice"]["invoiceId"])

# Refund an invoice
client.invoices.refund(
    invoice_id="inv_123",
    refund_amount=5000,
    reason="Customer request",
)
```

#### Create Checkout Sessions

```python
# Create a checkout session for subscription
session = client.checkout.create_session(
    plan_id=123,
    success_url="https://yoursite.com/success",
    cancel_url="https://yoursite.com/cancel",
    email="customer@example.com",
)

# Redirect user to checkout
checkout_url = session.get("url")
print(f"Checkout URL: {checkout_url}")
```

#### Manage Webhooks

```python
# List webhook endpoints
endpoints = client.webhooks.list_endpoints()

# Create a webhook endpoint
endpoint = client.webhooks.create_endpoint(
    url="https://yoursite.com/webhooks/unibee",
    events=["subscription.created", "subscription.cancelled", "invoice.paid"],
)

# List available event types
events = client.webhooks.list_events()
```

#### Apply Discount Codes

```python
# Create a discount code
discount = client.discounts.create(
    code="SUMMER20",
    name="Summer Sale - 20% Off",
    discount_type=1,  # 1=Percentage, 2=Fixed Amount
    discount_amount=20,  # 20%
    billing_type=2,  # 1=OneTime, 2=Recurring
    cycle_limit=3,  # Apply for 3 billing cycles
)

# Activate the discount
client.discounts.activate(discount_id=discount["discount"]["id"])

# Apply to a subscription
result = client.subscriptions.create(
    plan_id=123,
    user_id=456,
    discount_code="SUMMER20",
    gateway_id=1,
)
```

## Error Handling

The SDK provides specific exception classes for different error types:

```python
from unibee import UniBeeClient
from unibee.exceptions import (
    AuthenticationError,
    ValidationError,
    NotFoundError,
    RateLimitError,
    APIError,
)

client = UniBeeClient(api_key="your-api-key")

try:
    subscription = client.subscriptions.get(subscription_id="invalid_id")
except AuthenticationError as e:
    print(f"Authentication failed: {e}")
except NotFoundError as e:
    print(f"Resource not found: {e}")
except ValidationError as e:
    print(f"Validation error: {e}")
except RateLimitError as e:
    print(f"Rate limit exceeded. Retry after {e.retry_after} seconds")
except APIError as e:
    print(f"API error: {e}")
```

## Configuration

### Environment Variables

The SDK supports configuration via environment variables:

- `UNIBEE_API_KEY`: API key for authentication
- `UNIBEE_BASE_URL`: Base URL for the API (optional)

### Configuration Options

```python
client = UniBeeClient(
    api_key="your-api-key",
    base_url="https://api.unibee.dev",  # Production (default)
    timeout=30,  # Request timeout in seconds
    debug=False,  # Enable debug logging
)
```

### Environments

| Environment | Base URL |
|-------------|----------|
| Production | `https://api.unibee.dev` |
| Sandbox | `https://api-sandbox.unibee.top` |

## API Reference

### Available Resources

| Resource | Description |
|----------|-------------|
| `client.subscriptions` | Manage subscriptions |
| `client.plans` | Manage subscription plans |
| `client.invoices` | Manage invoices |
| `client.payments` | Manage payments and payment methods |
| `client.users` | Manage users (customers) |
| `client.webhooks` | Manage webhook endpoints |
| `client.merchants` | Manage merchant profile |
| `client.discounts` | Manage discount codes |
| `client.products` | Manage products |
| `client.gateways` | Manage payment gateways |
| `client.checkout` | Manage checkout sessions |
| `client.credit` | Manage credits and promo credits |

For detailed API documentation, visit [docs.unibee.dev](https://docs.unibee.dev/).

## Requirements

- Python 3.8+
- urllib3 >= 1.25.3

## Legacy API Client

The legacy auto-generated API client is still available in the `openapi_client` package for backwards compatibility, but we recommend using the new `unibee` package for a better developer experience.

## Contributing

We welcome contributions! Please see our [GitHub repository](https://github.com/UniBee-Billing/unibee-python-client) for more information.

## Support

- **Documentation**: [docs.unibee.dev](https://docs.unibee.dev/)
- **GitHub Issues**: [Report a bug](https://github.com/UniBee-Billing/unibee-python-client/issues)
- **Contact**: [unibee.dev/contact](https://unibee.dev/contact)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
