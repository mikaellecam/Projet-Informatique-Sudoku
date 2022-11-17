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
                if sqrt((x - i) ** 2 + (y - j) ** 2) <= rayon:
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
                         

Fichier = createfile(1024,1024)
cercle(Fichier,(1000,1000),300,"blanc")

with open('Formes\output.ppm', 'w') as f:
    for i in range(4):
        f.write(Fichier[i][0]+ "\n")
    for k in range(4,int(Fichier[1][0])+4):
        for j in range(int(Fichier[2][0])):
            f.write(" ".join((str(Fichier[k][j][0]), str(Fichier[k][j][1]), str(Fichier[k][j][2]))) + "\n")
    f.close()
