from flask import request, jsonify
from utils import leer_tareas, es_vacio, ESTADOS_VALIDOS, guardar_tareas


def crear_tarea():
    tareas = leer_tareas()
    data = request.get_json(silent=True) or {}

    if "id" not in data:
        return jsonify({"error": "Falta el campo 'id'."}), 400
    if es_vacio(data.get("titulo")):
        return jsonify({"error": "Falta el campo 'titulo' o esta vacio"}), 400
    if es_vacio(data.get("descripcion")):
        return jsonify({"error": "Falta el campo 'descripcion' o esta vacio"}), 400
    if es_vacio(data.get("estado")):
        return jsonify({"error": "Falta el campo 'estado' o esta vacio"}), 400
    
    if data["estado"] not in ESTADOS_VALIDOS:
        return jsonify({"error": "Estado invalido"}), 400
    
    if any(t.get("id") == data["id"] for t in tareas):
        return jsonify({"error": "Ya existe una tarea con ese id."}), 409 

    nueva = {
        "id": data["id"],
        "titulo": data["titulo"].strip(),
        "descripcion": data["descripcion"].strip(),
        "estado": data["estado"],
    }

    tareas.append(nueva)
    guardar_tareas(tareas)

    return jsonify({"data": nueva}), 201