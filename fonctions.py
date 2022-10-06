from math import sqrt
import random

def afficher(G):
    if G is None:
        return
    affichage = "------------------"
    for k in range(len(G)):
        affichage += f"\n| {G[k][0]} | {G[k][1]} || {G[k][2]} | {G[k][3]} |"
        if k == 1:
            affichage += "\n------------------"
        affichage += "\n" + "-"*(len(G)**2 + 2)
    return affichage


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

def generationgrille(N):
    nb = random.randint(abs((N**2)//3), (N**2)//3+1) # on ne rempli qu'a peu près 1/3 de la grille au préalable (difficulté)
    grid = [[0]*N for _ in range(N)] # ambiguité de python on ne peut pas écrire [[0]*N]*N (a cause de la mutabilitée)
    i = 0
    while i < nb:
        x, y = (random.randint(0, N-1), random.randint(0, N-1))
        #print(x,y, grid[x][y], i)
        if grid[x][y] == 0:
            i += 1
            grid[x][y] = random.randint(0, N)
    if not verification(grid):
        return generationgrille(N)
    return grid

def verification(G):
    for k in range(len(G)):
        if not verifier_ligne(G, k):
            return False
        if not verifier_bloc(G, k):
            return False
        if not verify_column(G, k):
            return False
    return True