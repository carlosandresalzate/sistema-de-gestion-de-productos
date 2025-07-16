"""
Script: decorators.py
"""

from colorama import Fore, Style


def header(text, level=1, color=Fore.GREEN, width=60, char="="):
    """
    Genera un encabezado decorativo para consola.

    Args:
        text (str): El texto del encabezado
        level (int): Nivel de encabezado (1: grande, 2: mediano, 3: pequeño).
        color (str): Color de texto (Fore de colorama).
        width (int): Ancho total del bloque.
        char (str): Caracter usado como borde (por defecto "=").

    Returns:
        str: Cadena formateada para impresion
    """

    if level == 1:
        deco_char = char
    elif level == 2:
        deco_char = "-"
    else:
        deco_char = "·"

    line = deco_char * width
    centere_text = text.center(width)

    return f"\n{color}{line}\n{centere_text}\n{line}{Style.RESET_ALL}"


def divider(char="-", color=Fore.WHITE, width=60):
    """
    Retorna una línea horizontal decorativa.

    Args:
        char (str): Caracter para la línea.
        color (str): Color del texto.
        width (int): Ancho de la línea.

    Returns:
        str
    """
    return f"{color}{char * width}{Style.RESET_ALL}"


def centered(text, color=Fore.WHITE, width=60):
    """
    Centra un texto con color.

    Args:
        text (str): Texto a centrar.
        color (str): Color del texto.
        width (int): Ancho total.

    Returns:
        str
    """
    return f"{color}{text.center(width)}{Style.RESET_ALL}"


def boxed_text(
    text,
    color=Fore.BLUE,
    border_char="·",
    padding=1,
    width=60,
    centered=True,
):
    """
    Muestra un texto dentro de un marco (box).

    Args:
        text (str): Texto a mostrar.
        color (str): Color del texto.
        border_char (str): Carácter del borde.
        padding (int): Espacio dentro del borde.
        width (int): Ancho total del bloque.
        centered (bool): Si se centra cada linea del box

    Returns:
        str
    """
    inner_width = width - 2
    pad = " " * padding
    content = f"{pad}{text}{pad}"
    content = content.center(inner_width)

    top_bot = border_char * width
    middle = f"{border_char}{content}{border_char}"

    lines = [top_bot, middle, top_bot]

    if centered:
        centered_lines = [line.center(width) for line in lines]
        return f"{color}" + "\n".join(centered_lines) + f"{Style.RESET_ALL}"
    else:
        return f"{color}" + "\n".join(lines) + f"{Style.RESET_ALL}"


def aligned_menu(text: str, indent: int = 10, color=Fore.WHITE):
    """
    Muestra una línea de menú con sangría izquierda (como un centrado balanceado).

    Args:
        text (str): Texto del ítem de menú.
        indent (int): Cantidad de espacios desde el margen izquierdo.
        color (str): Color del texto.

    Returns:
        str
    """
    return f"{color}{' ' * indent}{text}{Style.RESET_ALL}"
