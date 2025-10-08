from fastapi import FastAPI
from app.managers.user_manager import UserManager
from app.managers.task_manager import TaskManager

app = FastAPI()

user_manager = UserManager()
task_manager = TaskManager()

@app.get("/")
def home():
    return {"message": "Taskify API is running 🚀"}

@app.post("/register")
def register(username: str, password: str):
    return user_manager.register_user(username, password)

@app.post("/login")
def login(username: str, password: str):
    isLogined, user = user_manager.login_user(username, password)
    return {"success": isLogined, "username": user if isLogined else None}

@app.post("/add_task")
def add_task(username: str, content: str):
    task = task_manager.add_task(username, content)
    return {"task": task}

@app.get("/tasks")
def get_tasks(username:str):
    return {"tasks": task_manager.get_task_by_user(username)}
