import re
def parse_task(user_input):
    """
    Parses the user input to identify the task type.
    """
    user_input = user_input.lower()

    if "fetch emails" in user_input:
        return {"task": "fetch_emails"}

    elif "summarize" in user_input:
        match = re.search(r"summarize (.+)", user_input)
        if match:
            return {"task": "summarize_text", "content": match.group(1)}

    return {"task": "unsupported"}
