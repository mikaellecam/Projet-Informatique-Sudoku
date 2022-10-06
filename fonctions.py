from math import sqrt
import random


def afficher(G):
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
    l = []
    for x in G[i]:
        if 0<x<=4:
            if x not in l or x==0:
                l.append(x)
            else:
                return False
    return True


def verify_column(G,j):
    l = []
    for i in range(len(G)):
        if 0< G[i][j] <= 4:
            if G[i][j] not in l:
                l.append(G[i][j])
            else:
                return False
    return True


def est_complete(G):
    for k in range(len(G)):
        for i in range(len(G)):
            if G[k][i] == 0:
                return False
    return True


def afficherline(G,l):
    affichage = f"\n| {G[l][0]} | {G[l][1]} || {G[l][2]} | {G[l][3]} |"
    return affichage


def verification(G):
    for k in range(len(G)):
        if not verifier_ligne(G, k):
            return False
        if not verifier_bloc(G, k):
            return False
        if not verify_column(G, k):
            return False
    return True


def resolution(G):
    verif = verification(G)
    if len(G) == 0 or not verif:
        return None
    if est_complete(G):
        return G
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] == 0:
                x, y = i, j
    for k in range(1,len(G)+1):
        G[x][y] = k
        res = resolution(G)
        if res is not None:
            return res


def gen_grille(N, diff: int):
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
        nb = round(N**2*diff_coefs[diff]) #le nombre de chiffre qu'il nous reste dans la grille
        nbactuel = N**2 #c'est le nombre qu'il y a actuellement dans la grille
        while nbactuel > nb: 
            x, y = random.randint(0, N - 1), random.randint(0, N - 1) #positions random dans lesquelles on enlève le chiffre
            if res[x][y]:
                res[x][y] = 0 #on remplace le chiffre par un 0
                nbactuel -= 1 #on a retiré un nombre donc on décrémente de 1 le nombre actuel
        return res
    return gen_grille(N, diff) #Si nous n'avons pas trouvé de solution pour la position aléatoire, nous recommencons avec (normalement) une autre position