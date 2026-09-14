# Sistema de Blog

Este proyecto es un sistema simple de blog desarrollado en Python para practicar manejo de listas, funciones, validaciones y organización modular del código.

## ¿Cómo está organizado?

La estructura principal del proyecto es la siguiente:

- `main.py`: punto de entrada del programa. Ejecuta el menú principal.
- `blog/`: paquete principal del sistema.
  - `__init__.py`: marca el directorio como paquete de Python.
  - `datos.py`: contiene los datos iniciales del blog, como el autor, los estados y la lista de posts.
  - `operaciones.py`: incluye funciones para buscar por título, filtrar por etiquetas y listar los posts.
  - `menu.py`: define la interfaz del menú y la lógica de navegación.
  - `validaciones.py`: valida cada post y devuelve una lista con errores si hay inconsistencias.

## ¿Qué hace el sistema?

El menú permite:

1. Ver todos los posts.
2. Buscar un post por título.
3. Filtrar posts por tag o etiqueta.
4. Validar cada post y mostrar los errores detectados.
5. Salir del programa.

## Cómo ejecutar el sistema

Desde la carpeta raíz del proyecto, ejecutá:

```bash
python main.py
```

Si estás en Windows PowerShell, también podés usar:

```powershell
python .\main.py
```

## Requisitos

- Python 3.x
- Ejecutar desde la raíz del proyecto para que el paquete `blog` se resuelva correctamente.

## Nota

El proyecto está diseñado como una práctica de modularización. Cada archivo tiene una responsabilidad específica, lo que facilita mantener y ampliar el sistema.
