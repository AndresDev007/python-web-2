import reflex as rx

# Comun
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

preview="https://moure.dev/preview.jpg" # imagen que se muestra cuando se comparte en redes sociales
_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twiter:card", "content": "summary_large_image"},
    {"name": "twiter:site", "content": "@mouredev"}
]

# Index
index_title="MoureDev | Te enseño programación y desarrollo de software"
index_description="Hola, mi nombre es Brais Moure. Soy ingeniero de software, desarrollador freelance full-stack y divulgador."

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description}
]
index_meta.extend(_meta)

# Courses
courses_title="MoureDev | Cursos gratuitos de programación y desarrollo de software"
courses_description="Este es un listado de los cursos de programación gratuitos."

courses_meta = [
    {"name": "og:title", "content": courses_title},
    {"name": "og:description", "content": courses_description}
]
courses_meta.extend(_meta)