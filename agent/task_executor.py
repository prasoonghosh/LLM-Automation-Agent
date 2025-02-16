from textblob import TextBlob


def fetch_emails():
    """
    Simulates fetching emails from a system.
    """
    return {"status": "success", "emails": ["Email 1", "Email 2", "Email 3"]}


def summarize_text(text):
    """
    Summarizes the given text by extracting key sentences.
    """
    blob = TextBlob(text)
    sentences = blob.sentences

    # If text is too short, return it as is
    if len(sentences) <= 2:
        return text

    # Extract first 3 sentences for summary
    summary = " ".join(str(sentences[i]) for i in range(min(3, len(sentences))))
    return summary


def execute_task(parsed_task):
    """
    Executes the task based on the parsed input.
    """
    if parsed_task["task"] == "fetch_emails":
        return fetch_emails()

    elif parsed_task["task"] == "summarize_text":
        text = parsed_task.get("content", "")
        if text:
            return {"status": "success", "summary": summarize_text(text)}

    return {"status": "error", "message": "Unsupported task."}
