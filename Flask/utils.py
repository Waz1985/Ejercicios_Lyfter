import json

FILE_PATH = "tasks_list.json"
ESTADOS_VALIDOS = { "Por Hacer", "En Progreso", "Completada" }

def leer_tareas():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
    
def guardar_tareas(tareas):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(tareas, f, ensure_ascii=False, indent=4)

def es_vacio(valor):
    return valor is None or (isinstance(valor, str) and valor.strip() == "")