from blog.modelos import Blog
from blog.formateador import formatear_post, crear_separador

def mostrar_lista(lista_posts):
    if not lista_posts:
        print("\nNo se encontraron publicaciones.")
        return
    for post in lista_posts:
        print(crear_separador())
        print(formatear_post(post))

def mostrar_menu(blog: Blog):
    while True:
        print("\n--- MENÚ DEL BLOG (POO) ---")
        print("1. Ver todos los posts")
        print("2. Buscar por título")
        print("3. Filtrar por tag")
        print("4. Crear un nuevo post")
        print("5. Validar todos los posts")
        print("6. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Por favor, ingrese un número entero.")
            continue

        if opcion == 1:
            mostrar_lista(blog.listar_posts())

        elif opcion == 2:
            termino = input("Ingrese el título a buscar: ")
            resultados = blog.buscar_por_titulo(termino)
            mostrar_lista(resultados)

        elif opcion == 3:
            tag = input("Ingrese la etiqueta a buscar: ")
            resultados = blog.filtrar_por_tag(tag)
            mostrar_lista(resultados)

        elif opcion == 4:
            print("\n--- Crear Nuevo Post ---")
            titulo = input("Título: ")
            contenido = input("Contenido: ")
            nombre_autor = input("Nombre del autor: ")
            bio_autor = input("Bio del autor (opcional): ")
            tags_input = input("Etiquetas (separadas por coma): ")
            estado = input("Estado (borrador/publicado/archivado) [borrador]: ") or "borrador"

            tags = [t.strip() for t in tags_input.split(",") if t.strip()]

            exito, mensaje = blog.crear_post(
                titulo=titulo,
                contenido=contenido,
                nombre_autor=nombre_autor,
                bio_autor=bio_autor,
                tags=tags,
                estado=estado
            )

            if exito:
                print(f"\n¡Éxito! {mensaje}")
            else:
                print(f"\nNo se pudo crear el post. Errores: {', '.join(mensaje)}")

        elif opcion == 5:
            print("\n--- Reporte de Validación de Posts ---")
            reporte = blog.validar_todos_los_posts()
            for post, valido, msjs in reporte:
                estado_str = "VÁLIDO" if valido else f"INVÁLIDO ({', '.join(msjs)})"
                print(f"- Post ID {post.id} ('{post.titulo or 'Sin título'}'): {estado_str}")

        elif opcion == 6:
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

    print("\n¡Gracias por utilizar el blog!")