"""
Script: main.py

"""

from colorama import Fore
from app.db.manager import setup_schema
from app.ui.decorators import centered, divider, header
from app.ui.handler import handle_main_menu
from app.utils.close_app import end_program
# from app.utils.close_app import end_program


def main():
    # confimacion de la ubicacion de la base de datos
    conn = setup_schema()
    table = "productos"
    # Titulo de bienvenida
    # print(header("📦 BIENVENIDO A LA GESTIÓN DE PRODUCTOS 📦"))
    print(header("📦 GESTIÓN DE PRODUCTOS 📦", level=1, color=Fore.MAGENTA))
    print(
        centered(
            "Sistema de administración para productos de stock.", Fore.LIGHTWHITE_EX
        )
    )
    print(
        centered(
            "Cargá, buscá, editá y eliminá productos fácilmente.", Fore.LIGHTWHITE_EX
        )
    )
    print(divider())

    # print(boxed_text("hola mundo"))

    # Titulo
    while True:
        state = handle_main_menu(conn, table)
        print("state: ", state)
        if state == "close":
            end_program()


if __name__ == "__main__":
    main()
