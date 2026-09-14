perfil_autor = {
    "nombre": "Ana López",
    "bio": "Desarrolladora web y creadora de contenido sobre programación.",
    "especialidad": "Python y Django",
    "redes_sociales": ["@ana_dev", "@ana_python"]
}
estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {"Python", "Django", "Web", "Backend", "Python", "Principiantes", "Errores", "Excepciones", "Bases de datos", "Listas"}
posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "En este post veremos cómo empezar a programar con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Qué es Django",
        "contenido": "Django es un framework web creado con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "Web"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con listas",
        "contenido": "Las listas permiten guardar varios elementos en una sola variable.",
        "autor": perfil_autor,
        "tags": ["Python", "Listas"],
        "estado": "archivado"
    },
    {
        "id": 4,
        "titulo": "Introducción a las bases de datos",
        "contenido": "Aprende los conceptos básicos de las bases de datos y cómo trabajar con ellas en Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Bases de datos"],
        "estado": "publicado"
    },
    {
        "id": 5,
        "titulo": "Manejo de errores en Python",
        "contenido": "En este post aprenderemos a manejar errores y excepciones en Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Errores", "Excepciones"],
        "estado": "borrador"
    },
    #Post con título vacío para probar la validación
    {
        "id": 6,
        "titulo": "",
        "contenido": "",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "Web", "Backend"],
        "estado": "publicado"
    }
]