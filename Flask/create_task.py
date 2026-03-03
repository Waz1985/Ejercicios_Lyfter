from flask import request, jsonify
from utils import read_task, is_empty, VALID_STATES, save_tasks


def create_task():
    tasks = read_task()
    data = request.get_json(silent=True) or {}

    if "id" not in data:
        return jsonify({"error": "Field missed 'id'."}), 400
    if is_empty(data.get("title")):
        return jsonify({"error": "Field missed 'title' or is empty"}), 400
    if is_empty(data.get("description")):
        return jsonify({"error": "Field missed 'description' or is empty"}), 400
    if is_empty(data.get("state")):
        return jsonify({"error": "Field missed 'state' or is empty"}), 400
    
    if data["state"] not in VALID_STATES:
        return jsonify({"error": "Invalid state"}), 400
    
    if any(t.get("id") == data["id"] for t in tasks):
        return jsonify({"error": "Already exists a task with this id."}), 409 

    new = {
        "id": data["id"],
        "title": data["title"].strip(),
        "description": data["description"].strip(),
        "state": data["state"],
    }

    tasks.append(new)
    save_tasks(tasks)

    return jsonify({"data": new}), 201