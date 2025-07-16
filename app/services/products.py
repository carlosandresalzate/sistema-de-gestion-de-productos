"""
Script: productos.py

Set de fuciones CRUD
"""

from datetime import datetime
from app.ui.message import success, warning


def create_product(conn, product, table):
    """
    Agrega un producto en la base de datos en la tabla correspondiente

    Args:
        conn (sqlite3.Connection): inicio de la coneccion a la base de datos
        product (dict): producto que se agrega a la base de datos
        table (str): Nombre de la tabla a usar

    Returns:
        str: mensaje de confirmacion del producto agregado.
    """
    cursor = conn.cursor()
    cursor.execute(
        f"""
        INSERT INTO {table} (name, description, brand, quantity, category, price) VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            product["name"],
            product.get("description"),
            product.get("brand"),
            product["quantity"],
            product.get("category"),
            product["price"],
        ),
    )
    conn.commit()
    return success(f"{product['name']} agregado")


def read_all_products(conn, table, is_active=1):
    """
    Lee todos los productos en la base de datos y los visualiza en pantalla los productos activos

    Args:
        coon (sqlite3.Connection): coneccion a la base de datos
        table (str): nombre de la tabla a usar
        is_active (int): por defecto muestra los productos activos, o con 0 muestra los productos inactivos

    Returns:
        tupla: listado de productos [activos/inactivos] en la base de datos
    """
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table} WHere is_active = ?", (is_active,))
    return cursor.fetchall()


def update_product(conn, product_id, table, updates):
    """
    Actualiza campos especificos de un producto en la base de datos

    Args:
        conn (sqlite3.Connection): conexion activa a la base de datos
        product_id (int): ID unico del producto a modificar
        table (str): Nombre de la tabla donde esta el producto.
        updates (dict): Diccionario con campos a actualizar (eje. {"price": 12.5})

    Returns:
        bool: si se actualiza al menos un registro retorna True de lo contrario retorna false

    """
    if not updates:
        message = warning(
            "No se ingresaron campos para actualizar. Operación cancelada."
        )
        print(message)
        return False

    fields = ", ".join([f"{k} = ? " for k in updates])
    values = list(updates.values())
    values.append(product_id)

    cursor = conn.cursor()
    cursor.execute(
        f"""
        UPDATE {table} SET {fields} WHERE id = ? AND is_active = 1
        """,
        values,
    )
    conn.commit()
    return cursor.rowcount > 0


def delete_product(conn, product_id, table):
    """
    Realiza un borrado del producto (soft delete) y marca la fecha de eliminacion

    Args:
        conn (sqlite3.Connection): connecion a la base de datos
        product_id (int): ID de el producto a eliminar
        table (str): Nombre de la tabla a usar
    """
    cursor = conn.cursor()
    now = datetime.now().isoformat(timespec="seconds")
    cursor.execute(
        f"""
        UPDATE {table} SET is_active = 0, delete_at = ? WHERE id = ? AND is_active = 1
        """,
        (
            now,
            product_id,
        ),
    )
    conn.commit()
    return cursor.rowcount > 0


def hard_delete_product(conn, product_id, table):
    """
    Elimina completamente un producto de la base de datos (borrado fisico).

    Args:
        conn (sqlite3.Connection): coneccion a la base de datos
        product_id (int): Identificador unico del producto a borrar
        table (str): nombre de la tabla en la base de datos

    Returns:
        TODO: agregar
    """
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table} WHERE id = ?", (product_id,))
    conn.commit()
    return cursor.rowcount > 0


def search_by_id(conn, table, product_id):
    """
    Busca por ID en la tabla seleccionada

    Args:
        conn (sqlite3.Connection):
        table (str):
        product_id (int):

    Returns:
        tuple:
    """
    cursor = conn.cursor()
    cursor.execute(
        f"""
        SELECT * FROM {table} 
        WHERE ID = ? AND is_active = 1
        """,
        (product_id,),
    )
    return cursor.fetchone()


def search_by_name(conn, table, name):
    """
    Busca por nombre en la tabla seleccionada

    Args:
        conn (sqlite3.Connection):
        table (str):
        name (str):

    Returns:
        tuple:
    """
    cursor = conn.cursor()
    cursor.execute(
        f"""
            SELECT * FROM {table}
            WHERE name LIKE ? AND is_active = 1
        """,
        (f"%{name}%",),
    )
    return cursor.fetchall()


def search_by_category(conn, table, category):
    """
    Busca por categoria en la tabla seleccionada

    Args:
        conn (sqlite3.Connection):
        table (str):
        category (str):

    Returns:
        list:
    """
    category = category.strip().lower()
    cursor = conn.cursor()
    cursor.execute(
        f"""
        SELECT * FROM {table}
        WHERE category LIKE ? AND is_active = 1
        """,
        (f"%{category}%",),
    )
    return cursor.fetchall()


def map_products_for_display(products):
    """
    Filtra y reordena los datos de productos para mostrar en tabla.

    Args:
        products (list[tuple]): Lista completa de productos (con todas las columnas)

    Returns:
        list[tuple]: Lista con tuplas que contienen solo los datos deseados
    """
    return [(p[0], p[1], p[2], p[6], p[4]) for p in products]
