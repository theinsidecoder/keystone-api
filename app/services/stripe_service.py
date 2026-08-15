import stripe
from app.core.config import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

class StripeService:
    @staticmethod
    def create_customer(email: str) -> str:
        customer = stripe.Customer.create(email=email)
        return customer.id

    @staticmethod
    def create_checkout_session(customer_id: str, success_url: str, cancel_url: str):
        return stripe.checkout.Session.create(
            customer=customer_id,
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": "Premium SaaS Subscription"},
                    "unit_amount": 1999, # $19.99
                    "recurring": {"interval": "month"},
                },
                "quantity": 1,
            }],
            mode="subscription",
            success_url=success_url,
            cancel_url=cancel_url,
        )
