import reflex as rx
import link_bio.styles.styles as styles
import link_bio.constants as constants
from link_bio.routes import Route
from link_bio.styles.styles import Size
from link_bio.styles.colors import Color
from link_bio.components.floating_button import floating_button

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text("moure", color=Color.PRIMARY.value),
                rx.text("dev", color=Color.SECONDARY.value),
                style=styles.navbar_title_style
            ),
            href=Route.INDEX.value,
        ),
        floating_button(icon="/icons/donate.svg", href=constants.COFFEE_URL),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
    )
