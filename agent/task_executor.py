import os
from typing import Dict
from agent.llm_utils import summarize_text

def execute_task(parsed_task: Dict) -> Dict:
    """
    Executes the parsed task based on the identified type.
    """
    task_type = parsed_task.get("task")
    filename = parsed_task.get("filename")

    if not filename:
        return {"status": "error", "message": "Filename not provided."}

    if not os.path.exists(filename):
        return {"status": "error", "message": f"File '{filename}' not found."}

    if task_type == "read_file":
        return read_file(filename)

    elif task_type == "extract_errors":
        return extract_errors_from_file(filename)

    elif task_type == "summarize_file":
        return summarize_file(filename)

    else:
        return {"status": "error", "message": "Unsupported task."}


def read_file(filename: str) -> Dict:
    """ Reads and returns the full content of a file. """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    return {"status": "success", "content": content}


def extract_errors_from_file(filename: str) -> Dict:
    """ Extracts lines containing 'error' from a log file. """
    errors = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if "error" in line.lower():
                errors.append(line.strip())

    return {"status": "success", "errors": errors}


def summarize_file(filename: str) -> Dict:
    """ Reads the content of a file and generates a summary using LLM. """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    summary = summarize_text(content)
    return {"status": "success", "summary": summary}
