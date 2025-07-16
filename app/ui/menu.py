"""
Script: menu.py

set de utilidades para desplegar un menu de opciones.
"""

from colorama import Fore
from app.ui.config import FAREWELL, SYMBOL
from app.ui.decorators import aligned_menu, boxed_text
from app.ui.message import info, warning
from app.utils.close_app import end_program
from app.utils.random_farewell import set_random_farewell


def show_menu_options(list_opt, menu_title, navigate="close"):
    """
    Muestra un menu de opciones

    Args:
        list_opt (list[str]): Una lista de opciones para visualizar.
        navigate (str): define si se cierra o se vuelve atras en la navegacion
            - "close": Indica que se debe cerrar la aplicacion, por defecto
            - "previous": Indica que debe volver un paso atras en el menu

    Returns:
        tuple[str, str]
            - navigate (ver opciones) o la entrada del menu
            - mensaje accion

    Side Effects:
        - Solicita entrada al usurio con `input`
        - Muestra mensajes en consola con `print`

    Warnings:
        - En algunas aplicacionones como Warp terminal lanza un eror inesperado al usar `CTRL + C`

    """
    length = len(list_opt)
    menu_title = menu_title
    # box =
    print(boxed_text(menu_title, color=Fore.BLUE))

    for index, option in enumerate(list_opt, 1):
        # print(f"{index}. {option}")
        print(aligned_menu(f"{index}. {option}"))

    while True:
        try:
            get_user_opt = input(
                aligned_menu(f"Ingrese una opcion de (1-{length})\n\n{SYMBOL} ")
            ).strip()

            # print("get_user_opt ", get_user_opt)
            if not get_user_opt.isdigit():
                message = "Solo se permiten numeros"
                print(warning(message))
                continue

            index = int(get_user_opt)

            if index < 1 or index > length:
                message = warning("Opcion fuera de rango")
                print(message)
                continue

            selected_text = list_opt[index - 1]
            if index == length:
                match navigate:
                    case "close":
                        message = set_random_farewell(FAREWELL)
                        return "close", message
                    case "previous":
                        message = "🔙  Volviendo al menu"
                        return "previous", message
            return selected_text, f"✅ Elegiste: {selected_text}"
        # print(index)
        except KeyboardInterrupt:
            message = info("⏹  Interrumpido por el usuario con Ctrl+C", False)
            end_program(message)
        except EOFError:
            message = "\n⏹  Entrada terminada inesperadamente"
            end_program(message)
        except Exception as e:
            message = f"Error inesperado: {type(e).__name__}: {e}"
            end_program(message)
