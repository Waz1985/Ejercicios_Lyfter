import json

FILE_PATH = "tasks_list.json"
VALID_STATES = { "To Do", "In Progress", "Completed" }

def read_tasks():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
    
def save_tasks(tasks):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def is_empty(valor):
    return valor is None or (isinstance(valor, str) and valor.strip() == "")