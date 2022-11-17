from math import sqrt


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
    longueur = int(fichier[1])
    color = (str(color[0]), str(color[1]), str(color[2]))
    for i in range(x-rayon, x+rayon):
        for j in range(y-rayon, y+rayon):
            if 0 <= i * longueur + j <= len(fichier):
                if sqrt((x-i)**2 + (y-j)**2) <= rayon:

                    fichier[i*longueur + j] = f"{color[0]} {color[1]} {color[2]}" + "\n"
