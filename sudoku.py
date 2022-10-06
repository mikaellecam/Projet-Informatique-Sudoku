from fonctions import *
import random

grille = [[1,4,3,2], [3,2,0,4], [4,1,2,3], [2,3,4,1]]
grille_test_aresoudre = [[0,1,0,0], [0,4,0,0], [0,0,0,0], [1,0,0,4]]

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

G = generationgrille(4)
print(afficher(G))
print(afficher(resolution(G)))
