from math import sqrt
from fonctions import *


def cercle(fichier, coords: tuple, rayon: float, color: str):
    """
    fonction permettant de rajouter un cercle de centre coords et d'un certain rayon, avec une certaine couleur
    :param fichier: fichier dans lequel rajouter le cercle
    :param coords: coordonnées du centre du cercle
    :param rayon: rayon du cercle
    :param color: couleur du cercle en format RGB (tuple)
    :return: None
    """
    x, y = coords
    color = rgb(color)

    for i in range(y - rayon, y + rayon):
        for j in range(x - rayon, x + rayon):
            if 0 <= i < int(fichier[2][0]) and 0 <= j < int(fichier[1][0]):
                if (y - i) ** 2 + (x - j) ** 2 <= rayon ** 2:
                    fichier[i][j] = color
                    # print(fichier[i][j])


# ça ne fonctionne pas très bien
def segment(fichier, coords1, coords2: tuple, color: tuple):
    longueur = int(fichier[1][0])
    largeur = int(fichier[2][0])

    if coords1[1] < coords2[1]:
        x1, y1 = coords1  # x1 y1 plus en haut
        x2, y2 = coords2
    else:
        x1, y1 = coords2
        x2, y2 = coords1

    if x1 < largeur and x2 < largeur and y1 < longueur and y2 < longueur:
        if x1 == x2:
            for i in range(y1, y2):
                fichier[x1][i] = color
                print(fichier[x1][i])
                print(i)
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)):
                fichier[i][y1] = color
        else:
            i = y1
            if x1 < x2:
                for j in range(x1, x2, 1):
                    fichier[i][j] = color
                    i += 1
            else:
                for j in range(x1, x2, -1):
                    fichier[i][j] = color
                    i += 1


def polygone(fichier: list, coords: list, color: str):
    """
    fonction qui permet d'ajouter un polygone à n sommets, de la couleur donnée en paramètre
    :param fichier: fichier (liste) dans lequel ajotuer le polygone
    :param coords: liste des coordonnées des sommets du polygone (tuple[int])
    :param color: nom de la couleur utilisée pour le polygone
    :return: None
    """
    color = rgb(color)
    # rajouter le sort au cas où les points ne sont pas donnés dans l'ordre
    for i in range(len(coords) - 1):
        segment(fichier, coords[i], coords[i + 1], color)

    # On détermine les coordonnées des extrémitées pour ensuite parcourir tous les pixels du polygone
    # et identifier ceux que l'on veut modifier
    less_x, max_x, less_y, max_y = [coords[0]] * 4
    for coord in coords:
        if coord[0] < less_x[0]:
            less_x = coord
        if coord[0] > max_x[0]:
            max_x = coord
        if coord[1] < less_y[1]:
            less_y = coord
        if coord[1] > max_y[1]:
            max_y = coord

    # On va ensuite utiliser une méthode pour pouvoir vérifier que le pixel parcouru est dans le polygone et donc
    # et savoir si il doit être colorié, pour ça on trace un segment(virtuel) et on compte le nombre de segments que
    # l'on rencontre si c'est impair alors on le colorie.
    for i in range(less_y[0], max_y[0]):
        for j in range(less_x[1], max_x[1]):
            if fichier[i][j] != color:
                compteur = 0
                # TODO adapter pour éviter d'avoir un segment dans la même direction que un coté.
                for k in range(i, max_x[0]):
                    if fichier[i][k] == color and fichier[i][k - 1] != color:
                        compteur += 1
                if compteur % 2 == 1:
                    fichier[i][j] = color



def rgb(name):
    if name in ["blanc", "noir", "rouge", 'bleu', "vert", "jaune", "magenta", "cyan"]:
        name.lower()
        if name == "blanc":
            return (255, 255, 255)
        elif name == "noir":
            return (0, 0, 0)
        elif name == "rouge":
            return (255, 0, 0)
        elif name == "bleu":
            return (0, 0, 255)
        elif name == "vert":
            return (0, 255, 0)
        elif name == "jaune":
            return (255, 255, 0)
        elif name == "magenta":
            return (255, 0, 255)
        elif name == "cyan":
            return (0, 255, 255)
    else:
        return "Le nom de la couleur n'est pas reconnu"


def createfile(x, y):
    File = [["P3"], [str(x)], [str(y)], ["255"]]
    for i in range(y):
        File.append([rgb("noir")] * x)
    return File


# TODO La fonction dans laquelle on passe en paramètre une liste de formes et on les ajoute au fichier
# TODO faut aussi qu'on bascule toutes les fonctions de formes dans le fichier fonctions pour clear le main

Fichier = createfile(1024, 1024)
cercle(Fichier, (512, 206), 200, "blanc")

with open('output.ppm', 'w') as f:
    for i in range(4):
        f.write(Fichier[i][0] + "\n")
    for k in range(4, int(Fichier[2][0]) + 4):
        for j in range(int(Fichier[1][0])):
            f.write(" ".join((str(Fichier[k][j][0]), str(Fichier[k][j][1]), str(Fichier[k][j][2]))) + "\n")
    f.close()
