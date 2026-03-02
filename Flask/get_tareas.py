from utils import leer_tareas
from flask import request

def get_tarea():
    tareas = leer_tareas()
    fitro_estado = request.args.get("estado")
    if fitro_estado:
        tareas = [t for t in tareas if t.get("estado") == fitro_estado]
    return {"data": tareas}