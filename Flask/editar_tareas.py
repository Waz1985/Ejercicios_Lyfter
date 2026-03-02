from flask import request, jsonify
from utils import leer_tareas, es_vacio, ESTADOS_VALIDOS, guardar_tareas 

def editar_tarea(tarea_id):
    tareas = leer_tareas()
    data = request.get_json(silent=True) or {}

    tarea = next((t for t in tareas if t.get("id") == tarea_id), None)
    if not tarea:
        return jsonify({"error": "Tarea no encontrada."}), 404

    if "id" in data and data["id"] != tarea_id:
        return jsonify({"error": "No se permite cambiar el id de la tarea."}), 400

    if "estado" in data:
        if es_vacio(data.get("estado")):
            return jsonify({"error": "El campo 'estado' no puede estar vacío."}), 400
        if data["estado"] not in ESTADOS_VALIDOS:
            return jsonify({"error": "Estado inválido."}), 400

    if "titulo" in data and es_vacio(data.get("titulo")):
        return jsonify({"error": "El campo 'titulo' no puede estar vacío."}), 400

    if "descripcion" in data and es_vacio(data.get("descripcion")):
        return jsonify({"error": "El campo 'descripcion' no puede estar vacío."}), 400

    if "titulo" in data:
        tarea["titulo"] = data["titulo"].strip()
    if "descripcion" in data:
        tarea["descripcion"] = data["descripcion"].strip()
    if "estado" in data:
        tarea["estado"] = data["estado"]

    guardar_tareas(tareas)

    return jsonify({"data": tarea}), 200