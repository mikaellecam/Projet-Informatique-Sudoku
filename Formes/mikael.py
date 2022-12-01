from math import sqrt
from fonctions import *

def createfile(x,y):
    File = [["P3"], [str(x)], [str(y)], ["255"]]
    for i in range(y):
        File.append([rgb("noir")]*x)
    return File

def rgb(name):
    if name in ["blanc", "noir", "rouge",'bleu',"vert","jaune","magenta","cyan"]:
        name.lower()
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

def colormixer(color1,color2):
    r1,g1,b1 = color1
    r2,g2,b2 = color2
    r3,g3,b3 = 0,0,0
    if r1-r2 == 0:
        r3 = 255
    if g1-g2 == 0:
        g3 = 255
    if b1-b2 == 0:
        b3 = 255
    return (r3,g3,b3)

print(colormixer(rgb("magenta"),rgb("jaune")))

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
                if (x - i) ** 2 + (y - j) ** 2 <= rayon**2: 
                    fichier[i][j] = color
                    #print(fichier[i][j])

                         
def rectangle(fichier,point1,point2,color):
    """
    Fonction permettant de rajouter un cercle basé sur deux points, le premier qui est en haut à droite et le
    deuxième qui en bas à gauche.
    :param fichier: fichier dans lequel on rajoute le rectangle
    :param point: coordonnée de la valeur en haut à gauche
    :param longueur: la longueur du rectangle
    :param largeur: la largeur du rectangle
    :param color: la couleur (str)
    """
    couleur = rgb(color)
    x1,y1 = point1
    x2,y2 = point2

    for i in range(min(x1,x2),max(x1,x2)):
        for j in range(min(y1,y2),max(y1,y2)):
            if 0<=i<int(fichier[1][0]) and 0<=j<int(fichier[2][0]):
                fichier[j+4][i] = couleur


def segment(fichier, point1, point2, color='blanc',e=1):
    couleur = rgb(color)
    x1,y1 = point1
    x2,y2 = point2

    if abs(x2) == abs(x1):
        for j in range(min(y1,y2), max(y1,y2)+1):
                fichier[j+4][x1] = couleur
                for k in range(e):
                    fichier[j+4][x1+k] = couleur
    elif abs(y2) == abs(y1):
        for i in range(min(x1,x2),max(x1,x2)+1):
                if 0<=i<int(fichier[1][0]):
                    fichier[y1+4][i] = couleur
                    for k in range(e):
                        fichier[y1+4+k][i] = couleur
    else:
        pente = (y2-y1)/(x2-x1)
        origine = y1 - pente*x1
        largeur = [_ for _ in range(int(abs(pente))+e)]
        print(largeur)

        for i in range(min(x1,x2),max(x1,x2)+1):
            for j in range(min(y1,y2), max(y1,y2)+1):
                if 0<=i<int(fichier[1][0]) and 0<=j<int(fichier[2][0]):
                    if int(pente*i - j + origine) in largeur:
                        fichier[j+4][i] = couleur



Fichier = createfile(1024,1024)

segment(Fichier,(100,100),(200,100),"rouge")

segment(Fichier,(100,200),(100,100),"rouge")

segment(Fichier,(100,200),(200,200),"rouge")

segment(Fichier,(200,200),(200,100),'magenta')


with open('Formes\output.ppm', 'w') as f:
    for i in range(4):
        f.write(Fichier[i][0]+ "\n")
    for k in range(4,int(Fichier[2][0])+4):
        for j in range(int(Fichier[1][0])):
            f.write(" ".join((str(Fichier[k][j][0]), str(Fichier[k][j][1]), str(Fichier[k][j][2]))) + "\n")
    f.close()