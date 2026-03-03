from utils import read_tasks, save_tasks

def delete_task(task_id):
    tasks = read_tasks()
    task = next((t for t in tasks if t.get("id") == task_id), None)

    if not task:
        return {"error": "Task not found"}, 404
    
    tasks = [t for t in tasks if t.get("id") != task_id]
    
    save_tasks(tasks)

    return {"message": "Task deleted correctly"}, 200