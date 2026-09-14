
from blog.operaciones import buscar_por_titulo, filtrar_por_tag, listar_posts
from blog.datos import posts
from blog.validaciones import validar_post

# Función para mostrar el menú del blog
def mostrar_menu():
    while True:
        print("\n--- MENU DEL BLOG ---")
        print("1. Ver todos los posts")
        print("2. Buscar por titulo")
        print("3. Filtrar por tag")
        print("4. Validar un post")
        print("5. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            # Llamada a la función listar_posts
            listar_posts(posts)

        elif opcion == 2:
            # Llamada a la función buscar_por_titulo
            titulo_busqueda = input("Ingrese el título a buscar: ")
            buscar_por_titulo(posts, titulo_busqueda)

        elif opcion == 3:
            # Llamada a la función filtrar_por_tag
            tag_busqueda = input("Ingrese la etiqueta a buscar: ")
            filtrar_por_tag(posts, tag_busqueda)
        
        elif opcion == 4:
            print("Validando todos los posts del blog...")
            num_post = 0
            # Bucle for y llamada a la función validar_post para cada post en la lista
            for post in posts:
                num_post += 1
                valido, errores = validar_post(post)
                if valido:
                    print(f"Post {num_post}: es válido.")
                else:
                    print(f"Post {num_post}: no es válido - {errores}")

        elif opcion == 5:
            print("Saliendo del blog...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    print("\nGracias por usar el sistema de blog. ¡Hasta luego!")