"""
Script: feedback.py

Imprime mensaje en pantalla
"""

from colorama import Fore, Style

from app.ui.message import info, success, error


def show_edit_changes(original, updates):
    """
    Compara y muestra los valores viejos vs nuevos con colores.

    Args:
        original (tuple): producto roginal desde la DB
        update (dict): nuevos valores ingresados por el usuario
    """
    fields_map = {
        "description": (2, "Description"),
        "quantity": (4, "Cantidad"),
        "price": (6, "Precio"),
    }

    for field, (index, label) in fields_map.items():
        original_value = original[index]
        new_value = updates.get(field)

        original_str = str(original_value) if original_value is not None else "(vacio)"
        new_str = str(new_value) if new_value is not None else ""

        if new_value is not None:
            if new_value != original_value:
                red_value = error(f" - {original_str}", False)
                green_value = success(f"{new_str}")
                print(f"{label}: {red_value} → {green_value}\n")
            else:
                green_value = success(" - ", False)
                print(f"{label}: {green_value} (sin cambios)\n")
        else:
            red_value = error("(sin modificacion)", False)
            green_value = success(f"{original_str}", False)
            print(f"{label}: {green_value} → {red_value}\n")


def print_data_preview(data, title="Vista previa del contenido"):
    """
    Imprime un diccionario con formato alineado para mostrar en consola.

    Args:
        data (dict): Diccionario con formacto alineado para mostrar en consola.
        title (str): Titulo del bloque a mostrar (opcional)

    """
    # print(data)
    if not isinstance(data, dict):
        raise TypeError("Se esperaba un diccionario como entrada")

    print(info(f"🧾 {title}:\n"))

    max_key_len = max(len(str(k)) for k in data.keys())
    spacing = max_key_len + 2

    # Mostrar key para saber si obtengo value
    for key, value in data.items():
        label = f"{key}:".ljust(spacing)

        if key == "price":
            try:
                val_str = f"${float(value):,.2f}"
            except Exception:
                val_str = f"{value} (invalido)"

        elif key == "id" and (value is None or value == ""):
            val_str = f"{Fore.YELLOW}(a generar){Style.RESET_ALL}"
        else:
            val_str = str(value)

        print(f"{label}{val_str}")
