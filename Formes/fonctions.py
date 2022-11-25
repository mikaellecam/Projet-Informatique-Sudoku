from math import *

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

    color = (str(color[0]), str(color[1]), str(color[2]))
    for i in range(x - rayon, x + rayon):
        for j in range(y - rayon, y + rayon):
            if 0 <= i < len(fichier[5]) and 0 <= j < len(fichier[5]):
                if sqrt((x - i) ** 2 + (y - j) ** 2) <= rayon:
                    fichier[i][j] = color
                    #print(fichier[i][j])

def segment(fichier, point1, point2, color='blanc',e=1):
    """
    Une fonction qui prends un compte deux points et qui produit le segment sur de ces deux points.
    :param fichier: fichier qu'on modifie pour ajouter le segment
    :param point1: le premier point du segment
    :param point2: le deuxième point du segment
    :param color: la couleur en string
    :param e: la largeur du segment, définit à 1 par défaut
    """
    couleur = rgb(color)
    x1,y1 = point1
    x2,y2 = point2

    if abs(x2) == abs(x1):
        for j in range(min(y1,y2), max(y1,y2)):
                fichier[j+4][x1] = couleur
                for k in range(e):
                    fichier[j+4][x1+k] = couleur
    elif abs(y2) == abs(y1):
        for i in range(min(x1,x2),max(x1,x2)):
                if 0<=i<int(fichier[1][0]):
                    fichier[y1+4][i] = couleur
                    for k in range(e):
                        fichier[y1+4+k][i] = couleur
    else:
        pente = (y2-y1)/(x2-x1)
        origine = y1 - pente*x1
        largeur = [_ for _ in range(int(abs(pente))+e)]

        for i in range(min(x1,x2),max(x1,x2)):
            for j in range(min(y1,y2), max(y1,y2)):
                if 0<=i<int(fichier[1][0]) and 0<=j<int(fichier[2][0]):
                    if int(pente*i - j + origine) in largeur:
                        fichier[j+4][i] = couleur

def rgb(name):
    """
    Fonction qui prends en paramètre un nom de couleur et la convertis en un tuple (red,green,blue)
    """
    name.lower()
    if name in ["blanc", "noir", "rouge",'bleu',"vert","jaune","magenta","cyan"]:
        if name == "blanc":
            return (255,255,255)
        elif name == "noir":
            return (0,0,0)
        elif name == "rouge":
            return (255,0,0)
        elif name == "bleu":
            return (0,0,255)
        elif name == "vert":
            return (0,255,0)
        elif name == "jaune":
            return (255,255,0)
        elif name == "magenta":
            return (255,0,255)
        elif name == "cyan":
            return (0,255,255)
    else:
        print("Le nom de la couleur n'est pas reconnu")
        return (0,0,0)
        
def createfile(x,y):
    File = [["P3"], [str(x)], [str(y)], ["255"]]
    for i in range(x):
        File.append([rgb("noir")]*y)
    return File