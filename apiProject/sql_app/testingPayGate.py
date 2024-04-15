import paygate

# Replace with your actual PayGate merchant ID and API key
merchant_id = "YOUR_MERCHANT_ID"
api_key = "YOUR_API_KEY"

# Create a PayGate client instance
paygate_client = paygate.Client(merchant_id, api_key)

# Create a transaction object
transaction = {
    "amount": 100.00,  # Transaction amount in the specified currency
    "currency": "USD",  # Transaction currency (e.g., USD, EUR, CAD)
    "reference": "ORDER-12345",  # Unique reference identifier for the transaction
    "customer": {
        "email": "customer@example.com",  # Customer's email address
        "phone": "+1234567890",  # Customer's phone number (optional)
    },
    "payment_methods": ["card"],  # Accepted payment methods (e.g., card, mobile_money)
}

# Create a payment request
payment_request = paygate_client.create_payment_request(transaction)

# Get the payment URL
payment_url = payment_request["payment_url"]

# Redirect the user to the PayGate payment page
redirect(payment_url)

# Process the payment response
payment_response = paygate_client.get_payment_response(transaction["reference"])

# Check if the payment was successful
if payment_response["status"] == "success":
    # Process the successful payment
    print("Payment successful!")

    # Update the order status in your e-commerce system
    update_order_status(transaction["reference"], "paid")
else:
    # Handle payment failure
    print("Payment failed:", payment_response["error"])
