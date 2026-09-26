# Sistema de Blog (Programación Orientada a Objetos + JSON)

Este proyecto es un sistema de gestión de blog desarrollado en Python, estructurado bajo el paradigma de **Programación Orientada a Objetos (POO)** y con persistencia de datos local mediante un archivo **JSON**.

---

## 🏗️ Arquitectura y Clases (`blog/modelos.py`)

La lógica del sistema se organiza mediante tres clases principales:

1. **`Autor`**:
   - Representa al autor de una publicación.
   - Atributos: `nombre` y `bio`.
   - Incluye métodos para convertir el objeto a diccionario (`a_diccionario`) y reconstruirlo desde un diccionario (`desde_diccionario`).

2. **`Post`**:
   - Representa una publicación del blog.
   - Atributos: `id`, `titulo`, `contenido`, `autor` (instancia de `Autor`), `tags` (lista de etiquetas) y `estado` (`borrador`, `publicado`, `archivado`).
   - Implementa métodos de serialización para facilitar el guardado en JSON.

3. **`Blog` (Clase Centralizadora)**:
   - Administra la colección de objetos `Post`.
   - Al instanciarse, se encarga de cargar las publicaciones guardadas desde `posts.json`.
   - Ofrece métodos para:
     - `listar_posts()`: Retorna todas las publicaciones.
     - `buscar_por_titulo(termino)`: Busca publicaciones por coincidencia en el título.
     - `filtrar_por_tag(tag)`: Filtra publicaciones por etiqueta.
     - `crear_post(...)`: Instancia un `Autor` y un `Post`, lo agrega a la lista y actualiza el archivo JSON.
     - `validar_todos_los_posts()`: Valida la estructura y campos de cada publicación.

---

## 💾 Persistencia de Datos (`posts.json` + `blog/datos.py`)

- **Lectura:** Al iniciar la aplicación en `main.py`, la clase `Blog` llama a `cargar_posts()` de `datos.py`, leyendo el archivo `posts.json` y transformando los diccionarios en objetos `Post` y `Autor`.
- **Escritura:** Cada vez que se crea un nuevo post mediante el método `blog.crear_post()`, los objetos se convierten a formato diccionario y se guardan automáticamente en `posts.json` usando el módulo nativo `json`.

---

## 📁 Estructura del Proyecto

```text
├── main.py            # Punto de entrada de la aplicación
├── posts.json         # Archivo de persistencia de datos
├── README.md          # Documentación del proyecto
└── blog/              # Paquete principal
    ├── __init__.py
    ├── datos.py        # Lectura y escritura en el archivo JSON
    ├── formateador.py  # Formato de visualización en consola
    ├── menu.py         # Interfaz de usuario interactiva
    └── modelos.py      # Definición de las clases Autor, Post y Blog