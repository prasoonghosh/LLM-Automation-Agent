import logging

logger = logging.getLogger(__name__)

def parse_task(user_input: str):
    """
    Parses the user's input and returns a structured task.
    """
    logger.info(f"Parsing user input: {user_input}")

    # Normalize input
    user_input = user_input.lower().strip()

    # Check for email-related tasks
    if "email" in user_input or "fetch emails" in user_input or "get emails" in user_input:
        logger.info("Task recognized: fetch_emails")
        return {"task": "fetch_emails"}

    logger.info("Task not recognized")
    return {"task": "unsupported"}
