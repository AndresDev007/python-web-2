import reflex as rx
from link_bio.styles.colors import Color, ColorButton

def floating_button(icon: str, href: str):
    return rx.link(
        rx.box(
            rx.button(
                rx.image(src=icon, style={"width": "50px"}),
                border_radius="50%",
                box_shadow="md",
                background_color= ColorButton.BLANCO_TRANSPARENTE,
                _hover={
                    "cursor": "pointer",
                    "transform": "scale(1.05)",
                    "background-color": Color.PRIMARY,
                },
            ),
            position="fixed",
            bottom="20px",
            right="20px",
            z_index="1000",
        ),
        href=href,
        is_external=True,
    )