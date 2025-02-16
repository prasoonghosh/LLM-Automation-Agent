import logging

logger = logging.getLogger(__name__)

def execute_task(parsed_task: dict):
    """
    Executes the given task and returns the result.
    """
    logger.info(f"Executing task: {parsed_task}")

    if parsed_task.get("task") == "fetch_emails":
        # Simulate fetching emails
        emails = ["Email 1", "Email 2", "Email 3"]
        logger.info(f"Fetched emails: {emails}")
        return {"status": "success", "emails": emails}

    logger.error("Unsupported task received")
    return {"status": "error", "message": "Unsupported task."}
