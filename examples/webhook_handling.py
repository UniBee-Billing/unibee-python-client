#!/usr/bin/env python3
"""
UniBee Python SDK - Webhook Handling Example

This script demonstrates how to set up and handle webhooks.

Before running, set your API key:
    export UNIBEE_API_KEY="your-api-key"
"""

import os
import sys
import hmac
import hashlib
import json

# Add parent directory to path for development
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from unibee import UniBeeClient
from unibee.exceptions import UniBeeError


def verify_webhook_signature(payload: bytes, signature: str, secret: str) -> bool:
    """
    Verify webhook signature.
    
    Args:
        payload: Raw request body bytes
        signature: Signature from X-UniBee-Signature header
        secret: Webhook signing secret
    
    Returns:
        True if signature is valid
    """
    expected_sig = hmac.new(
        secret.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected_sig, signature)


def handle_webhook_event(event_type: str, data: dict):
    """
    Handle different webhook event types.
    
    Args:
        event_type: The type of event (e.g., "subscription.created")
        data: The event data
    """
    print(f"\nHandling event: {event_type}")
    
    if event_type == "subscription.created":
        subscription = data.get("subscription", {})
        print(f"  New subscription: {subscription.get('subscriptionId')}")
        print(f"  User ID: {subscription.get('userId')}")
        print(f"  Plan ID: {subscription.get('planId')}")
    
    elif event_type == "subscription.cancelled":
        subscription = data.get("subscription", {})
        print(f"  Cancelled subscription: {subscription.get('subscriptionId')}")
    
    elif event_type == "subscription.updated":
        subscription = data.get("subscription", {})
        print(f"  Updated subscription: {subscription.get('subscriptionId')}")
        print(f"  Status: {subscription.get('status')}")
    
    elif event_type == "invoice.paid":
        invoice = data.get("invoice", {})
        print(f"  Paid invoice: {invoice.get('invoiceId')}")
        amount = invoice.get("totalAmount", 0) / 100
        currency = invoice.get("currency", "USD")
        print(f"  Amount: {currency} {amount:.2f}")
    
    elif event_type == "invoice.created":
        invoice = data.get("invoice", {})
        print(f"  New invoice: {invoice.get('invoiceId')}")
    
    elif event_type == "payment.success":
        payment = data.get("payment", {})
        print(f"  Payment successful: {payment.get('paymentId')}")
    
    elif event_type == "payment.failed":
        payment = data.get("payment", {})
        print(f"  Payment failed: {payment.get('paymentId')}")
    
    else:
        print(f"  Unhandled event type: {event_type}")
        print(f"  Data: {json.dumps(data, indent=2)[:200]}...")


def setup_webhooks():
    """Setup webhook endpoints."""
    api_key = os.environ.get("UNIBEE_API_KEY")
    if not api_key:
        print("Error: Please set UNIBEE_API_KEY environment variable")
        sys.exit(1)
    
    client = UniBeeClient(api_key=api_key)
    
    try:
        # List existing endpoints
        print("Current webhook endpoints:")
        endpoints = client.webhooks.list_endpoints()
        for ep in endpoints.get("endpointList", []):
            print(f"  - {ep.get('url')}")
        
        # List available event types
        print("\nAvailable webhook events:")
        events = client.webhooks.list_events()
        event_list = events.get("eventList", [])
        for event in event_list[:10]:
            print(f"  - {event}")
        if len(event_list) > 10:
            print(f"  ... and {len(event_list) - 10} more")
        
        # Example: Create a new endpoint (uncomment to use)
        # print("\nCreating webhook endpoint...")
        # new_endpoint = client.webhooks.create_endpoint(
        #     url="https://your-server.com/webhooks/unibee",
        #     events=[
        #         "subscription.created",
        #         "subscription.cancelled",
        #         "subscription.updated",
        #         "invoice.paid",
        #         "invoice.created",
        #         "payment.success",
        #         "payment.failed",
        #     ],
        # )
        # print(f"Created endpoint: {new_endpoint}")
        
        # Get webhook secret for signature verification
        # secret = client.webhooks.get_secret()
        # print(f"\nWebhook secret: {secret.get('secret')}")
        
    except UniBeeError as e:
        print(f"Error: {e}")
        sys.exit(1)


def simulate_webhook_handling():
    """Simulate handling webhook events."""
    print("\n" + "=" * 50)
    print("Simulating webhook event handling")
    print("=" * 50)
    
    # Simulated webhook events
    test_events = [
        {
            "type": "subscription.created",
            "data": {
                "subscription": {
                    "subscriptionId": "sub_123",
                    "userId": 456,
                    "planId": 789,
                    "status": 2,
                }
            }
        },
        {
            "type": "invoice.paid",
            "data": {
                "invoice": {
                    "invoiceId": "inv_123",
                    "totalAmount": 1999,
                    "currency": "USD",
                    "status": 3,
                }
            }
        },
        {
            "type": "payment.success",
            "data": {
                "payment": {
                    "paymentId": "pay_123",
                    "amount": 1999,
                    "currency": "USD",
                }
            }
        },
    ]
    
    for event in test_events:
        handle_webhook_event(event["type"], event["data"])


def main():
    """Main function."""
    print("UniBee Webhook Handling Example")
    print("-" * 50)
    
    setup_webhooks()
    simulate_webhook_handling()
    
    print("\n" + "=" * 50)
    print("Flask webhook handler example:")
    print("=" * 50)
    print("""
from flask import Flask, request, jsonify

app = Flask(__name__)
WEBHOOK_SECRET = "your-webhook-secret"

@app.route('/webhooks/unibee', methods=['POST'])
def handle_unibee_webhook():
    # Verify signature
    signature = request.headers.get('X-UniBee-Signature', '')
    if not verify_webhook_signature(request.data, signature, WEBHOOK_SECRET):
        return jsonify({'error': 'Invalid signature'}), 401
    
    # Parse event
    event = request.json
    event_type = event.get('type')
    data = event.get('data', {})
    
    # Handle event
    handle_webhook_event(event_type, data)
    
    return jsonify({'received': True}), 200
""")


if __name__ == "__main__":
    main()
