

<div align="center">
  <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=200&h=200&fit=crop&crop=faces" width="120" height="120" style="border-radius:50%"/>
  <h1>⚡ SaaS Backend API</h1>
  <p><em>Production-grade backend for modern SaaS applications — built with FastAPI, PostgreSQL, Redis, Celery, and Stripe.</em></p>
  
  [![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
  [![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
  [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org)
  [![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io)
  [![Celery](https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white)](https://docs.celeryq.dev)
  [![Stripe](https://img.shields.io/badge/Stripe-008CDD?style=for-the-badge&logo=stripe&logoColor=white)](https://stripe.com)
  [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
  [![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
  [![Live Demo](https://img.shields.io/badge/Live%20Demo-PythonAnywhere-1f425f?style=for-the-badge)](https://theinsidecoder.pythonanywhere.com/docs)
</div>

---

## 📖 Table of Contents

- [Why This Project?](#-why-this-project)
- [✨ Features](#-features)
- [🧠 Architecture](#-architecture)
- [🛠 Tech Stack](#-tech-stack)
- [📁 Project Structure](#-project-structure)
- [🚀 Quick Start](#-quick-start)
- [🔐 Environment Variables](#-environment-variables)
- [📡 API Reference](#-api-reference)
- [💳 Payment Flow](#-payment-flow)
- [⚙️ Background Tasks](#-background-tasks)
- [🧠 Caching & Rate Limiting](#-caching--rate-limiting)
- [📊 Monitoring & Logging](#-monitoring--logging)
- [🧪 Testing](#-testing)
- [🌍 Deployment](#-deployment)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [🙏 Acknowledgements](#-acknowledgements)
- [👨‍💻 About the Developer](#-about-the-developer)

---

## 🎯 Why This Project?

Most tutorials stop at "Hello World" or a single endpoint. This project is different. It's a **complete, production-ready SaaS backend** that implements the core building blocks every real-world subscription product needs — authentication, payments, background processing, caching, rate limiting, and robust testing.

I built this to serve as a **reference architecture** for developers who want to launch a SaaS without reinventing the wheel. It's designed with clean separation of concerns, async SQLAlchemy, and best practices gleaned from real production systems.

**Key design principles:**
- ✅ **Scalable by default** — modular components can be swapped or extended.
- ✅ **Developer-friendly** — interactive Swagger docs, easy setup, sensible defaults.
- ✅ **Production-grade** — Dockerized, with structured logging and comprehensive tests.
- ✅ **Zero-cost to start** — works with SQLite and in-memory fallbacks for local dev.

---

## ✨ Features

| Category | Feature | Description |
|----------|---------|-------------|
| 🔐 **Security** | JWT Authentication | Secure token-based auth with bcrypt password hashing |
| | Role Management | Superuser flag for future admin capabilities |
| 💳 **Payments** | Stripe Checkout | Create checkout sessions and handle webhooks |
| | Payment Tracking | Store payment records with status updates |
| ⚙️ **Background Jobs** | Celery Tasks | Asynchronous task processing (e.g., welcome emails) |
| | Memory Broker Fallback | Run locally without Redis |
| 🧠 **Caching** | Redis Integration | Cache user profiles for 60 seconds |
| | In-Memory Fallback | Works out-of-the-box for development |
| 🚦 **Rate Limiting** | IP-based Limits | Protect endpoints from abuse (5 req/min on root) |
| 📝 **Logging** | Console & File | Structured logs with configurable levels |
| 🧪 **Testing** | Pytest Suite | 3+ tests covering auth, health, and payments |
| 🐳 **Deployment** | Dockerfile | Ready for containerized deployment |
| | PythonAnywhere Ready | Free tier compatible |

---

## 🧠 Architecture

The backend follows a **layered architecture** with clear separation of concerns:

```mermaid
graph TB
    Client[Client / Browser] -->|HTTP Requests| API[FastAPI App]
    API --> Auth[Authentication Middleware]
    API --> Rate[Rate Limiter]
    API --> Routes[API Router v1]
    Routes --> AuthEnd[Auth Endpoints]
    Routes --> UserEnd[User Endpoints]
    Routes --> PayEnd[Payment Endpoints]
    Routes --> TaskEnd[Task Endpoints]
    Routes --> HealthEnd[Health Endpoints]
    AuthEnd --> Service[Service Layer]
    UserEnd --> Service
    PayEnd --> Service
    TaskEnd --> Service
    Service --> DB[(PostgreSQL / SQLite)]
    Service --> Cache[(Redis / In-Memory)]
    Service --> Celery[Celery Worker]
    Celery --> Broker[Message Broker]
    Celery --> Cache
    PayEnd --> Stripe[Stripe API]
    Stripe --> Webhook[Webhook Handler]
```

---

## 🛠 Tech Stack

| Layer | Technology | Why |
|-------|------------|-----|
| **API Framework** | FastAPI | Async, auto docs, high performance |
| **Database** | PostgreSQL (SQLite for dev) | Reliable, production-proven |
| **ORM** | SQLAlchemy 2.0 (async) | Async support, modern API |
| **Caching** | Redis | High-speed in-memory store |
| **Background Jobs** | Celery | Distributed task queue |
| **Authentication** | python-jose, bcrypt | JWT standard, secure hashing |
| **Payments** | Stripe | Industry-leading payment processor |
| **Rate Limiting** | slowapi | Simple IP-based limiting |
| **Logging** | Python logging | Built-in, no dependencies |
| **Testing** | pytest, httpx | Standard testing stack |
| **Containerization** | Docker | Easy deployment anywhere |

---

## 📁 Project Structure

```
back-end-APIs-system/
├── app/
│   ├── __init__.py
│   ├── main.py                  # FastAPI app entry
│   ├── core/
│   │   ├── config.py            # Pydantic settings
│   │   ├── security.py          # JWT & password utilities
│   │   ├── logging.py           # Logging setup
│   │   ├── cache.py             # Redis/in-memory cache
│   │   └── celery_app.py        # Celery instance
│   ├── db/
│   │   ├── base.py              # Declarative base
│   │   ├── session.py           # Async DB session
│   │   └── init_db.py           # Table creation
│   ├── models/
│   │   ├── user.py              # User model
│   │   └── payment.py           # Payment model
│   ├── schemas/
│   │   ├── user.py              # Pydantic schemas
│   │   └── payment.py
│   ├── api/
│   │   ├── deps.py              # Dependencies (auth)
│   │   └── v1/
│   │       ├── api.py           # Router aggregation
│   │       └── endpoints/
│   │           ├── auth.py
│   │           ├── users.py
│   │           ├── payments.py
│   │           ├── tasks.py
│   │           └── health.py
│   ├── services/                # Business logic (stub)
│   ├── tasks/
│   │   └── example_tasks.py     # Celery task
│   └── utils/
├── tests/
│   ├── conftest.py              # Test fixtures
│   ├── test_auth.py
│   ├── test_health.py
│   └── test_payments.py
├── .env.example
├── .gitignore
├── requirements.txt
├── Dockerfile
├── pytest.ini
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+** (recommended)
- **pip**
- **Git**
- (Optional) **Docker** for containerized runs

### Installation

<details>
<summary><b>📦 Windows / Linux / macOS</b></summary>

```bash
# Clone the repository
git clone https://github.com/theinsidecoder/back-end-APIs-system.git
cd back-end-APIs-system

# Create virtual environment
python -m venv venv
source venv/bin/activate       # Linux/macOS
.\venv\Scripts\activate        # Windows PowerShell

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env           # Linux/macOS
copy .env.example .env         # Windows

# For a quick demo, use SQLite + in-memory cache by editing .env:
# DATABASE_URL=sqlite+aiosqlite:///./dev.db
# REDIS_URL=

# Run the server
uvicorn app.main:app --reload
```

</details>

<details>
<summary><b>🐳 Docker</b></summary>

```bash
docker build -t saas-backend .
docker run -p 8000:8000 --env-file .env saas-backend
```

</details>

Visit **http://localhost:8000/docs** to see the interactive Swagger UI.

---

## 🔐 Environment Variables

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `DATABASE_URL` | Async SQLAlchemy database URL | Yes | `postgresql+asyncpg://user:pass@host/db` |
| `REDIS_URL` | Redis connection URL (leave empty for memory) | No | `redis://localhost:6379/0` |
| `SECRET_KEY` | Secret key for JWT encoding | Yes | `your-super-secret-key` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | JWT token expiry in minutes | No (default: 30) | `30` |
| `STRIPE_SECRET_KEY` | Stripe secret key | Yes | `sk_test_...` |
| `STRIPE_WEBHOOK_SECRET` | Stripe webhook signing secret | Yes | `whsec_...` |
| `ENVIRONMENT` | Environment name (`development` / `production`) | No | `development` |
| `LOG_LEVEL` | Logging level (`DEBUG`, `INFO`, `WARNING`) | No | `INFO` |

---

## 📡 API Reference

All endpoints are documented automatically at `/docs` (Swagger UI) and `/redoc` (ReDoc).

### Authentication

| Method | Endpoint | Description | Auth? |
|--------|----------|-------------|-------|
| POST | `/api/v1/auth/register` | Register a new user | No |
| POST | `/api/v1/auth/login` | Login and receive JWT | No |

### Users

| Method | Endpoint | Description | Auth? |
|--------|----------|-------------|-------|
| GET | `/api/v1/users/me` | Get current user profile | Yes |

### Payments

| Method | Endpoint | Description | Auth? |
|--------|----------|-------------|-------|
| POST | `/api/v1/payments/create-checkout-session` | Create Stripe checkout session | Yes |
| POST | `/api/v1/payments/webhook` | Stripe webhook handler | No (signature verified) |

### Tasks

| Method | Endpoint | Description | Auth? |
|--------|----------|-------------|-------|
| POST | `/api/v1/tasks/send-welcome-email` | Queue welcome email background task | Yes |

### Health

| Method | Endpoint | Description | Auth? |
|--------|----------|-------------|-------|
| GET | `/api/v1/health/` | Basic health check | No |
| GET | `/api/v1/health/db` | Database connectivity check | No |

---

## 💳 Payment Flow

1. **Create Checkout Session**  
   `POST /api/v1/payments/create-checkout-session` (with JWT)  
   Body: `{"amount": 1000, "currency": "usd"}`  
   Response: `{"checkout_url": "https://checkout.stripe.com/..."}`

2. **Customer Pays**  
   User is redirected to Stripe Checkout. Use test card `4242 4242 4242 4242`.

3. **Webhook Notification**  
   Stripe sends a `checkout.session.completed` event to `/api/v1/payments/webhook`.  
   The handler verifies the signature and updates the payment status to `paid`.

---

## ⚙️ Background Tasks

- Celery is used for asynchronous processing.
- In production, configure a **Redis broker**.
- For development, the **memory broker** allows running without Redis.

**Run the Celery worker locally:**

```bash
celery -A app.core.celery_app.celery_app worker --loglevel=info --pool=solo
```

**Example task:** `send_welcome_email` logs a welcome message and could be extended to send real emails.

---

## 🧠 Caching & Rate Limiting

### Caching
- `app/core/cache.py` provides a unified interface.
- If `REDIS_URL` is set, it uses Redis; otherwise, an in-memory cache.
- The `/users/me` endpoint caches the profile for 60 seconds.

### Rate Limiting
- Implemented with `slowapi`.
- Root endpoint limited to **5 requests per minute** per IP.
- Easily add limits to other endpoints by applying the `@limiter.limit("...")` decorator.

---

## 📊 Monitoring & Logging

- **Console logging** for development visibility.
- **File logging** (`app.log`) for production audits.
- Log level configurable via `LOG_LEVEL` env var.
- Includes timestamps, logger names, and severity levels.

Example log output:
```
2026-08-14 22:42:17,526 - app.main - INFO - Application started
```

---

## 🧪 Testing

The test suite uses **pytest**, **httpx**, and an isolated SQLite database to ensure endpoints behave correctly.

```bash
pytest
```

### Test Cases

| File | Test | Description |
|------|------|-------------|
| `test_auth.py` | `test_register_and_login` | Full auth flow (register → login → token) |
| `test_health.py` | `test_health` | Health endpoint returns 200 |
| `test_payments.py` | `test_create_checkout_session_requires_auth` | Payment endpoint requires JWT |

---

## 🌍 Deployment

### Option 1: PythonAnywhere (Free, no credit card)

Detailed step-by-step guide available [here](https://github.com/theinsidecoder/back-end-APIs-system/wiki/PythonAnywhere-Deployment).

### Option 2: Render (Free tier)

1. Push code to GitHub.
2. Create a new **Web Service** on Render.
3. Connect your repository.
4. Set environment variables.
5. Deploy.

### Option 3: Docker (Any cloud)

```bash
docker build -t saas-backend .
docker run -p 8000:8000 --env-file .env saas-backend
```

---

## 🤝 Contributing

Contributions make the open-source community amazing. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🙏 Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com) for the amazing web framework
- [SQLAlchemy](https://www.sqlalchemy.org) for the powerful ORM
- [Celery](https://docs.celeryq.dev) for background task processing
- [Stripe](https://stripe.com) for payment processing
- [Unsplash](https://unsplash.com) for beautiful open-source images
- [Shields.io](https://shields.io) for badges
- [Mermaid](https://mermaid.js.org) for diagrams

---

## 👨‍💻 About the Developer

<div align="center">
  <img src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100&h=100&fit=crop&crop=faces" width="100" height="100" style="border-radius:50%"/>
  <h3>The Inside Coder</h3>
  <p>Full-Stack Developer & Open Source Enthusiast</p>
  
  [![GitHub](https://img.shields.io/badge/GitHub-theinsidecoder-181717?style=for-the-badge&logo=github)](https://github.com/theinsidecoder)
  [![Twitter](https://img.shields.io/badge/Twitter-%40theinsidecoder-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/theinsidecoder)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-theinsidecoder-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/theinsidecoder)
</div>

---

<div align="center">
  <sub>Built with ❤️ by <strong>The Inside Coder</strong></sub>
</div>
```




