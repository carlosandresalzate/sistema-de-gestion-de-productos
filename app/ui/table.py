"""
Script: table.py

Muestra una tabla de datos especificos
"""

# from app.ui.config import COLUMNS, MAX_COLUMN_WIDTHS


def print_product_table(products):
    """
    Imprime una tabla formateada con los productos.

    Args:
        products (list[tuple]): Lista de tuplas, cada una representa un producto
    """

    columns = ["id", "name", "description", "price", "quantity"]
    max_column_widths = {
        "id": 4,
        "name": 10,
        "description": 20,
        "price": 7,
        "quantity": 8,
    }

    # str_rows = [
    #     [str(item) if item is not None else "None" for item in row] for row in products
    # ]
    str_rows = []
    for row in products:
        str_row = []
        for i, item in enumerate(row):
            col_name = columns[i]
            val = str(item) if item is not None else "None"
            max_w = max_column_widths.get(col_name)
            if max_w and len(val) > max_w:
                val = val[: max_w - 3] + "..."
            str_row.append(val)
        str_rows.append(str_row)
    # print(str_rows)

    col_widths = [max_column_widths[col] for col in columns]
    # for i, col in enumerate(columns):
    #     max_len = len(col)
    #     for row in str_rows:
    #         max_len = max(max_len, len(row[i]))
    #     col_widths.append(max_len + 2)  # padding

    # Helpers
    def format_row(row):
        """
        Funcion auxiliar para centrar cada celda
        """
        return (
            "| "
            + " | ".join(row[i].center(col_widths[i]) for i in range(len(row)))
            + " |"
        )

    def separator():
        """
        Linea separadora
        Returns:
            str:
        """
        return "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

    # Tabla
    print(separator())
    print(format_row(columns))
    print(separator())
    for row in str_rows:
        print(format_row(row))
    print(separator())
