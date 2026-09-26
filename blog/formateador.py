def crear_separador() -> str:
    return "-" * 40

def formatear_post(post) -> str:
    tags = ", ".join(post.tags) if post.tags else "Sin etiquetas"
    return f"""
ID: {post.id}
Título: {post.titulo}
Autor: {post.autor.nombre}
Estado: {post.estado}
Etiquetas: {tags}
Contenido: {post.contenido}
"""
