import stripe
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.models.payment import Payment
from app.schemas.payment import CheckoutSessionRequest, CheckoutSessionResponse
from app.core.config import settings
from sqlalchemy import select

router = APIRouter()
stripe.api_key = settings.STRIPE_SECRET_KEY

@router.post("/create-checkout-session", response_model=CheckoutSessionResponse)
async def create_checkout_session(
    request: CheckoutSessionRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": request.currency,
                    "product_data": {
                        "name": "SaaS Subscription",
                    },
                    "unit_amount": request.amount,
                },
                "quantity": 1,
            }],
            mode="payment",
            success_url="https://yourdomain.com/success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url="https://yourdomain.com/cancel",
            metadata={"user_id": str(current_user.id)}
        )
        payment = Payment(
            user_id=current_user.id,
            stripe_session_id=session.id,
            amount=request.amount,
            currency=request.currency,
            status="pending"
        )
        db.add(payment)
        await db.commit()
        return {"checkout_url": session.url}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/webhook")
async def stripe_webhook(request: Request, db: AsyncSession = Depends(get_db)):
    payload = await request.body()
    sig_header = request.headers.get("Stripe-Signature")
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError as e:
        raise HTTPException(status_code=400, detail="Invalid signature")

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        result = await db.execute(
            select(Payment).where(Payment.stripe_session_id == session["id"])
        )
        payment = result.scalar_one_or_none()
        if payment:
            payment.status = "paid"
            await db.commit()
    return {"received": True}
