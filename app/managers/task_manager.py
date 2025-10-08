from pathlib import Path
from datetime import datetime
import uuid
from models import Task
from utils.json_helper import read_json,write_json
import json
from tagger import Tagger

FILE_PATH = "C:/Users/Ömer Faruk Özvardar/Desktop/Taskify/data/tasks.json"

class TaskManager:
    def __init__(self,file_path:Path = FILE_PATH):
        self.file_path = Path(file_path)

    def load_tasks(self):
        if not self.file_path.exists():
            return[]
        try:
            data = read_json(self.file_path)
            return data
        except json.JSONDecodeError as err:
            print("Something went wrong about JSON file... err:" + str(err))
            return []

    def save_tasks(self, tasks):
    # JSON sadece dict, str, int falan kabul ediyor
        tasks_dict = [
            {k: (v.isoformat() if isinstance(v, datetime) else v) for k, v in t.items()}
            if isinstance(t, dict) else t.__dict__
            for t in tasks
        ]
        write_json(self.file_path, tasks_dict)

    def add_task(self,owner,content,tags=None):
        tasks = self.load_tasks()

        tag_creator = Tagger()
        tag_creator.fit_docs([content], n_cluster=1)
        tag = tag_creator.suggest_tag(content=content)

        task = Task(
            task_id = str(uuid.uuid4()),
            owner = owner,
            content=content,
            tags = tag if tag else [],
            complated= False,
            created_time = datetime.now().isoformat()
        )
        
        tasks.append(task.__dict__)
        self.save_tasks(tasks)
        return task.__dict__
    

    def get_task_by_user(self,owner:str):
        tasks = self.load_tasks()
        return [t for t in tasks if t['owner'] == owner]
    
    def complate_task(self,task_id):
        tasks = self.load_tasks()
        for t in tasks:
            if t['task_id'] == task_id:
                t['complated'] = True
                self.save_tasks(tasks=tasks)
                return t
        return None
    
    def delete_task(self,task_id:str):
        tasks = self.load_tasks()
        new_tasks = [t for t in tasks if t['task_id'] != task_id]
        if len(new_tasks) == len(tasks):
            return False
        self.save_tasks(tasks=tasks)
        return True
    



