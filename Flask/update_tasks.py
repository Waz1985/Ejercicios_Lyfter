from flask import request, jsonify
from utils import read_tasks, is_empty, VALID_STATES, save_tasks 

def update_task(task_id):
    tasks = read_tasks()
    data = request.get_json(silent=True) or {}

    task = next((t for t in tasks if t.get("id") == task_id), None)
    if not task:
        return jsonify({"error": "Task not found."}), 404

    if "id" in data and data["id"] != task_id:
        return jsonify({"error": "You can't change the task id."}), 400

    if "state" in data:
        if is_empty(data.get("state")):
            return jsonify({"error": "Field 'state' can't be empty."}), 400
        if data["state"] not in VALID_STATES:
            return jsonify({"error": "Invalid state."}), 400

    if "title" in data and is_empty(data.get("title")):
        return jsonify({"error": "Field 'title' can't be empty."}), 400

    if "description" in data and is_empty(data.get("description")):
        return jsonify({"error": "Field 'description' can't be empty."}), 400

    if "title" in data:
        task["title"] = data["title"].strip()
    if "description" in data:
        task["description"] = data["description"].strip()
    if "state" in data:
        task["state"] = data["state"]

    save_tasks(tasks)

    return jsonify({"data": task}), 200