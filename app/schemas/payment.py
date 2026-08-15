from pydantic import BaseModel

class CheckoutSessionRequest(BaseModel):
    amount: int
    currency: str = "usd"

class CheckoutSessionResponse(BaseModel):
    checkout_url: str
