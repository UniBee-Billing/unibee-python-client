#!/usr/bin/env python3
"""
UniBee SDK Basic Usage Examples

This script demonstrates common operations with the UniBee Python SDK.
Make sure to set your API key before running.

Usage:
    export UNIBEE_API_KEY="your_api_key_here"
    python basic_usage.py
"""

import os
import sys

# Add parent directory to path for local development
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from unibee import UniBeeClient, UniBeeError


def main():
    # Get API key from environment variable
    api_key = os.environ.get("UNIBEE_API_KEY")
    if not api_key:
        print("Error: Please set UNIBEE_API_KEY environment variable")
        print("  export UNIBEE_API_KEY='your_api_key_here'")
        sys.exit(1)
    
    # Use sandbox for testing
    use_sandbox = os.environ.get("UNIBEE_SANDBOX", "true").lower() == "true"
    
    # Initialize the client
    client = UniBeeClient(
        api_key=api_key,
        base_url=(
            "https://api-sandbox.unibee.top" if use_sandbox 
            else "https://api.unibee.dev"
        ),
        debug=os.environ.get("UNIBEE_DEBUG", "false").lower() == "true"
    )
    
    print(f"Connected to: {client._base_url}")
    print("-" * 50)
    
    try:
        # Example 1: List Plans
        print("\n📋 Listing Plans...")
        plans = client.plan.list(count=5)
        if hasattr(plans, 'plans') and plans.plans:
            for plan in plans.plans:
                print(f"  - {plan.plan_name}: ${plan.amount/100:.2f}/{plan.interval_unit}")
        else:
            print("  No plans found. Create some plans in the dashboard first.")
        
        # Example 2: List Users
        print("\n👥 Listing Users...")
        users = client.user.list(count=5)
        if hasattr(users, 'users') and users.users:
            for user in users.users:
                email = getattr(user, 'email', 'N/A')
                print(f"  - {email}")
        else:
            print("  No users found.")
        
        # Example 3: List Subscriptions
        print("\n📊 Listing Subscriptions...")
        subs = client.subscription.list(count=5)
        if hasattr(subs, 'subscriptions') and subs.subscriptions:
            for sub in subs.subscriptions:
                sub_id = getattr(sub, 'subscription_id', 'N/A')
                status = getattr(sub, 'status', 'N/A')
                print(f"  - {sub_id}: status={status}")
        else:
            print("  No subscriptions found.")
        
        # Example 4: List Payment Gateways
        print("\n💳 Listing Payment Gateways...")
        gateways = client.gateway.list()
        if hasattr(gateways, 'gateways') and gateways.gateways:
            for gw in gateways.gateways:
                name = getattr(gw, 'gateway_name', 'N/A')
                print(f"  - {name}")
        else:
            print("  No gateways configured.")
        
        # Example 5: List Webhook Endpoints
        print("\n🔗 Listing Webhook Endpoints...")
        endpoints = client.webhook.list_endpoints()
        if hasattr(endpoints, 'endpoints') and endpoints.endpoints:
            for ep in endpoints.endpoints:
                url = getattr(ep, 'url', 'N/A')
                print(f"  - {url}")
        else:
            print("  No webhook endpoints configured.")
        
        print("\n" + "-" * 50)
        print("✅ All examples completed successfully!")
        
    except UniBeeError as e:
        print(f"\n❌ Error: {e}")
        if hasattr(e, 'status_code'):
            print(f"   Status Code: {e.status_code}")
        if hasattr(e, 'request_id'):
            print(f"   Request ID: {e.request_id}")
        sys.exit(1)


if __name__ == "__main__":
    main()
