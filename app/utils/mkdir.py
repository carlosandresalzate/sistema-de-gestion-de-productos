"""
Script: mkdir.py

Crea carpetas o archivos

See Also:
    - [Crear direcorios y archivos](https://docs.python.org/3/library/pathlib.html#creating-files-and-directories)
"""

from pathlib import Path


def init_path(name, level=0):
    """
    Crea un directorio

    Args:
        name (str): Nombre del directorio
        level (int): Numero que define el nivel de creacion, por defecto es al mismo nivel del que es llamado por ultima vez
    """
    base_path = Path(__file__).resolve().parents[level]
    target_path = base_path / name
    target_path.mkdir(parents=True, exist_ok=True)
