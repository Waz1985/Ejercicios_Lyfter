import json
from flask import Flask
from create_task import create_task
from get_tasks import get_task
from update_tasks import update_task
from delete_tasks import delete_task

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>Hello, World!</h1>"

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return get_task()

@app.route("/tasks", methods=["POST"])
def add_tasks():
    return create_task()
    
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_tasks(task_id):
    return update_task(task_id)

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_tasks(task_id):
    return delete_task(task_id)

if __name__ == "__main__":
    app.run(host="localhost", debug=True)