import json
from pathlib import Path

def read_json(path:str) -> list:
    """

    Read json and return list.

    """

    file = Path(path)

    if not file.exists():
        return []

    with open(file,"r",encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as err:
            print("JSON DECODE ERROR ! ",err)
            return []
        return data

def write_json(path:str,data:list):
    """
        Write data to Json file.
    """
    with open(path,"w",encoding="utf-8") as file:
        json.dump(data,file,indent=4,ensure_ascii=False)

        




