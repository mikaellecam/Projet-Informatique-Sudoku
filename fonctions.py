from math import sqrt
import random

def afficher(G):
    """
    fonction qui permet d'afficher de manière propre une grille de sudoku
    :param G: la grille à afficher
    :return: None
    """
    if G is None:
        print("None")
        return
    affichage = "------------------"
    for k in range(len(G)):
        affichage += f"\n| {G[k][0]} | {G[k][1]} || {G[k][2]} | {G[k][3]} |"
        if k == 1:
            affichage += "\n------------------"
        affichage += "\n" + "-"*(len(G)**2 + 2)
    print(affichage)


def verifier_bloc(G,i):
    """
    fonction qui vérifie qu'un bloc donné respecte bien les règles du sudoku
    :param G: la grille utilisée
    :param i: indice du bloc(numéro en partant d'en haut a gauche vers en bas à droite)
    :return: bool
    """
    x,y = (i//sqrt(len(G))*sqrt(len(G))),(i%sqrt(len(G))*sqrt(len(G)))
    coords = [(x+i,y+j) for j in range(int(sqrt(len(G)))) for i in range(int(sqrt(len(G))))]
    l = []
    for pos in coords:
        a,b = list(map(int,pos))
        if 0 < G[a][b] <= 4:
            if G[a][b] not in l:
                l.append(G[a][b])
            else:
                return False
    return True


def verifier_ligne(G,i):
    """
    fonction qui vérifie si la ligne d'indice i respecte les règles du sudoku
    :param G: la grille utilisée
    :param i: l'indice de la ligne
    :return: bool
    """
    l = []
    for x in G[i]:
        if 0<x<=4:
            if x not in l or x==0:
                l.append(x)
            else:
                return False
    return True


def verify_column(G,j):
    """
    fonction qui vérifie qu'une colonne d'indice donné respecte les règles du sudoku
    :param G: la grille utilisée
    :param j: l'indice de la colonne
    :return: bool
    """
    l = []
    for i in range(len(G)):
        if 0< G[i][j] <= 4:
            if G[i][j] not in l:
                l.append(G[i][j])
            else:
                return False
    return True


def est_complete(G):
    """
    fonction qui permet de vérifier si une grille de sudoku ne comporte aucune case vide
    :param G: la grille à vérifier
    :return: bool
    """
    for k in range(len(G)):
        for i in range(len(G)):
            if G[k][i] == 0:
                return False
    return True


def afficherline(G,l):
    """
    fonction qui permet d'afficher une ligne d'indice donné
    :param G: la grille utilisée
    :param l: l'indice de la ligne
    :return: None
    """
    affichage = f"\n| {G[l][0]} | {G[l][1]} || {G[l][2]} | {G[l][3]} |"
    print(affichage)


def verification(G):
    """
    fonction qui utilise toutes les autres fonction de vérification pour savoir si la grille est correcte
    :param G: la grille à vérifier
    :return: bool
    """
    for k in range(len(G)):
        if not verifier_ligne(G, k):
            return False
        if not verifier_bloc(G, k):
            return False
        if not verify_column(G, k):
            return False
    return True


def resolution(G):
    """
    fonction qui va résoudre la grille donnée en respectant les règles du sudoku
    :param G: la grille (partiellement remplie) à résoudre
    :return: la grille complétée(list)
    """
    verif = verification(G)
    a = False
    if len(G) == 0 or not verif:
        return None
    if est_complete(G):
        return G
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] == 0:
                x, y = i, j
                a = True
                break
        if a:
            break
    for k in range(1,len(G)+1):
        G[x][y] = k
        res = resolution(G)
        if res is not None:
            return res
    G[x][y] = 0


def recursive_construct(N, grid=None):
    """
    Fonction récursive qui permet de placer un nombre aléatoire dans la grille donnée en paramètre, si elle est
    complète on la renvoie puisqu'elle est vraie. et on teste d'autres valeurs par cases au cas où il y aurait des
    problèmes, cette fonction à des probabilitées uniformes et exécute N^2 appels max
    :param N: longueur de la grille
    :param grid: la grille qu'il faut remplir
    :return: list
    """
    res = None
    if grid is None:
        grid = [[0]*N for _ in range(N)]
    if est_complete(grid): # si on rentre dans ce cas c'est que la grille est forcément résolue
        return grid        # donc on la renvoie
    x,y = random.randint(0,N-1), random.randint(0,N-1)
    while grid[x][y]:
        x, y = random.randint(0, N - 1), random.randint(0, N - 1)  # On choisie une pos aléatoire pour y mettre un nb
    t = [i for i in range(1,N+1)] # on génère les possibilitées de nb pour la case
    while len(t) > 0:
        grid[x][y] = t.pop(random.randint(0,len(t)-1)) # on remplace la case par le nombre choisi aléatoirement
        if verification(grid): # on vérifie que le coup respecte les règles
            res = recursive_construct(N,grid) # si oui on continue pour une autre case
        if res is not None: # si il est différent de None c'est qu'on a résolu la grille
            return res
    grid[x][y] = 0
    return None  # si jamais on a pas réussi on reset la case et on revient en arrière


def gen_grille(N, diff):
    """
    Fonction qui permet la création d'une grille de sudoku totalement aléatoire, et qui utilise recursive_construction
    pour générer une grille dont on sait qu'elle peut être résolue, puis on la vide en fonction de la diffcultée choisie
    :param N: longueur de la grille voulue
    :param diff: indice de difficultée
    :return: list
    """
    diff_coefs = [0.5, 0.35, 0.25]  # Coefficient de difficulté
    nb = round(
        N ** 2 * diff_coefs[diff])  # le nombre de chiffre dans la liste qu'on veut obtenir en fonction de la difficulté
    nbactuel = N ** 2  # c'est le nombre qu'il y a actuellement dans la grille
    res = recursive_construct(N)
    while nbactuel > nb:
        x, y = random.randint(0, N - 1), random.randint(0,
                                                        N - 1)  # positions random dans lesquelles on enlève le chiffre
        if res[x][y]:
            res[x][y] = 0  # on remplace le chiffre par un 0
            nbactuel -= 1  # on a retiré un nombre donc on décrémente de 1 le nombre actuel
    return res



def gen_grille_other(N, diff: int):
    """
    fonction qui génère une grille de sudoku en fonction de la difficultée donnée, cette grille aura toujours
    une solution
    :param N: la taille de la grille
    :param diff: l'indice de difficulté parmis [0,1,2]
    :return: la grille partiellement remplie à résoudre
    """
    grid = [[0]*N for _ in range(N)] #Grille vide
    diff_coefs = [0.5,0.35,0.25] #Coefficient de difficulté
    t = [i for i in range(1,N+1)] #Valeur entre 1 et 4 inclus
    x,y = random.randint(0,N-1), random.randint(0,N-1) #Position aléatoire de notre valeur aléatoire
    res = None
    while res is None and len(t) > 0: #Tant qu'on ne trouve pas de solution, on change le nombre aléatoire et recommence la résolution
        indexe = random.randint(0,len(t)-1) #Le nombre(aléatoire) qu'on met dans la grille
        grid[x][y] = t.pop(indexe) #on met le nombre qu'on a définit, et on l'enlève de la liste
        res = resolution(grid) #on essaie de résoudre
    if res is not None: #Si on trouve une solution
        nb = round(N**2*diff_coefs[diff]) #le nombre de chiffre dans la liste qu'on veut obtenir en fonction de la difficulté
        nbactuel = N**2 #c'est le nombre qu'il y a actuellement dans la grille
        while nbactuel > nb:
            x, y = random.randint(0, N - 1), random.randint(0, N - 1) #positions random dans lesquelles on enlève le chiffre
            if res[x][y]:
                res[x][y] = 0 #on remplace le chiffre par un 0
                nbactuel -= 1 #on a retiré un nombre donc on décrémente de 1 le nombre actuel
        return res
    return gen_grille_other(N, diff) #Si nous n'avons pas trouvé de solution pour la position aléatoire, nous recommencons avec (normalement) une autre position
