#!/bin/bash

# Verifly Development Startup Script
echo "🚀 Starting Verifly development servers..."

# Check if we're in the right directory
if [ ! -f "docker-compose.yml" ]; then
    echo "❌ Please run this script from the project root directory"
    exit 1
fi

# Function to check if port is in use
check_port() {
    if lsof -Pi :$1 -sTCP:LISTEN -t >/dev/null ; then
        echo "⚠️  Port $1 is already in use"
        return 1
    else
        return 0
    fi
}

# Check required ports
echo "🔍 Checking ports..."
check_port 3000 || echo "Frontend port 3000 is busy"
check_port 8000 || echo "Backend port 8000 is busy"
check_port 5432 || echo "PostgreSQL port 5432 is busy"
check_port 6379 || echo "Redis port 6379 is busy"

echo ""
echo "Choose your development setup:"
echo "1) Docker Compose (recommended - includes databases)"
echo "2) Local development (requires local PostgreSQL and Redis)"
echo ""
read -p "Enter your choice (1 or 2): " choice

case $choice in
    1)
        echo "🐳 Starting with Docker Compose..."
        
        # Copy environment file if it doesn't exist
        if [ ! -f .env ]; then
            cp env.example .env
            echo "📝 Created .env file from template"
        fi
        
        # Start services
        docker compose up --build
        ;;
    2)
        echo "💻 Starting local development servers..."
        
        # Check if virtual environment exists
        if [ ! -d "backend/venv" ]; then
            echo "❌ Virtual environment not found. Please run ./scripts/dev-setup.sh first"
            exit 1
        fi
        
        # Start backend in background
        echo "🐍 Starting FastAPI backend..."
        cd backend
        source venv/bin/activate
        uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
        BACKEND_PID=$!
        cd ..
        
        # Start frontend in background
        echo "🌐 Starting Next.js frontend..."
        cd frontend
        npm run dev &
        FRONTEND_PID=$!
        cd ..
        
        echo ""
        echo "✅ Development servers started!"
        echo "🌐 Frontend: http://localhost:3000"
        echo "🔧 Backend API: http://localhost:8000"
        echo "📚 API Docs: http://localhost:8000/docs"
        echo ""
        echo "Press Ctrl+C to stop all servers"
        
        # Wait for Ctrl+C
        trap "echo '🛑 Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID; exit" INT
        wait
        ;;
    *)
        echo "❌ Invalid choice. Please run the script again."
        exit 1
        ;;
esac
