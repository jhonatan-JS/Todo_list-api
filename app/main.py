from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from .models import user, task
from .routers import auth, task as task_router

user.Base.metadata.create_all(bind=engine)
task.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(task_router.router)

@app.get("/")
def root():
    return {"message": "API Todo List"}
