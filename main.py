from blog.modelos import Blog
from blog.menu import mostrar_menu

if __name__ == "__main__":
    # Instanciamos la clase Blog que se encarga de cargar los posts de datos.py
    mi_blog = Blog()

    # Ejecutamos el menú pasándole el objeto mi_blog
    mostrar_menu(mi_blog)