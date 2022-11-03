from math import sqrt
import random

def afficher(grille):
    """
    fonction qui permet d'afficher de manière propre une grille de sudoku
    :param G: la grille à afficher
    :return: None
    """
    G = remplacage0(grille)
    size = int(sqrt(len(G)))
    if G is None:
        print("None")
        return
    if len(G) == 4:
        affichage = "---------"*size
        for i in range(len(G)):
            if i == size:
                affichage += "\n"+ "---------"*size
            affichage += "\n"
            for j in range(len(G)):
                if (i,j) in coords:
                    affichage += f"| \033[1;31m{G[i][j]}\033[1;37m "
                else:
                    affichage += f"| {G[i][j]} "
                if j % 2 == 1:
                    affichage += "|"
            affichage += "\n"+ "---------"*size
    print(affichage)


def remplacage0(G):
    A = [x[:] for x in G]
    for i in range(len(G)):
        for j in range(len(G)):
            if A[i][j] == 0:
                A[i][j] = ' '
    return A


def verifier_bloc(G,i):
    """
    fonction qui vérifie qu'un bloc donné respecte bien les règles du sudoku
    :param G: la grille utilisée
    :param i: indice du bloc(numéro en partant d'en haut a gauche vers en bas à droite)
    :return: bool
    """
    x, y = (i//sqrt(len(G))*sqrt(len(G))),(i%sqrt(len(G))*sqrt(len(G)))
    coords = [(x+i, y+j) for j in range(int(sqrt(len(G)))) for i in range(int(sqrt(len(G))))]
    l = []
    for pos in coords:
        a,b = list(map(int,pos))
        if 0 < G[a][b] <= len(G):
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
        if 0 < x <= len(G):
            if x not in l:
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
        if 0 < G[i][j] <= len(G):
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
        x, y = random.randint(0, N - 1), random.randint(0,N - 1)  # positions random dans lesquelles on enlève le chiffre
        if res[x][y]:
            res[x][y] = 0  # on remplace le chiffre par un 0
            nbactuel -= 1  # on a retiré un nombre donc on décrémente de 1 le nombre actuel
    return res


def coordsfix(Grille):
    """
    Fonction qui créer un dictionnaire des coordonnées et des valeurs des cases imposées par la génération de grille.
    Ce qui permet de fixer les cases non modifiable
    :param Grille: La grille qu'on regarde
    :return: dictionnaire
    """
    dic = {}
    for i in range(len(Grille)):
        for j in range(len(Grille)):
            if Grille[i][j] != 0:
                dic[(i,j)] = Grille[i][j]
    return dic


def mettre_valeur(Grille):
    afficher(Grille)
    if est_complete(Grille):
        print("Bravo tu as complété la grille!")
        rep = input("Veux tu rejouer? (Y,N): ")
        if rep == 'Y':
            return jouer()
        else:
            print("Merci d'avoir joué")
            return None
    case = input("Selectionner une case(écrit comme ceci: i,j où i c'est les lignes et j les colonnes): ")
    try:
        i = int(case[0])-1;j = int(case[2])-1
        if i < 0 or j < 0:
            print(f"Le(s) chiffre(s) des coordonnées ou de la valeur ne sont pas dans l'intervalle correspondant: [1,{len(Grille)}]")
            return mettre_valeur(Grille)
        if (i,j) in coords:
            print("Les coordonnées sélectionnées correspondent à une valeur pas modifiable")
            print(i,j)
            return mettre_valeur(Grille)
        valeur = int(input("Quelle valeur voulez vous mettre dans cette case: "))
        Grille[i][j] = valeur
        if valeur not in [0,1,2,3,4]:
            print("La valeur n'est pas dans l'intervalle [0,4].")
            Grille[i][j] = 0
            return mettre_valeur(Grille)
        if verification(Grille):
            return mettre_valeur(Grille)
        else:
            print("Cette valeur ne peut pas être placé ici")
            Grille[i][j] = 0
            return mettre_valeur(Grille)
    except ValueError:
        print("Le(s) chiffre(s) des coordonnées ou de la valeur ne sont pas des nombres")
        return mettre_valeur(Grille)
    except IndexError:
        print(f"Le(s) chiffre(s) des coordonnées ou de la valeur ne sont pas dans l'intervalle correspondant: [1,{len(Grille)}]")
        return mettre_valeur(Grille)


def jouer():
    try:
        taille = 2
        difficulte = int(input("Quelle difficulté souhaitez vous de 1 à 3: "))
        Grille = gen_grille(taille**2,difficulte-1)
        global coords
        coords = coordsfix(Grille)
        return mettre_valeur(Grille)
    except ValueError:
        print("Les chiffres entrées ne sont pas des valeurs valables")
        return jouer()
    except IndexError:
        print("La difficulté n'est pas dans l'intervalle [1,3]")
        return jouer()

