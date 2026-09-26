def crear_separador():
    return "-" * 40
def formatear_post(post):
    tags = ", ".join(post["tags"])
    return f"""
Título: {post["titulo"]}
Autor: {post["autor"]["nombre"]}
Estado: {post["estado"]}
Etiquetas: {tags}
"""
