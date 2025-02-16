import random

import openai
import os
# API key (Replace with environment variable in production)
api_key = os.getenv("OPEN_API_KEY")

# Function to classify the task type
def classify_task(user_input, model="gpt-4o-mini"):
    """
    Uses OpenAI's LLM to classify the task type from user input.
    Example tasks: Summarization, Email Assignment, etc.
    """
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": f"What type of task is this: {user_input}"}]
        )
        return response.choices[0].message.content.lower()  # Returns the task type in lowercase

    except openai.APIError as e:
        return f"API Error: {e}"
    except Exception as e:
        return f"Unexpected Error: {e}"

# Function to summarize text
def summarize_text(text, model="gpt-4o-mini"):
    """
    Summarizes a given text using OpenAI's API.
    """
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": f"Summarize this: {text}"}]
        )
        return response.choices[0].message.content

    except openai.APIError as e:
        return f"API Error: {e}"
    except Exception as e:
        return f"Unexpected Error: {e}"

# Function to assign an email
def assign_email(email_content, model="gpt-4o-mini"):
    """
    Extracts the recipient and assigns the email based on content.
    Example use case: Assigning customer queries to the correct department.
    """
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": f"Who should handle this email? {email_content}"}]
        )
        return f"Assigned to: {response.choices[0].message.content}"

    except openai.APIError as e:
        return f"API Error: {e}"
    except Exception as e:
        return f"Unexpected Error: {e}"

# Main function to execute tasks
def execute_task(user_input):
    """
    Determines the task type and executes the relevant function.
    """
    task_type = classify_task(user_input)

    if "summarize" in task_type:
        return summarize_text(user_input)
    elif "assign email" in task_type or "email" in task_type:
        return assign_email(user_input)
    else:
        return "Sorry, I don't understand this task."

# Example usage
if __name__ == "__main__":
    task = input("Enter your task: ")  # Example: "Summarize the following report..."
    result = execute_task(task)
    print("Task Result:", result)
