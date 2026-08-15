from pydantic import BaseModel

class CheckoutSessionRequest(BaseModel):
    amount: int  # in cents
    currency: str = "usd"

class CheckoutSessionResponse(BaseModel):
    checkout_url: str