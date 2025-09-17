from celery import Celery
from app.core.config import settings

# Create Celery instance
celery_app = Celery(
    "verifly",
    broker=settings.redis_url,
    backend=settings.redis_url,
    include=["app.tasks"]
)

# Configure Celery
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    result_expires=3600,
)

# Health check task
@celery_app.task
def health_check():
    """Simple health check task."""
    return "Celery is working!"


if __name__ == "__main__":
    celery_app.start()
