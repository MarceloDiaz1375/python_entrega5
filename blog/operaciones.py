from blog.formateador import formatear_post, crear_separador
# Función para buscar posts por título
def buscar_por_titulo(lista, termino):
    encontrados = [post for post in lista if termino.lower().strip() in post['titulo'].lower()]
    if encontrados:
        print("\nPosts encontrados:")
        for post in encontrados:
            print(f" - {post['titulo']} | Estado: {post['estado']}")
    else:
        print("No se encontraron posts con ese título.")

# Función para filtrar posts por tag
def filtrar_por_tag(lista, tag):
    encontrados = [post for post in lista if tag.lower().strip() in [t.lower().strip() for t in post['tags']]]
    if encontrados:
        print(f"\nPosts con el tag '{tag}':")
        for post in encontrados:
            print(f" - {post['titulo']} | Etiquetas: {', '.join(post['tags'])}")
    else:
        print("No se encontraron posts con esa etiqueta.")

# Función para listar todos los posts
def listar_posts(lista_posts):
    for post in lista_posts:
        print(crear_separador())
        print(formatear_post(post))