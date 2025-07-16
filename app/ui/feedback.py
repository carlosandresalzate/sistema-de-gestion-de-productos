"""
Script: feedback.py

Imprime mensaje en pantalla
"""

from colorama import Fore, Style

from app.ui.message import success, error


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
