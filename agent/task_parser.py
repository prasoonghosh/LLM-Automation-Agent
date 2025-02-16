from typing import Dict

def parse_task(user_input: str) -> Dict:
    """
    Parses the user input to determine the task type and extract necessary parameters.
    """
    user_input = user_input.lower()

    if "read file" in user_input or "show contents of" in user_input:
        filename = user_input.split("of")[-1].strip()
        return {"task": "read_file", "filename": filename}

    elif "extract errors from" in user_input or "find errors in" in user_input:
        filename = user_input.split("from")[-1].strip()
        return {"task": "extract_errors", "filename": filename}

    elif "summarize report" in user_input or "summarize file" in user_input:
        filename = user_input.split("report")[-1].strip()
        return {"task": "summarize_file", "filename": filename}

    else:
        return {"task": "unsupported"}
