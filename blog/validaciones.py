from blog.datos import estados_post

# Función para validar los posts del blog

def validar_post(post):
    errores = []

    if not isinstance(post, dict):
        return False, ["El post debe ser un diccionario."]

    claves_requeridas = ["titulo", "contenido", "autor", "tags", "estado"]
    for clave in claves_requeridas:
        if clave not in post:
            errores.append(f"No se encontró la clave '{clave}' en el post.")

    if not post.get("titulo"):
        errores.append("El post debe tener un título.")

    if not post.get("contenido"):
        errores.append("El post debe tener contenido.")

    autor = post.get("autor")
    if not isinstance(autor, dict) or "nombre" not in autor:
        errores.append("El autor debe ser un diccionario con al menos la clave 'nombre'.")

    tags = post.get("tags")
    if not isinstance(tags, list) or not all(isinstance(tag, str) for tag in tags):
        errores.append("Las etiquetas deben ser una lista de cadenas.")

    estado = post.get("estado")
    if estado not in estados_post:
        errores.append(f"El estado '{estado}' no es válido. Debe ser uno de {estados_post}.")

    if errores:
        return False, errores

    return True, "El post es válido."