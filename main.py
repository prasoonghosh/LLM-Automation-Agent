from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent.task_parser import parse_task
from agent.task_executor import execute_task

app = FastAPI()

class TaskRequest(BaseModel):
    user_input: str

@app.post("/execute-task/")
async def execute_task_endpoint(request: TaskRequest):
    """
    API endpoint to process automation tasks.
    """
    try:
        parsed_task = parse_task(request.user_input)
        result = execute_task(parsed_task)
        return {"status": "success", "data": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "LLM Automation Agent is running!"}
