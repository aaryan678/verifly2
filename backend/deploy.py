#!/usr/bin/env python3
"""
Deployment script for Render.
Runs database migrations before starting the server.
"""

import asyncio
import os
import subprocess
import sys
from app.core.config import settings

def run_migrations():
    """Run Alembic migrations."""
    print("Running database migrations...")
    try:
        result = subprocess.run(
            ["alembic", "upgrade", "head"],
            check=True,
            capture_output=True,
            text=True
        )
        print("Migrations completed successfully!")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Migration failed: {e}")
        print(f"Error output: {e.stderr}")
        sys.exit(1)

def main():
    """Main deployment function."""
    print(f"Starting deployment for environment: {settings.environment}")
    
    # Only run migrations in production
    if settings.environment == "production":
        run_migrations()
    else:
        print("Skipping migrations in development mode")
    
    print("Deployment script completed!")

if __name__ == "__main__":
    main()
