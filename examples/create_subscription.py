#!/usr/bin/env python3
"""
UniBee Python SDK - Create Subscription Example

This script demonstrates how to create a subscription for a user.

Before running, set your API key:
    export UNIBEE_API_KEY="your-api-key"
"""

import os
import sys
from pprint import pprint

# Add parent directory to path for development
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from unibee import UniBeeClient
from unibee.exceptions import UniBeeError, ValidationError


def main():
    """Create subscription example."""
    
    api_key = os.environ.get("UNIBEE_API_KEY")
    if not api_key:
        print("Error: Please set UNIBEE_API_KEY environment variable")
        sys.exit(1)
    
    # Use sandbox for testing
    client = UniBeeClient.sandbox(api_key=api_key)
    print(f"Using: {client.config.base_url}")
    
    try:
        # Step 1: Get or create a user
        print("\n1. Getting/creating user...")
        email = "test-customer@example.com"
        
        try:
            user_response = client.users.get(email=email)
            user = user_response.get("user")
            print(f"   Found existing user: {user.get('id')}")
        except UniBeeError:
            # Create new user
            user_response = client.users.create(
                email=email,
                first_name="Test",
                last_name="Customer",
            )
            user = user_response.get("user")
            print(f"   Created new user: {user.get('id')}")
        
        user_id = user.get("id")
        
        # Step 2: List available plans
        print("\n2. Available plans:")
        plans_response = client.plans.list(status=[2])  # Active plans
        plans = plans_response.get("plans", [])
        
        if not plans:
            print("   No active plans found. Please create a plan first.")
            sys.exit(1)
        
        for i, plan in enumerate(plans[:5], 1):
            amount = plan.get("amount", 0) / 100
            currency = plan.get("currency", "USD")
            interval = plan.get("intervalUnit", "month")
            print(f"   {i}. {plan.get('planName')} - {currency} {amount:.2f}/{interval}")
        
        # Use first plan for demo
        plan = plans[0]
        plan_id = plan.get("id")
        print(f"\n   Using plan: {plan.get('planName')} (ID: {plan_id})")
        
        # Step 3: Preview the subscription
        print("\n3. Subscription preview:")
        preview = client.subscriptions.create_preview(
            plan_id=plan_id,
            user_id=user_id,
            quantity=1,
        )
        
        total = preview.get("totalAmount", 0) / 100
        currency = preview.get("currency", "USD")
        print(f"   Total amount: {currency} {total:.2f}")
        
        # Step 4: Create the subscription
        print("\n4. Creating subscription...")
        
        # Note: In a real scenario, you'd get gateway_id from client.gateways.list()
        gateways = client.gateways.list()
        gateway_list = gateways.get("gateways", [])
        
        if not gateway_list:
            print("   No payment gateways configured.")
            print("   Please configure a gateway in UniBee admin panel.")
            sys.exit(1)
        
        gateway_id = gateway_list[0].get("gatewayId")
        
        result = client.subscriptions.create(
            plan_id=plan_id,
            user_id=user_id,
            gateway_id=gateway_id,
            quantity=1,
            return_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
        )
        
        print("\n   Subscription created!")
        print(f"   Subscription ID: {result.get('subscription', {}).get('subscriptionId')}")
        
        # Check if payment is needed
        payment_link = result.get("link")
        if payment_link:
            print(f"\n   Payment required. Redirect user to:")
            print(f"   {payment_link}")
        else:
            print("\n   Subscription is active (no payment required)")
        
    except ValidationError as e:
        print(f"\nValidation Error: {e}")
        sys.exit(1)
    except UniBeeError as e:
        print(f"\nAPI Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
