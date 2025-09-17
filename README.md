# Verifly - Secure Authentication Platform

A modern full-stack application built with Next.js, FastAPI, PostgreSQL, Redis, and Celery.

## Architecture

- **Frontend**: Next.js 14 + TypeScript + Tailwind CSS
- **Backend**: FastAPI + SQLAlchemy 2.0 + Alembic
- **Database**: PostgreSQL
- **Cache/Queue**: Redis + Celery
- **Authentication**: JWT with httpOnly cookies

## Features

- ✅ Email/password authentication
- ✅ JWT access & refresh tokens
- ✅ httpOnly cookie security
- ✅ Database migrations with Alembic
- ✅ Background job processing with Celery
- ✅ Modern responsive UI with Tailwind CSS
- ✅ Type-safe API with TypeScript & Pydantic
- ✅ Docker containerization
- ✅ CI/CD with GitHub Actions

## Quick Start

### Prerequisites

- Docker & Docker Compose (recommended)
- Node.js 18+ (for local development)
- Python 3.12+ (for local development)
- PostgreSQL & Redis (for local development without Docker)

### Option 1: Docker Setup (Recommended)

```bash
# 1. Clone and setup
git clone <your-repo-url>
cd verifly2

# 2. One-command setup
./scripts/setup.sh

# 3. Access the application
# Frontend: http://localhost:3000
# API: http://localhost:8000
# API Docs: http://localhost:8000/docs
# Mailhog: http://localhost:8025
```

### Option 2: Local Development Setup

```bash
# 1. Clone repository
git clone <your-repo-url>
cd verifly2

# 2. Setup local development environment
./scripts/dev-setup.sh

# 3. Start development servers
./scripts/start-dev.sh
```

### Manual Local Setup

If you prefer to set up manually:

```bash
# Backend setup
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt

# Frontend setup
cd ../frontend
npm install

# Start backend (in one terminal)
cd backend
source venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Start frontend (in another terminal)
cd frontend
npm run dev
```

### Initialize Database

```bash
# With Docker
docker compose exec api alembic upgrade head

# Local development (make sure PostgreSQL is running)
cd backend
source venv/bin/activate
alembic upgrade head
```

### Access the Application

- **Frontend**: http://localhost:3000
- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Mailhog**: http://localhost:8025 (Docker only)

## Available Scripts

The project includes several helpful scripts in the `scripts/` directory:

- **`./scripts/setup.sh`** - Complete Docker setup with database migrations
- **`./scripts/dev-setup.sh`** - Setup local development environment (venv + npm install)
- **`./scripts/start-dev.sh`** - Interactive script to start development servers

## Development

### Backend Development

```bash
cd backend

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
alembic upgrade head

# Start development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Development

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### Database Migrations

```bash
# Create new migration
cd backend
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Downgrade migration
alembic downgrade -1
```

### Background Jobs

```bash
# Start Celery worker
cd backend
celery -A app.celery_app worker --loglevel=info

# Start Celery beat (scheduler)
celery -A app.celery_app beat --loglevel=info
```

## API Endpoints

### Authentication

- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/logout` - Logout user
- `POST /api/auth/refresh` - Refresh access token
- `GET /api/auth/me` - Get current user

### Health

- `GET /` - Root endpoint
- `GET /health` - Health check

## Environment Variables

Copy `env.example` to `.env` and update the values:

```bash
# Database
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/verifly

# Redis
REDIS_URL=redis://localhost:6379/0

# JWT
SECRET_KEY=your-secret-key-change-in-production-must-be-32-chars
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7

# Environment
ENVIRONMENT=development
```

## Testing

### Backend Tests

```bash
cd backend
pytest tests/ -v
```

### Frontend Tests

```bash
cd frontend
npm test
```

## Deployment

### Production Environment Variables

Make sure to set secure values for:

- `SECRET_KEY` - Use a secure random key
- `DATABASE_URL` - Production database URL
- `REDIS_URL` - Production Redis URL
- `ENVIRONMENT=production`

### Docker Production Build

```bash
docker compose -f docker-compose.prod.yml up --build
```

## Project Structure

```
verifly2/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/routes/     # API routes
│   │   ├── core/           # Core configuration
│   │   ├── db/             # Database models & schemas
│   │   └── services/       # Business logic
│   ├── alembic/            # Database migrations
│   └── requirements.txt
├── frontend/               # Next.js frontend
│   ├── app/                # App router pages
│   ├── components/         # Reusable components
│   ├── lib/                # Utilities & API client
│   └── package.json
├── docker-compose.yml      # Development environment
└── .github/workflows/      # CI/CD
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Run linting and tests
6. Submit a pull request

## License

MIT License