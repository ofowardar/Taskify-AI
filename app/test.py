
from managers.task_manager import TaskManager
from managers.user_manager import UserManager
from utils import json_helper
import uuid


task_manager = TaskManager()
user_manager = UserManager()

user_manager.register_user("test1","test1")

isLogined,username = user_manager.login_user("test1","test1")

context = """
I need go to shop and buy some vegetables for my healty eating because i will prepare dinner for tonight.
"""

if isLogined:
    task = task_manager.add_task(username,context)
    print(task)

#owner_tasks = task_manager.get_task_by_user(username)
#print(owner_tasks)

task_manager.complate_task(task['task_id'])



