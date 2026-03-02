from utils import leer_tareas, guardar_tareas

def eliminar_tarea(tarea_id):
    tareas = leer_tareas()
    tarea = next((t for t in tareas if t.get("id") == tarea_id), None)

    if not tarea:
        return {"error": "Tarea no encontrada"}, 404
    
    tareas = [t for t in tareas if t.get("id") != tarea_id]
    
    guardar_tareas(tareas)

    return {"mensaje": "Tarea eliminada correctamente"}, 200