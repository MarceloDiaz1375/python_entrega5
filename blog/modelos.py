from blog.datos import cargar_posts, guardar_posts

class Autor:
    def __init__(self, nombre: str, bio: str = ""):
        self.nombre = nombre
        self.bio = bio

    def a_diccionario((self) -> dict:
        return {
            "nombre": self.nombre,
            "bio": self.bio
        }

    @classmethod
    def desde_diccionario(cls, datos: dict):
        if not datos or not isinstance(datos, dict):
            return cls(nombre="Anónimo", bio="")
        return cls(
            nombre=datos.get("nombre", "Anónimo"),
            bio=datos.get("bio", "")
        )


class Post:
    def __init__(self, id_post: int, titulo: str, contenido: str, autor: Autor, tags: list = None, estado: str = "borrador"):
        self.id = id_post
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor  # Debe ser una instancia de la clase Autor
        self.tags = tags if tags is not None else []
        self.estado = estado

    def a_diccionario(self) -> dict:
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.a_diccionario(),
            "tags": self.tags,
            "estado": self.estado
        }

    @classmethod
    def desde_diccionario(cls, datos: dict):
        autor_obj = Autor.desde_diccionario(datos.get("autor"))
        return cls(
            id_post=datos.get("id", 0),
            titulo=datos.get("titulo", ""),
            contenido=datos.get("contenido", ""),
            autor=autor_obj,
            tags=datos.get("tags", []),
            estado=datos.get("estado", "borrador")
        )


class Blog:
    def __init__(self):
        # Al instanciar Blog, cargamos las publicaciones desde el JSON
        self.posts = self.cargar_desde_json()

    def cargar_desde_json(self) -> list:
        datos_dict = cargar_posts()
        return [Post.desde_diccionario(p) for p in datos_dict]

    def guardar_en_json(self):
        datos_dict = [p.a_diccionario() for p in self.posts]
        guardar_posts(datos_dict)

    def obtener_todos((self) -> list:
        """Devuelve todos los objetos Post cargados."""
        return self.posts

    def listar_posts(self) -> list:
        """Devuelve la lista completa de posts."""
        return self.posts

    def buscar_por_titulo(self, termino: str) -> list:
        """Busca y retorna los posts cuyo título coincida con el término."""
        termino_limpio = termino.lower().strip()
        return [p for p in self.posts if termino_limpio in p.titulo.lower()]

    def filtrar_por_tag(self, tag: str) -> list:
        """Filtra y retorna los posts que contengan la etiqueta ingresada."""
        tag_limpio = tag.lower().strip()
        return [
            p for p in self.posts 
            if tag_limpio in [t.lower().strip() for t in p.tags]
        ]

    def crear_post(self, titulo: str, contenido: str, nombre_autor: str, bio_autor: str, tags: list, estado: str = "borrador") -> tuple:
        """Crea un objeto Autor, un objeto Post, lo agrega a la lista y persiste en JSON."""
        autor = Autor(nombre=nombre_autor, bio=bio_autor)
        nuevo_id = len(self.posts) + 1
        
        nuevo_post = Post(
            id_post=nuevo_id,
            titulo=titulo,
            contenido=contenido,
            autor=autor,
            tags=tags,
            estado=estado
        )

        valido, errores = self.validar_un_post(nuevo_post)
        if valido:
            self.posts.append(nuevo_post)
            self.guardar_en_json()
            return True, "Post creado con éxito."
        else:
            return False, errores

    def validar_un_post(self, post: Post) -> tuple:
        """Valida una instancia individual de Post."""
        errores = []
        estados_validos = ("borrador", "publicado", "archivado")

        if not post.titulo or not post.titulo.strip():
            errores.append("El post debe tener un título.")

        if not post.contenido or not post.contenido.strip():
            errores.append("El post debe tener contenido.")

        if not post.autor or not post.autor.nombre or not post.autor.nombre.strip():
            errores.append("El post debe tener un autor con nombre.")

        if not isinstance(post.tags, list):
            errores.append("Las etiquetas deben ser una lista.")

        if post.estado not in estados_validos:
            errores.append(f"El estado '{post.estado}' no es válido. Debe ser uno de {estados_validos}.")

        if errores:
            return False, errores
        return True, ["Post válido."]

    def validar_todos_los_posts(self) -> list:
        """Valida toda la colección de publicaciones y devuelve el reporte."""
        reporte = []
        for p in self.posts:
            valido, msjs = self.validar_un_post(p)
            reporte.append((p, valido, msjs))
        return reporte