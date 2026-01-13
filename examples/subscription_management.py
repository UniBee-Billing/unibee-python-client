#!/usr/bin/env python3
"""
UniBee SDK - Subscription Management Examples

This script demonstrates subscription lifecycle management with the UniBee SDK.

Usage:
    export UNIBEE_API_KEY="your_api_key_here"
    python subscription_management.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from unibee import UniBeeClient, UniBeeError, UniBeeNotFoundError


def main():
    api_key = os.environ.get("UNIBEE_API_KEY")
    if not api_key:
        print("Error: Please set UNIBEE_API_KEY environment variable")
        sys.exit(1)
    
    client = UniBeeClient(
        api_key=api_key,
        base_url="https://api-sandbox.unibee.top"  # Use sandbox for testing
    )
    
    print("UniBee Subscription Management Examples")
    print("=" * 50)
    
    # =========================================================================
    # 1. List and Filter Subscriptions
    # =========================================================================
    print("\n1️⃣ Listing Subscriptions")
    
    # Get all subscriptions
    all_subs = client.subscription.list()
    print(f"   Total subscriptions: {getattr(all_subs, 'total', 0)}")
    
    # Filter by status (2 = active)
    active_subs = client.subscription.list(status=[2])
    print(f"   Active subscriptions: {getattr(active_subs, 'total', 0)}")
    
    # =========================================================================
    # 2. Get Subscription Details
    # =========================================================================
    print("\n2️⃣ Getting Subscription Details")
    
    if hasattr(all_subs, 'subscriptions') and all_subs.subscriptions:
        sub = all_subs.subscriptions[0]
        sub_id = getattr(sub, 'subscription_id', None)
        if sub_id:
            try:
                details = client.subscription.get(subscription_id=sub_id)
                print(f"   Subscription ID: {sub_id}")
                print(f"   Status: {getattr(details, 'status', 'N/A')}")
                print(f"   Plan: {getattr(details.plan, 'plan_name', 'N/A') if details.plan else 'N/A'}")
            except UniBeeNotFoundError:
                print(f"   Subscription {sub_id} not found")
    else:
        print("   No subscriptions to show")
    
    # =========================================================================
    # 3. Preview Subscription Creation (without creating)
    # =========================================================================
    print("\n3️⃣ Preview Subscription Creation")
    
    # First, get available plans and users
    plans = client.plan.list(count=1, status=[2])  # Active plans
    users = client.user.list(count=1)
    gateways = client.gateway.list()
    
    if (hasattr(plans, 'plans') and plans.plans and 
        hasattr(users, 'users') and users.users and
        hasattr(gateways, 'gateways') and gateways.gateways):
        
        plan = plans.plans[0]
        user = users.users[0]
        gateway = gateways.gateways[0]
        
        try:
            preview = client.subscription.create_preview(
                user_id=user.id,
                plan_id=plan.id,
                gateway_id=gateway.gateway_id
            )
            print(f"   Preview for: {user.email}")
            print(f"   Plan: {plan.plan_name}")
            print(f"   Total: ${getattr(preview, 'total_amount', 0)/100:.2f}")
        except UniBeeError as e:
            print(f"   Preview error: {e}")
    else:
        print("   Missing plans, users, or gateways. Set them up first.")
    
    # =========================================================================
    # 4. Subscription Configuration
    # =========================================================================
    print("\n4️⃣ Getting Subscription Configuration")
    
    try:
        config = client.subscription.get_config()
        print(f"   Config loaded: {config is not None}")
    except UniBeeError as e:
        print(f"   Config error: {e}")
    
    print("\n" + "=" * 50)
    print("✅ Examples completed!")
    print("\nNote: Full subscription creation/modification should be done")
    print("in a real environment with proper user flows.")


if __name__ == "__main__":
    main()
