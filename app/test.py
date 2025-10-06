
from managers.task_manager import TaskManager
from managers.user_manager import UserManager
from utils import json_helper
import uuid


task_manager = TaskManager()
user_manager = UserManager()

user_manager.register_user("Mr.Whitee","mrbabawhite")

is_logined,username = user_manager.login_user("Mr.Whitee","mrbabawhite")

if is_logined:
    print("Login Succesfully!!")

    task = task_manager.add_task(username,"Unity Kursu İzle")
    task_manager.complate_task(task['task_id'])

