from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Task API")


class TaskInput(BaseModel):
    title: str
    completed: bool = False


class Task(TaskInput):
    id: int


tasks: list[Task] = []
next_task_id = 1


@app.get("/health")
def get_health():
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    # TODO: Retorne as tarefas armazenadas.
    raise NotImplementedError


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_input: TaskInput):
    # TODO: Crie uma tarefa com ID único, adicione-a à lista e retorne-a.
    raise NotImplementedError


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    # TODO: Localize a tarefa; lance HTTPException com status 404 se não existir.
    raise NotImplementedError


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)