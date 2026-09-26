import json
import os

RUTA_ARCHIVO = "posts.json"

def cargar_posts() -> list:
    """Lee el archivo JSON y retorna una lista de diccionarios."""
    if not os.path.exists(RUTA_ARCHIVO):
        return []

    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except Exception as e:
        print(f"Error al leer {RUTA_ARCHIVO}: {e}")
        return []

def guardar_posts(lista_diccionarios: list):
    """Escribe la lista de diccionarios en el archivo JSON."""
    try:
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(lista_diccionarios, archivo, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error al escribir en {RUTA_ARCHIVO}: {e}")