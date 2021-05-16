""" moduuli, joka sisältää kuvanlataus funktion.
"""
import os
import pygame
DIRNAME = os.path.dirname(__file__)
def load_image(filename):
    """ Lataa kuvan pygame kirjaston avulla
    Args:
        filename: Merkkijonoarvo, joka kertoo kuvatiedoston nimen.
    """
    return pygame.image.load(os.path.join(DIRNAME, "assets", filename))
