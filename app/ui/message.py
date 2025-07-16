from colorama import Fore


def info(msg, emoji=True):
    """
    colorea mensaje de informacion para el usuario.

    Args:
        msg (str): mensaje de informacion que se desea colorear.
        emoji (bool): Por defecto muestra un emoji al inicio del string, o False no agrega el emoji

    Returns:
        str: Un string con la tipografia de color CYAN
    """
    if emoji:
        return f"ℹ  {Fore.CYAN}{msg}{Fore.RESET}"
    else:
        return f"{Fore.CYAN}{msg}{Fore.RESET}"


def success(msg, emoji=True):
    """
    colorea un mensaje de (success: traducir y mejorar)  para el usuario.

    Args:
        msg (str): mensaje de success que se desea colorear.
        emoji (bool): Por defecto muestra un emoji al inicio del string, o False no agrega el emoji

    Returns:
        str: Un string con la tipografia de color GREENN
    """
    if emoji:
        return f"✅ {Fore.GREEN}{msg}{Fore.RESET}"
    else:
        return f"{Fore.GREEN}{msg}{Fore.RESET}"


def warning(msg, emoji=True):
    """
    colorea un mensaje de (warning: traducir y mejorar)  para el usuario.

    Args:
        msg (str): mensaje de Warning que se desea colorear.
        emoji (bool): Por defecto muestra un emoji al inicio del string, o False no agrega el emoji

    Returns:
        str: Un string con la tipografia de color Yellow
    """
    if emoji:
        return f"⚠ {Fore.YELLOW}{msg}{Fore.RESET}"
    else:
        return f"{Fore.YELLOW}{msg}{Fore.RESET}"


def error(msg, emoji=True):
    """
    colorea un mensaje de (error: traducir y mejorar)  para el usuario.
    """
    if emoji:
        return f"❌ {Fore.RED}{msg}{Fore.RESET}"
    else:
        return f"{Fore.RED}{msg}{Fore.RESET}"
