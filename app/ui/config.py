"""
Script: config.py

contiene todas las variables globales para el modulo UI
"""

from app.ui.message import info


# Simbolo que alerta de una entrada de usuario
SYMBOL = info(">", False)

MAIN_MENU_OPTIONS = [
    "Agregar Producto",
    "Mostrar Productos",
    "Editar Producto",
    "Eliminar Producto (soft)",
    # "Eliminar Producto (hard)", # para borrar de la base de datos totalmente
    "Buscar Producto",
    "Salir",
]

SEARCH_OPTIONS = [
    "Buscar por ID",
    "Buscar por Nombre",
    "Buscar por Categoria",
    "Menu Principal",
]

FAREWELL = [
    "Hasta la vista 👋",
    "Nos vemos pronto 👀",
    "Cuídate mucho 🤗",
    "Hasta la próxima 🔜",
    "Que tengas un buen día ☀️",
    "Nos vemos en la próxima 📆",
    "Fue un gusto, ¡hasta luego! 🤝",
    "Chau, cuidate 🛵",
    "Hasta entonces ⏳",
    "Adiós, y buena suerte 🍀",
]

COLUMNS = [
    "id",
    "name",
    "description",
    "brand",
    "quantity",
    "category",
    "price",
    "create_at",
    "is_active",
    "delete_at",
]

MAX_COLUMN_WIDTHS = {"description": 30, "create_at": 20, "delete_at": 20}
