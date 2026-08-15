
# SaaS Backend API

Production-style backend with FastAPI, PostgreSQL, Redis, Celery, Stripe, JWT Auth, Rate Limiting, Caching, Logging, and Testing.

## Features
- JWT Authentication
- Stripe Payments
- Background Jobs (Celery)
- Redis Caching
- Rate Limiting
- Logging
- Pytest Testing
- Docker Support

## Setup
1. Clone the repo.
2. Create `.env` from `.env.example` and fill in your credentials (Neon, Redis Cloud, Stripe).
3. Install dependencies: `pip install -r requirements.txt`
4. Run server: `uvicorn app.main:app --reload`
5. Run Celery worker: `celery -A app.core.celery_app.celery_app worker --loglevel=info --pool=solo`

## Test
`pytest`

## Deploy to Render
- Push to GitHub.
- Create a new Web Service on Render pointing to this repo.
- Set environment variables.
- For Celery, create a Background Worker with the same repo and command: `celery -A app.core.celery_app.celery_app worker --loglevel=info --pool=solo`.
9. Run the Application Locally
Start FastAPI server
Make sure your virtual environment is activated, then:

powershell
uvicorn app.main:app --reload
You should see output indicating the server is running at http://127.0.0.1:8000.

Start Celery worker (in a new PowerShell, same folder, venv activated)
powershell
.\venv\Scripts\Activate.ps1
celery -A app.core.celery_app.celery_app worker --loglevel=info --pool=solo
Open API Docs
Visit http://localhost:8000/docs to interact with your API.


