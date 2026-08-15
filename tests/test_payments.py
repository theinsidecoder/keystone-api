import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_checkout_session_requires_auth(client: AsyncClient):
    response = await client.post("/api/v1/payments/create-checkout-session", json={"amount": 1000})
    assert response.status_code == 401
