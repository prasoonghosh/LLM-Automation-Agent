from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent.task_parser import parse_task
from agent.task_executor import execute_task

# Initialize FastAPI app
app = FastAPI()

# Define request model
class TaskRequest(BaseModel):
    user_input: str

@app.post("/execute-task/")
async def execute_task_endpoint(request: TaskRequest):
    """
    Endpoint to receive a task from the user, parse it, and execute it.
    """
    try:
        # Parse the task
        parsed_task = parse_task(request.user_input)

        # Log parsed task
        print(f"Parsed Task: {parsed_task}")

        # Execute the parsed task
        result = execute_task(parsed_task)

        # Log execution result
        print(f"Execution Result: {result}")

        # Return the result
        return {"status": "success", "data": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Root endpoint
@app.get("/")
def root():
    return {"message": "LLM Automation Agent is running!"}
