from utils import read_tasks
from flask import request

def get_task():
    tasks = read_tasks()
    state_filter = request.args.get("state")
    if state_filter:
        tasks = [t for t in tasks if t.get("state") == state_filter]
    return {"data": tasks}