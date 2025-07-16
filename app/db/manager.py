"""
Script: manager.py


"""

import sqlite3
from pathlib import Path

from app.ui.message import info, success
from app.utils.mkdir import init_path

level = 2  # nivel en el que se va a crear la carpeta `data_dir_name`
data_dir_name = "data"
inventario_db_name = "inventario.db"


def is_data():
    """
    Define si la carpeta "data" existe y no la crea

    Returns:
        str(URL): la ruta a la carpeta data

    See Also:
        - init_path()
    """
    DB_PATH = Path(__file__).resolve().parents[level] / data_dir_name
    if DB_PATH.exists():
        print(success(f"La carpeta {data_dir_name}/ encontrada"))
        return DB_PATH
    else:
        print(info(f"La carpeta {data_dir_name}/ no existe y sera creada"))
        init_path(data_dir_name, level)
        return DB_PATH


def init_db():
    """
    Inicia la coneccion con la base de datos, si no existe la crea en una ubicacion especifica.

    Returns:
        ¿?
    """
    dir = is_data()
    if dir:
        DB_PATH = f"{dir}/{inventario_db_name}"
        return sqlite3.connect(DB_PATH)


def setup_schema():
    """
    Crea una tabla si no existe
    """
    conn = init_db()
    with conn as sqlite_conn:
        cursor = sqlite_conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                brand TEXT,
                quantity INTEGER NOT NULL CHECK (quantity >= 0),
                category TEXT,
                price REAL NOT NULL,
                create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                is_active BOOLEAN DEFAULT 1,
                delete_at DATETIME DEFAULT NULL
            )
        """)
        print(success(f"Tabla '{inventario_db_name}' iniciada exitosamente"))
        sqlite_conn.commit()
        return conn
