import json
from flask import Flask
from crear_tareas import crear_tarea
from get_tareas import get_tarea
from editar_tareas import editar_tarea
from eliminar_tareas import eliminar_tarea

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>Hello, World!</h1>"

@app.route("/tareas", methods=["GET"])
def obtener_tareas():
    return get_tarea()

@app.route("/tareas", methods=["POST"])
def agregar_tareas():
    return crear_tarea()
    
@app.route("/tareas/<int:tarea_id>", methods=["PUT"])
def modificar_tareas(tarea_id):
    return editar_tarea(tarea_id)

@app.route("/tareas/<int:tarea_id>", methods=["DELETE"])
def borrar_tareas(tarea_id):
    return eliminar_tarea(tarea_id)

if __name__ == "__main__":
    app.run(host="localhost", debug=True)