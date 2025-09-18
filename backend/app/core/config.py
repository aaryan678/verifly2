from pydantic_settings import BaseSettings
from typing import Optional, List
import os


class Settings(BaseSettings):
    # Database
    database_url: str = "sqlite+aiosqlite:///./verifly.db"
    
    # Redis
    redis_url: str = "redis://localhost:6379/0"
    
    # JWT
    secret_key: str = "your-secret-key-change-in-production-must-be-32-chars"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 7
    
    # Environment
    environment: str = "development"
    
    # CORS - handle both string and list formats
    backend_cors_origins: List[str] = ["http://localhost:3000"]
    
    @property
    def cors_origins(self) -> List[str]:
        """Handle CORS origins from environment variable (comma-separated string) or list"""
        if isinstance(self.backend_cors_origins, str):
            return [origin.strip() for origin in self.backend_cors_origins.split(",")]
        return self.backend_cors_origins
    
    # Email (for future use)
    smtp_host: str = "localhost"
    smtp_port: int = 1025
    smtp_user: Optional[str] = None
    smtp_password: Optional[str] = None
    smtp_from: str = "noreply@verifly.com"
    
    class Config:
        env_file = ["dev.env", ".env"]
        case_sensitive = False


settings = Settings()
