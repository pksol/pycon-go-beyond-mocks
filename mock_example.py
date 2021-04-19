import os

import stripe  # a popular payment processing provider

stripe.api_key = os.environ.get('STRIPE_API_KEY')


def charge_customer(payment_method, items_bought, item_price):
    amount = items_bought * item_price
    stripe.Charge.create(
        amount=amount,
        currency="usd",
        source=payment_method)
