import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_register_and_login(client: AsyncClient):
    register_data = {
        "email": "test@example.com",
        "full_name": "Test User",
        "password": "password123"
    }
    response = await client.post("/api/v1/auth/register", json=register_data)
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"

    login_data = {
        "email": "test@example.com",
        "password": "password123"
    }
    response = await client.post("/api/v1/auth/login", json=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()