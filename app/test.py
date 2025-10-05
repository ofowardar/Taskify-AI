from pathlib import Path
#from passlib.context import CryptContext
from datetime import datetime
from managers.task_manager import TaskManager
from managers.user_manager import UserManager
from utils import json_helper
import uuid


user_manager = UserManager()
task_manager = TaskManager()

# Users test
#user_manager.register_user("deneme2","deneme2")

#Login test
if user_manager.login_user("denem","ofo123"):
    print("Login Succesfully!")
else:
    print("Something Went Wrong!")

task_manager.add_task("Testtest","astronout")