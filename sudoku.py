from fonctions import *
import random

grille = [[1,4,3,2], [3,2,0,4], [4,1,2,3], [2,3,4,1]]
grille_test_aresoudre = [[0,1,0,0], [0,4,0,0], [0,0,0,0], [1,0,0,4]]

def gen_grille(N, diff: int):
    grid = [[0]*N for _ in range(N)]
    diff_coefs = [0.25,0.35,0.5]
    t = [i for i in range(1,N+1)]
    x,y = random.randint(0,N-1), random.randint(0,N-1)
    res = None
    while res is None and len(t) > 0:
        indexe = random.randint(0,len(t)-1)
        grid[x][y] = t.pop(indexe)
        res = resolution(grid)
    if res is not None:
        nb = round(N**2*diff_coefs[diff])
        p = N**2
        while p > nb:
            x, y = random.randint(0, N - 1), random.randint(0, N - 1)
            if res[x][y]:
                res[x][y] = 0
                p -= 1
        return res
    return gen_grille(N, diff)




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



G = gen_grille(4, 1)
print(afficher(G))
"""G = generationgrille(4)
print(afficher(G))
print(afficher(resolution(G)))"""
