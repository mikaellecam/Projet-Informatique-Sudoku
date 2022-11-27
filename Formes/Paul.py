from random  import randint
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
def segment(fichier, point1, point2, color='blanc',e=1):
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


def determinant(vec1, vec2):
    return vec1[0]*vec2[1] - vec2[0]*vec1[1]


def p_scalaire(vec1, vec2):
    return vec1[0] * vec2[0] + vec1[1] * vec2[1]


def point_inter(ligne1: tuple, ligne2: tuple):
    dy = (ligne1[0][0] - ligne1[1][0], ligne2[0][0] - ligne2[1][0])
    dx = (ligne1[0][1] - ligne1[1][1], ligne2[0][1] - ligne2[1][1])

    denom = determinant(dy, dx)
    if denom == 0:
        print("IMPOSSIBLE")
        return

    det = (determinant(*ligne1), determinant(*ligne2))
    y = determinant(det, dy) / denom
    x = determinant(det, dx) / denom
    return y, x

def point_inter1(point, vec, point1, vec1):
    if vec[0] == 0:
        pente1 = vec[1]/10**-20
    else:
        pente1 = vec[1] / vec[0]
    if vec1[0] == 0:
        pente2 = vec1[1]/10**-20
    else:
        pente2 = vec1[1] / vec1[0]


    temp_y = point1[1] + (point[0]-point1[0])*pente2
    #print(temp_y, coeff, point1[0], vec1, point[0] + coeff*vec1[1], w)
    #print(point1[0]+point[0]-point1[0])
    #print(point1[1] + (point[0]-point1[0])*pente2)
    #print(pente2*11)
    #print(pente2, pente1, vec, vec1)
    x = (point[1] - temp_y) / (pente2 - pente1)
    y = pente1 * x + point[0]
    #if pente2 != 0:
     #   return x + point[1], y
    return y, x + point[1]


def polygone(fichier: list, coords: list, color: str):
    """
    fonction qui permet d'ajouter un polygone à n sommets, de la couleur donnée en paramètre
    :param fichier: fichier (liste) dans lequel ajotuer le polygone
    :param coords: liste des coordonnées des sommets du polygone (tuple[int])
    :param color: nom de la couleur utilisée pour le polygone
    :return: None
    """

    vecteurs = [] # on a les vecteurs de chaques segment
    # rajouter le sort au cas où les points ne sont pas donnés dans l'ordre
    for i in range(len(coords) - 1):
        vecteurs.append((coords[i+1][0]-coords[i][0],coords[i+1][1] - coords[i][1]))
        segment(fichier, coords[i], coords[i + 1], color)
    vecteurs.append((coords[0][0]-coords[len(coords)-1][0], coords[0][1] - coords[len(coords)-1][1]))
    segment(fichier, coords[len(coords)-1], coords[0], color)
    print(vecteurs)
    color = rgb(color)

    for i in range(1,20):
        for j in range(1, 20):
            vec = (i, j)
            cond = False
            for vec1 in vecteurs:
                #print(determinant(vec, vec1))
                if not determinant(vec, vec1):
                    cond = True
                    break
            if not cond:
                break
        if not cond:
            break
    print(vec, cond)



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

    #print(less_x, max_x, less_y, max_y)

    # On va ensuite utiliser une méthode pour pouvoir vérifier que le pixel parcouru est dans le polygone et donc
    # et savoir si il doit être colorié, pour ça on trace un segment(virtuel) et on compte le nombre de segments que
    # l'on rencontre si c'est impair alors on le colorie.
    coeff = max(abs(max_x[0] - less_x[0]), abs(max_y[1] - less_y[1]))
    for i in range(less_y[1]+4, max_y[1]+4):
        #print(i)
        for j in range(less_x[0], max_x[0]):

            if i > 3:
                #print("hahah", i, j)
                if fichier[i][j] != color:
                    compteur = 0
                    inters = []
                    """if 154 <= i <= 202 and 154 <= j <= 202:
                        print("~~~~~~~~~~~~~~")
                        print(j, i)"""
                    for k in range(-1, len(vecteurs)-1):
                        if vecteurs[k] is not None:
                            seg_point = coords[k+1]
                            if i <= max_y[1]:
                                inter = point_inter1((j,i), vec, coords[k], vecteurs[k])
                            else:
                                inter = point_inter1((j,i-4), vec, coords[k], vecteurs[k])
                            """if 154 <= i <= 202 and 154 <= j <= 202:

                                print("inter: ",inter)"""

                            if inter is not None:
                                """ if 154 <= i <= 202 and 154 <= j <= 202:
                                    print("hgh", coords[k], seg_point, vecteurs[k])
                                    print(i <= max_y[1])"""
                                inf = (min(coords[k][0], seg_point[0]), min(coords[k][1], seg_point[1]))
                                sup = (max(coords[k][0], seg_point[0]), max(coords[k][1], seg_point[1]))
                                if inf[0] <= inter[0] <= sup[0] and inf[1] <= inter[1] <= sup[1]:
                                    if vecteurs[k][0] <= 0 and vecteurs[k][1] <= 0:
                                        temp_coeff = -1
                                    else:
                                        temp_coeff = 1

                                    #if sup[0] >= inter[0]-(inf[0])*temp_coeff >= 0 and sup[1] >= inter[1]-(inf[1])*temp_coeff >= 0 and inter not in inters:
                                    if inter[0] - j >= 0 and inter[1]-i + 4*(i > max_y[1]) >= 0 and inter not in inters:
                                        """if 154 <= i <= 130 and 154 <= j <= 202:
                                            print("drrereerer")"""
                                        compteur += 1
                                inters.append(inter)
                    """if 154 <= i <= 202 and 154 <= j <= 202:
                        print(compteur)"""
                    if compteur % 2 == 1:
                        fichier[i][j] = color
                        #print(i,j,fichier[i][j])





def createfile(x, y):
    File = [["P3"], [str(x)], [str(y)], ["255"]]
    for i in range(y):
        File.append([rgb("noir")] * x)
    return File


# TODO La fonction dans laquelle on passe en paramètre une liste de formes et on les ajoute au fichier
# TODO faut aussi qu'on bascule toutes les fonctions de formes dans le fichier fonctions pour clear le main

Fichier = createfile(600, 300)
print(len(Fichier), len(Fichier[5]))
#cercle(Fichier, (512, 206), 200, "blanc")
#polygone(Fichier, [(150,100), (200,200), (100,200)], "rouge")
polygone(Fichier, [(100,100), (200,100), (200,200), (150,250), (100,200)], "rouge")
#print(point_inter1((166,143), (19,19)), ())
#segment(Fichier, (100,100), (200,100), "rouge")

with open('output.ppm', 'w') as f:
    for i in range(4):
        f.write(Fichier[i][0] + "\n")
    for k in range(4, int(Fichier[2][0]) + 4):
        for j in range(int(Fichier[1][0])):
            f.write(" ".join((str(Fichier[k][j][0]), str(Fichier[k][j][1]), str(Fichier[k][j][2]))) + "\n")
    f.close()
