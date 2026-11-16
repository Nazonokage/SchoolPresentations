import os
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, StrictBool
from sqlalchemy import Boolean, Column, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Session

engine = create_engine(os.environ["DATABASE_URL"], pool_pre_ping=True)
class Base(DeclarativeBase): pass
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    done = Column(Boolean, nullable=False, default=False)
Base.metadata.create_all(engine)
class NewTask(BaseModel):
    title: str
class Change(BaseModel):
    done: StrictBool
app = FastAPI()
def view(row):
    return {"id": str(row.id), "title": row.title, "done": row.done}
@app.get("/tasks")
def tasks():
    with Session(engine) as db:
        return [view(row) for row in db.scalars(select(Task).order_by(Task.id))]
@app.post("/tasks", status_code=201)
def add(body: NewTask):
    title = body.title.strip()
    if not 1 <= len(title) <= 80: raise HTTPException(422, "Title must contain 1–80 characters")
    with Session(engine) as db:
        row = Task(title=title, done=False)
        db.add(row)
        db.commit()
        return view(row)
@app.patch("/tasks/{task_id}")
def update(task_id: int, body: Change):
    with Session(engine) as db:
        row = db.get(Task, task_id)
        if row is None: raise HTTPException(404, "Task missing")
        row.done = body.done
        db.commit()
        return view(row)
@app.delete("/tasks/{task_id}", status_code=204)
def remove(task_id: int):
    with Session(engine) as db:
        row = db.get(Task, task_id)
        if row is None: raise HTTPException(404, "Task missing")
        db.delete(row)
        db.commit()
    return Response(status_code=204)

@app.get("/suggest")
def suggest():
    return {"tip": "Visit the library before lunch."}
