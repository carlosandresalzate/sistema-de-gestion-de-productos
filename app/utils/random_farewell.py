"""
Script: random_farewell.py

retorna una frase al azar a partir de una lista
"""

import random


def set_random_farewell(farewell):
    """
    Retrona una despedia al azar
    """
    phrase = random.choice(farewell)
    return phrase
