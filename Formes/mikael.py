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

    color = (str(color[0]), str(color[1]), str(color[2]))
    for i in range(x - rayon, x + rayon):
        for j in range(y - rayon, y + rayon):
            if 0 <= i < len(fichier[5]) and 0 <= j < len(fichier[5]):
                if (x - i) ** 2 + (y - j) ** 2 <= rayon**2: 
                    fichier[i][j] = color
                    #print(fichier[i][j])

#ça ne fonctionne pas très bien                    
def segment(fichier, coords1, coords2: tuple, color: tuple):
    
    longueur=int(fichier[1][0])
    largeur=int(fichier[2][0])
    
    if coords1[1]<coords2[1]:
        x1,y1=coords1 #x1 y1 plus en haut
        x2,y2=coords2
    else:
        x1,y1=coords2
        x2,y2=coords1
    
    if x1<largeur and x2<largeur and y1<longueur and y2<longueur:
        if x1==x2:
            for i in range(y1,y2):
                fichier[x1][i]= color
                print(fichier[x1][i])
                print(i)
        elif y1==y2:
            for i in range(min(x1,x2),max(x1,x2)):
                fichier[i][y1]= color
        else:
            i=y1
            if x1<x2:
                for j in range(x1,x2,1):
                    fichier[i][j]=color
                    i+=1
            else:
                for j in range(x1,x2,-1):
                    fichier[i][j]=color
                    i+=1
                         
def rectangle_dapresenoncé(fichier,point1,point2,color):
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
    longueur = x2 - x1
    largeur = y2 - y1

    for i in range(x1,x1+longueur+1):
        for j in range(y1,y1+largeur+1):
            if 0<=i<=int(fichier[1][0]) and 0<=j<=int(fichier[2][0]):
                fichier[j+4][i] = couleur

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

def createfile(x,y):
    File = [["P3"], [str(x)], [str(y)], ["255"]]
    for i in range(y):
        File.append([rgb("noir")]*x)
    return File

Fichier = createfile(512,512)
#cercle(Fichier,(16,16),10,"blanc")
rectangle_dapresenoncé(Fichier,(-10,-10),(600,300),"blanc")


with open('Formes\output.ppm', 'w') as f:
    for i in range(4):
        f.write(Fichier[i][0]+ "\n")
    for k in range(4,int(Fichier[2][0])+4):
        for j in range(int(Fichier[1][0])):
            f.write(" ".join((str(Fichier[k][j][0]), str(Fichier[k][j][1]), str(Fichier[k][j][2]))) + "\n")
    f.close()