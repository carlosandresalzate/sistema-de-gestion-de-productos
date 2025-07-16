"""
Script: close_app.py

Cierra la aplicacion cuando se invoca
"""

import os
import sys

from app.ui.message import info
from app.utils.animation import point_animated


def end_program(message="Cancelando  el programa"):
    """
    Finaliza el progarma

    os.system("cls") No funciona en Warp para windows, desconozco en sistemas Unix
    """
    # sys.stdout.write("\n" + " " * len(message))
    # sys.stdout.flush()
    # os.system("cls" if os.name == "nt" else "clear")
    print(f"\n{info(message, False)}", end="\n", flush=True)
    point_animated(2)
    print("\n")
    os.system("cls")
    sys.exit(0)
    os.system("cls" if os.name == "nt" else "clear")
