from pathlib import Path
#from passlib.context import CryptContext
from datetime import datetime
from managers.task_manager import TaskManager
from managers.user_manager import UserManager
from utils import json_helper
import uuid


user_manager = UserManager()
task_manager = TaskManager()

user_manager.register_user("ofowardar","ofoofo")

is_logined,current_username = user_manager.login_user("ofowardar","ofoofo")
#is_logined,current_username = user_manager.login_user("deneme_son","sadsa") Wrong Passwd test
print(is_logined)

if current_username:
    task = task_manager.add_task(current_username,"asdsadsa")

print(current_username)

own_tasks = task_manager.get_task_by_user(current_username)

print(own_tasks)

complated_task = task_manager.complate_task(task['task_id'])
print(complated_task)
