import reflex as rx
import link_bio.styles.styles as styles
# Importar para que funcionen las paginas
import link_bio.pages.index as index
import link_bio.pages.courses as courses


class State(rx.State):
    pass



app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
