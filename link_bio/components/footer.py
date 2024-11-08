import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size
from link_bio.styles.colors import Color, TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo.png",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt="Logotipo de MoureDev. Una \"eme\" entre llaves."
        ),
        rx.vstack(
            rx.box(
                f"© 2014-{datetime.date.today().year} ",
                rx.link(" MoureDev by Brais Moure ", color=Color.PRIMARY.value, href=const.MOUREDEV_URL, is_external=True),
                " v3.",
                padding_top=Size.DEFAULT.value
            ),
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/github.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value
                ),
                rx.text(
                    "BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD.",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value
                )
            ),
            href=const.REPO_URL,
            is_external=True
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        spacing=Size.ZERO.value,
        color=TextColor.FOOTER.value,
        align="center"
    )
