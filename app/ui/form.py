"""
Script: form.py

Funciones para validar las entradas de usuario y agruarlas antes de hacer algos con los datos

TODO: todos los Examples estan desactualizados de las clases anteriores, hay que actualizar un poco
"""

from app.ui.config import SYMBOL
from app.ui.message import error, info, warning
from app.utils.close_app import end_program


def get_product_name():
    """
    Solicita el usuario el nombre del producto con opcion para cancelar.

    El usuario puede ingresar el nombre del producto o '0' para salir. Maneja errores como interrupciones con `Ctrl + C` o fin de entrda (EOF). devuelve una tupla que
    indica si la accion fue valida o si el proceso fue cancelado/interrumpido.

    Returns:
        tuple[str, str] or None:
            - ("ok", nombre): Si se ingreso un nombre valido.
            - ("exit", mensaje): Si el usuario interrumpio o cancelo el proceso)
            - None: Si hay algun fallo inesperado (muy poco probable)

    Side Effects:
        - Solicita entrada al usuario con `input`
        - Muestra mensajes en conosola con `print`

    Warnings:
        - En algunas aplicacionones como Warp terminal lanza un eror inesperado al usar `CTRL + C`

    Example:
        >>> get_product_name() # doctest: +SKIP
        ("ok", "abaco")
        >>> get_product_name() # doctest: +SKIP
        ("exit", "El proceso fue interrumpido por CTRL + C)

    See Also:
        - [Excepciones en python](https://docs.python.org/es/3.13/library/exceptions.html)
    """
    while True:
        try:
            name = input(f"Nombre del producto\n{SYMBOL} ").strip().lower()

            if not name:
                print(
                    warning(
                        "Ingrese el nombre del producto para continuar, 0 para cancelar y salir"
                    )
                )
                continue
            if name == "0":
                message = info("↩ Volviendo al menú principal")
                print(message)
                return "previous", message

            return "ok", name

        except KeyboardInterrupt:
            message = "Interrumpido por el usuario con Ctrl+C"
            print(info(f"⏹ {message}", False))
            end_program()
            # return ("exit", message)
        except EOFError:
            message = "Entrada terminada inesperadamente"
            print(info(f"\n⏹  {message}"), False)
            end_program()
            # return ("exit", message)


def get_product_description():
    """
    Solicita el usuario una descripcion del producto con opcion para cancelar.

    El usuario puede ingresar una descripcion o '0' para salir. Maneja errores como interrupciones con `Ctrl + C` o fin de entrda (EOF). devuelve una tupla que indica si la accion fue valida o si el proceso fue cancelado/interrumpido.

    Returns:
        tuple[str, str] or None:
            - ("ok", descripcion): Si se ingreso un nombre valido.
            - ("exit", mensaje): Si el usuario interrumpio o cancelo el proceso)
            - None: Si hay algun fallo inesperado (muy poco probable)

    Side Effects:
        - Solicita entrada al usuario con `input`
        - Muestra mensajes en conosola con `print`

    Warnings:
        - En algunas aplicacionones como Warp terminal lanza un eror inesperado al usar `CTRL + C`

    Example:
        >>> get_product_description() # doctest: +SKIP
        ("ok", "abaco de madera fabricacion artesanal color rojo")
        >>> get_product_description() # doctest: +SKIP
        ("exit", "El proceso fue interrumpido por CTRL + C)

    See Also:
        - [Excepciones en python](https://docs.python.org/es/3.13/library/exceptions.html)
    """
    while True:
        try:
            description = input(f"Descripcion\n{SYMBOL} ").strip().lower()
            if description == "":
                return None, description
            if not description:
                print(
                    warning(
                        "Ingrese una descripcion para poder continuar, 0 para cancelar"
                    )
                )
                continue
            if description == "0":
                message = info("↩ Volviendo al menú principal")
                print(message)
                return "previous", message

            return "ok", description
        except KeyboardInterrupt:
            message = "Interrumpido por el usuario con Ctrl+C"
            print(info(f"⏹ {message}", False))
            end_program(message)
            # return ("exit", message)
        except EOFError:
            message = "Entrada terminada inesperadamente"
            print(info(f"⏹ {message}", False))
            end_program(message)


def get_product_brand():
    """
    Solicita al usuario la marca de producto con opcion para cancelar.

    El usuario puede ingresar la marca del producto o '0' para salir. Maneja errores como interrupciones con `Ctrl + C` o fin de entrda (EOF). devuelve una tupla que indica si la accion fue valida o si el proceso fue cancelado/interrumpido.

    Returns:
        tuple[str, str] or None:
            - ("ok", marca): Si se ingreso una marca valida.
            - ("exit", mensaje): Si el usuario interrumpio o cancelo el proceso)
            - None: Si hay algun fallo inesperado (muy poco probable)

    Side Effects:
        - Solicita entrada al usuario con `input`
        - Muestra mensajes en conosola con `print`

    Warnings:
        - En algunas aplicacionones como Warp terminal lanza un eror inesperado al usar `CTRL + C`

    Example:
        >>> get_product_brand() # doctest: +SKIP
        ("ok", "abakitos")
        >>> get_product_brand() # doctest: +SKIP
        ("exit", "El proceso fue interrumpido por CTRL + C)

    See Also:
        - [Excepciones en python](https://docs.python.org/es/3.13/library/exceptions.html)
    """
    while True:
        try:
            brand = input(f"Marca\n{SYMBOL} ").strip().lower()
            if not brand:
                print(
                    warning("Ingrese la marca para continuar, 0 para cancelar y salir")
                )
                continue
            if brand == "0":
                message = info("↩ Volviendo al menú principal")
                print(message)
                return "previous", message
            return "ok", brand
        except KeyboardInterrupt:
            message = "Interrumpido por el usuario con Ctrl+C"
            print(info(f"⏹ {message}", False))
            end_program()
            # return ("exit", message)
        except EOFError:
            message = "Entrada terminada inesperadamente"
            print(info(f"\n⏹  {message}"), False)
            end_program()
            # return ("exit", message)


def get_product_quantity():
    """
    Solicita al usuario la cantidad de unidades del producto
    """
    while True:
        try:
            quantity = input(f"Cantidad\n{SYMBOL} ").strip()
            if quantity == "":
                return None, quantity
            if not quantity:
                print(
                    warning(
                        "Ingrese la cantidad de productos por Und, o 0 para cancelar"
                    )
                )
                continue
            if quantity == "0":
                message = info("↩ Volviendo al menú principal")
                print(message)
                return "previous", message

            if not quantity.isdigit():
                message = "Ingrese un numero que represente la cantidad"
                print(warning(message))
                continue

            quantity_to_int = int(quantity)
            if quantity_to_int > 0:
                return "ok", quantity_to_int
            else:
                message = "Ingrese un valor mayor a 0"
                print(warning(message))
                continue
        except KeyboardInterrupt:
            message = "Interrumpido por el usuario con Ctrl+C"
            print(info(f"⏹ {message}", False))
            end_program()
        except EOFError:
            message = "Entrada terminada inesperadamente"
            print(info(f"\n⏹  {message}"), False)
            end_program()
        except Exception as e:
            message = f"Error inesperado: {type(e).__name__}: {e}"
            print(info(f"\n⏹  {message}"), False)
            end_program()


def get_category():
    """
    Solicita al usuario la categoria del producto
    """
    while True:
        try:
            category = input(f"Categoria\n{SYMBOL} ").strip().lower()

            if not category:
                print(warning("Ingrese la categoria del produto, o 0 para cancelar"))
                continue
            if category == "0":
                message = info("↩ Volviendo al menú principal")
                print(message)
                return "previous", message
            return "ok", category
        except KeyboardInterrupt:
            message = "Interrumpido por el usuario con Ctrl+C"
            print(info(f"⏹ {message}", False))
            end_program()
            # return ("exit", message)
        except EOFError:
            message = "Entrada terminada inesperadamente"
            print(info(f"\n⏹  {message}"), False)
            end_program()
        except Exception as e:
            message = f"Error inesperado: {type(e).__name__}: {e}"
            print(info(f"\n⏹  {message}"), False)
            end_program()


def get_price():
    """
    Solicita al usuario el precio por unidad del producto
    """
    while True:
        try:
            price = input(f"Precio\n{SYMBOL}").strip()
            if price == "":
                return None, price

            if not price.isdigit():
                print(warning("Ingrese el precio del producto, o 0 para cancelar"))
                continue
            if price == "0":
                message = "Cancelando el programa"
                end_program(message)

            if price.isdigit():
                try:
                    price_to_float = float(price)
                    if price_to_float < 0:
                        message = "El precio no puede ser negativo"
                        print(error(message))
                        continue
                    return "ok", price_to_float
                except ValueError:
                    message = "Precio invalido. Debe ser un numero valido"
                    print(error(message))
                except Exception as e:
                    message = f"Error inesperado: {type(e).__name__}: {e}"
                    print(error(message))
        except KeyboardInterrupt:
            message = "Interrumpido por el usuario con Ctrl+C"
            print(info(f"⏹ {message}", False))
            end_program()
            # return ("exit", message)
        except EOFError:
            message = "Entrada terminada inesperadamente"
            print(info(f"\n⏹  {message}"), False)
            end_program()
        except Exception as e:
            message = f"Error inesperado: {type(e).__name__}: {e}"
            print(info(f"\n⏹  {message}"), False)
            end_program()
