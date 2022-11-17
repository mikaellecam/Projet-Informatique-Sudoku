from math import sqrt
from PIL import Image

def cercle(fichier, coords: tuple, rayon: float, color: tuple):
    """
    fonction permettant de rajouter un cercle de centre coords et d'un certain rayon, avec une certaine couleur
    :param fichier: fichier dans lequel rajouter le cercle
    :param coords: coordonnées du centre du cercle
    :param rayon: rayon du cercle
    :param color: couleur du cercle en format RGB (tuple)
    :return: None
    """
    x, y = coords
    pixels = []
    for i in range(x-rayon, x+rayon):
        for j in range(y-rayon, y+rayon):
            if sqrt(i**2 + j**2) <= rayon:
                pixels.append(color)
            else:
                pixels.append((0, 0, 0))

