#!/usr/bin/env python3
"""
UniBee Python SDK - Basic Usage Example

This script demonstrates basic usage of the UniBee Python SDK.

Before running, set your API key:
    export UNIBEE_API_KEY="your-api-key"

Or for sandbox testing:
    export UNIBEE_API_KEY="your-sandbox-api-key"
    export UNIBEE_BASE_URL="https://api-sandbox.unibee.top"
"""

import os
import sys
from pprint import pprint

# Add parent directory to path for development
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from unibee import UniBeeClient
from unibee.exceptions import UniBeeError, AuthenticationError


def main():
    """Main example function."""
    
    # Initialize the client
    # Uses UNIBEE_API_KEY environment variable by default
    api_key = os.environ.get("UNIBEE_API_KEY")
    if not api_key:
        print("Error: Please set UNIBEE_API_KEY environment variable")
        print("  export UNIBEE_API_KEY='your-api-key'")
        sys.exit(1)
    
    # Create client (use sandbox() for testing)
    client = UniBeeClient(api_key=api_key)
    # Or: client = UniBeeClient.sandbox(api_key=api_key)
    
    print(f"Connected to: {client.config.base_url}")
    print("-" * 50)
    
    try:
        # Get merchant profile
        print("\n1. Getting merchant profile...")
        profile = client.merchants.get_profile()
        merchant = profile.get("merchant", {})
        print(f"   Merchant: {merchant.get('companyName', 'N/A')}")
        
        # List users
        print("\n2. Listing users...")
        users_response = client.users.list(count=5)
        users = users_response.get("users", [])
        print(f"   Found {len(users)} users (showing first 5)")
        for user in users[:5]:
            print(f"   - {user.get('email')} (ID: {user.get('id')})")
        
        # List plans
        print("\n3. Listing plans...")
        plans_response = client.plans.list(count=5)
        plans = plans_response.get("plans", [])
        print(f"   Found {len(plans)} plans (showing first 5)")
        for plan in plans[:5]:
            amount = plan.get("amount", 0) / 100  # Convert from cents
            currency = plan.get("currency", "USD")
            print(f"   - {plan.get('planName')} - {currency} {amount:.2f}")
        
        # List subscriptions
        print("\n4. Listing active subscriptions...")
        subs_response = client.subscriptions.list(status=[2], count=5)  # status 2 = Active
        subscriptions = subs_response.get("subscriptions", [])
        print(f"   Found {len(subscriptions)} active subscriptions (showing first 5)")
        for sub in subscriptions[:5]:
            print(f"   - {sub.get('subscriptionId')} (User: {sub.get('userId')})")
        
        # List invoices
        print("\n5. Listing recent invoices...")
        invoices_response = client.invoices.list(count=5)
        invoices = invoices_response.get("invoices", [])
        print(f"   Found {len(invoices)} invoices (showing first 5)")
        for inv in invoices[:5]:
            amount = inv.get("totalAmount", 0) / 100
            currency = inv.get("currency", "USD")
            status = inv.get("status")
            print(f"   - {inv.get('invoiceId')} - {currency} {amount:.2f} (Status: {status})")
        
        # List webhooks
        print("\n6. Listing webhook endpoints...")
        webhooks_response = client.webhooks.list_endpoints()
        endpoints = webhooks_response.get("endpointList", [])
        print(f"   Found {len(endpoints)} webhook endpoints")
        for ep in endpoints:
            print(f"   - {ep.get('url')}")
        
        print("\n" + "-" * 50)
        print("Example completed successfully!")
        
    except AuthenticationError as e:
        print(f"\nAuthentication Error: {e}")
        print("Please check your API key.")
        sys.exit(1)
    except UniBeeError as e:
        print(f"\nAPI Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
