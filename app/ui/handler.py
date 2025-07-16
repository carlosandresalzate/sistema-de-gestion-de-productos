"""
Script: handler.py

Muestra el menu principal y maneja la navegacion
"""

from app.services.products import (
    create_product,
    delete_product,
    hard_delete_product,
    map_products_for_display,
    read_all_products,
    search_by_category,
    search_by_id,
    search_by_name,
    update_product,
)
from app.ui.config import FAREWELL, MAIN_MENU_OPTIONS, SEARCH_OPTIONS, SYMBOL
from app.ui.decorators import header
from app.ui.form import (
    get_category,
    get_price,
    get_product_brand,
    get_product_description,
    get_product_name,
    get_product_quantity,
)
from app.ui.menu import show_menu_options
from app.ui.message import error, info, warning
from app.ui.table import print_product_table
from app.utils.animation import point_animated
from app.utils.close_app import end_program
from app.utils.random_farewell import set_random_farewell


def handle_main_menu(conn, table):
    """
    Muestra el menu principal y maneja la navegacion

    Args:
        conn (sqlite3.Connection): enlace
        table (str): nombre de la tabla

    Returns:
        str: navigate opciones

    TODO: agregar la salida de cada caso, aun no  esta estructurada
    """
    selected_option, _ = show_menu_options(MAIN_MENU_OPTIONS, "Menu Principal")

    match selected_option:
        case "Agregar Producto":
            print(header("Agregar Producto", 2) + "\n")
            product = ask_new_product_date()
            if product == "previous":
                return

            create_product(conn, product, table)
            print("Agregar: ", type(product), " ", product)

        case "Mostrar Productos":
            print(header("Mostrar Productos", 2) + "\n")
            products = read_all_products(conn, table)
            display_products = map_products_for_display(products)
            print_product_table(display_products)

        case "Editar Producto":
            print(header("Editar Producto", level=3))
            header("Editar Producto", level=3)
            product_id = ask_product_id()
            print("product_id", product_id)
            if product_id == "None":
                return
            print("product_id: ", product_id)
            updates = ask_update_data()
            print("Editar: ", updates)
            update_product(conn, product_id, table, updates)

        case "Eliminar Producto (soft)":
            product_id = ask_product_id()
            delete_product(conn, product_id, table)
            print("eliminar soft: ", product_id)

        case "Eliminar Producto (hard)":
            product_id = ask_product_id()
            hard_delete_product(conn, product_id, table)
            print("Eliminar hard: ", product_id)

        case "Buscar Producto":
            product = handle_search_menu(conn, table)

        case "close":
            message = set_random_farewell(FAREWELL)
            print("selected", selected_option)
            end_program(message)

        case _:
            message = error("Opcion invalida")
            print(message)

    return "continue"


def handle_search_menu(conn, table):
    """
    Maneja el submenu de busqueda
    """

    selected_option, _ = show_menu_options(
        SEARCH_OPTIONS, "Busqueda", navigate="previous"
    )
    print("selected_option: ", selected_option)

    match selected_option:
        case "Buscar por ID":
            product_id = ask_product_id()
            product = search_by_id(conn, table, product_id)
            print(product)
        case "Buscar por Nombre":
            _, name = get_product_name()
            print("name ", _)
            if _ == "previous":
                return
            else:
                results = search_by_name(conn, table, name)
                print(results)
        case "Buscar por Categoria":
            _, category = get_category()
            results = search_by_category(conn, table, category)
            print(results)
        case "previous":
            message = info("↩ Volviendo al menú principal", False)
            print(message)
            point_animated(1)
            return
        case _:
            print("❌ Opción no válida")


def ask_new_product_date():
    """
    TODO: Agregar titulo y descripcion

    Returns:
        dict: la entidad...?
    """

    _, name = get_product_name()
    if _ == "previous":
        return "previous"
    _, description = get_product_description()
    if _ == "previous":
        return "previous"
    _, brand = get_product_brand()
    if _ == "previous":
        return "previous"
    _, quantity = get_product_quantity()
    if _ == "previous":
        return "previous"
    _, category = get_category()
    if _ == "previous":
        return "previous"
    _, price = get_price()
    if _ == "previous":
        return "previous"

    return {
        "name": name,
        "description": description,
        "brand": brand,
        "quantity": quantity,
        "category": category,
        "price": price,
    }


def ask_product_id():
    """
    ¿?
    Side Effects:
        - Pide una entrada al usuario con `input`
        - Muestra mensajes por consola con `print`

    TODO: faltan validaciones
    """
    while True:
        try:
            product_id = input(
                f"Ingrese el {info('ID', False)} del producto o {info('0', False)} para regresar\n{SYMBOL} "
            ).strip()
            if product_id.isdigit():
                if product_id == "0":
                    return

                product_id_to_number = int(product_id)
                return product_id_to_number
            else:
                message = warning("Ingrese un numero valido")
                print(message)
        except KeyboardInterrupt:
            message = info("⏹  Interrumpido por el usuario con Ctrl+C", False)
            end_program(message)
        except EOFError:
            message = "Entrada terminada inesperadamente"
            print(info(f"\n⏹  {message}"), False)
            end_program(message)
        except ValueError:  # Puede ser que esto aqui este de mas
            message = warning("Debe ser un numero entero")
            print(message)
            return message
        except Exception as e:
            message = error(e)
            print(message)
            return message


def ask_update_data():
    """
    ¿?
    Returns:
        dict:
    """
    updates = {}
    message = info("Deja vacio un campo si no quieres modificarlo")
    print(message)

    _, description = get_product_description()
    if description != "":
        updates["description"] = description

    _, quantity = get_product_quantity()
    if quantity != "":
        try:
            quantity = int(quantity)
            updates["quantity"] = quantity
        except ValueError:
            message = warning("Cantidad no válida, se ignora.")
            print(message)

    _, price = get_price()
    if price != "":
        try:
            price = float(price)
            updates["price"] = price
        except ValueError:
            print(warning("Precio no válido, se ignora."))

    return updates
