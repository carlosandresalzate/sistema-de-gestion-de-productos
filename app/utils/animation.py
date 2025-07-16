"""
Script: animation.py

Set de animaciones UI (En Consturccion)
"""


def point_animated(duration=3):
    """
    Muestra una animacion de puntos suspensivos en consola simulando una carga.

    Esta funcion imprime una animacion con uno, dos y tres puntos ("...", como un loader o spinner) en una sola llinea, sobre escribiendo el contenido anterior, durante un diempo especificado en segundos.

    Args:
        Duration (int): Duracion total de la animacion en segundos. por defecto 3

    Returns:
        None

    Side Effects:
        - Imprime en consola (`stdout`) con efecto animado.
        - Modifica de la linea actual del cursos con `\r` y `sys.stdout.write`
        - Utiliza `sleep`, por lo que introduce un retardo real en la ejecucion.

    Warnings:
        - Esta animacion bloquea la ejecucion del programa durante su duracion.

    Example:
        >>> point_animated(2) #doctest: +SKIP
        # Imprime puntos animados como un loader durante 2 segundos

    See Also:
        - time.sleep: Para retardo de ejecucion.
        - sys.stdout.flush: Para forzar salida inmediata.
    """
    from time import time, sleep
    import sys
    from colorama import Fore

    points = [".  ", ".. ", "..."]
    start = time()

    while time() - start < duration:
        for p in points:
            sys.stdout.write(f"\r{Fore.BLUE + p}")
            sys.stdout.flush()
            sleep(0.5)
    sys.stdout.write(f"{Fore.RESET}\r" + "" * 20 + "\r")
