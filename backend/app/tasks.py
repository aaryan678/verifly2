from app.celery_app import celery_app


@celery_app.task
def send_email_task(to_email: str, subject: str, body: str):
    """Background task to send email."""
    # TODO: Implement email sending logic
    print(f"Sending email to {to_email}: {subject}")
    return f"Email sent to {to_email}"


@celery_app.task
def process_data_task(data: dict):
    """Background task to process data."""
    # TODO: Implement data processing logic
    print(f"Processing data: {data}")
    return "Data processed successfully"
