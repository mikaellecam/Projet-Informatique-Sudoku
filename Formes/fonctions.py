
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

    for i in range(x - rayon, x + rayon):
        for j in range(y - rayon, y + rayon):
            if 0 <= i < len(fichier[5]) and 0 <= j < len(fichier[5]):
                if (x - i) ** 2 + (y - j) ** 2 <= rayon**2:
                    if fichier[i][j] is not rgb("noir"):
                        fichier[i][j] = colormixer(fichier[i][j],color)
                    else:
                        fichier[i][j] = color



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
                if fichier[j+4][i] is not rgb("noir"):
                    fichier[j+4][i] = colormixer(fichier[j+4][i],couleur)
                else:
                    fichier[j+4][i] = couleur

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
        print(largeur)

        for i in range(min(x1,x2),max(x1,x2)):
            for j in range(min(y1,y2), max(y1,y2)):
                if 0<=i<int(fichier[1][0]) and 0<=j<int(fichier[2][0]):
                    if int(pente*i - j + origine) in largeur:
                        fichier[j+4][i] = couleur
                        for k in range(e):
                            fichier[j+4+k][i] = couleur


def determinant(vec1, vec2):
    return vec1[0]*vec2[1] - vec2[0]*vec1[1]


def p_scalaire(vec1, vec2):
    return vec1[0] * vec2[0] + vec1[1] * vec2[1]


def point_inter1(point, vec, point1, vec1):
    if vec[0] == 0:
        pente1 = vec[1]/10**-20
    else:
        pente1 = vec[1] / vec[0]
    if vec1[0] == 0:
        pente2 = vec1[1]/10**-20
    else:
        pente2 = vec1[1] / vec1[0]


    temp_y = point1[1] + (point[0]-point1[0])*pente2 #+ 4 #+ 4*(abs(-point[0]*pente2 + point[1] - (point1[1] + pente2*-point1[0]))/sqrt(1+pente2**2) < 2)
    x = (point[1]-4 - temp_y) / (pente2 - pente1)
    y = point[1]-4 + pente1 * x

    return x + point[0] , y
    #+ 1*(vec1[0] < 0 and vec1[1] < 0)


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

    print(less_x, max_x, less_y, max_y)

    # On va ensuite utiliser une méthode pour pouvoir vérifier que le pixel parcouru est dans le polygone et donc
    # et savoir si il doit être colorié, pour ça on trace un segment(virtuel) et on compte le nombre de segments que
    # l'on rencontre si c'est impair alors on le colorie.
    for i in range(less_y[1]+4, max_y[1]+4):
        for j in range(less_x[0], max_x[0]):
            if i > 3:
                if fichier[i][j] != color:
                    compteur = 0
                    inters = []
                    for k in range(-1, len(vecteurs)-1):
                        if vecteurs[k] is not None:
                            seg_point = coords[k+1]
                            if i <= max_y[1]:
                                inter = point_inter1((j,i), vec, coords[k], vecteurs[k])
                            else:
                                inter = point_inter1((j,i), vec, coords[k], vecteurs[k])

                            if inter is not None:
                                inf = (min(coords[k][0], seg_point[0]), min(coords[k][1], seg_point[1]))
                                sup = (max(coords[k][0], seg_point[0]), max(coords[k][1], seg_point[1]))

                                ###################################
                                if inter in inters  and inter[0] - j >= -0.75 and inter[1]-i + 4 >= 0:
                                    cond_temp = False
                                    for p in inters:
                                        if j - p[0] > 0 and i -4-p[1] > 0:
                                            if p[0] < inter[0] and p[1] < inter[1] and determinant(vec, (inter[0]-p[0],
                                                                                                         inter[1]-p[1])) <1:
                                                if less_x[0] <= p[0] <= max_x[0] and less_y[1] <= p[1] <= max_y[1]:
                                                    cond_temp = True
                                                    break
                                    if not cond_temp:
                                        compteur += 1
                                ##################################
                                elif inf[0] <= inter[0] <= sup[0] and inf[1] <= inter[1] <= sup[1]:
                                    if inter[0] - j >= -0.75 and inter[1]-i + 4 >= 0 and inter not in inters:
                                        compteur += 1

                                    inters.append(inter)

                    if compteur % 2 == 1:
                        fichier[i][j] = color

def ellipse(fichier, centre: tuple, grand, petit: float, color):
    
    color = rgb(color)
    cx,cy=centre
    for x in range(cx-grand,cx+grand):
        for y in range(cy-petit,cy+petit):
            verif= ((x-cx)**2)/(grand**2) + (((y-cy)**2)/(petit**2))
            print(verif)
            if 0 <= y < int(fichier[2][0]) and 0 <= x < int(fichier[1][0]):
                if (verif <= 1):
                    fichier[x][y]=color

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

def colormixer(color1,color2):
    r1,g1,b1 = color1
    r2,g2,b2 = color2
    r3,g3,b3 = 0,0,0

    if color1 in [rgb("rouge"),rgb("vert"),rgb('bleu')] and color2 in [rgb("rouge"),rgb("vert"),rgb('bleu')]:
        print("pass")
        return (r1+r2,g1+g2,b1+b2)
    elif color1 in [rgb("magenta"),rgb("cyan"),rgb("jaune")] and color2 in [rgb("magenta"),rgb("cyan"),rgb("jaune")]:
        if r1 == 255 and r2 == 255:
            r3 = 255
        if g1 == 255 and g2 == 255:
            g3 = 255
        if b1 == 255 and b2 == 255:
            b3 = 255
        return (r3,g3,b3)
    else:
        return (int((r1+r2)/2),int((g1+g2)/2),int((b1+b2)/2))



def createfile(x,y):
    File = [["P3"], [str(x)], [str(y)], ["255"]]
    for i in range(x):
        File.append([rgb("noir")]*y)
    return File