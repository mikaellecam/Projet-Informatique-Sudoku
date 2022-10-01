from fonctions import verifier_bloc,verifier_ligne,verify_column,est_complete
import random

# N = int(input("Taille de grille: "))
grille = [[1,4,3,2], [3,2,0,4], [4,1,2,3], [2,3,4,1]]
grille_test_aresoudre = [[0,1,0,0], [0,4,0,0], [0,0,0,0], [1,0,0,4]]


def afficher(G):
    affichage = "------------------"
    for k in range(len(G)):
        affichage += f"\n| {G[k][0]} | {G[k][1]} || {G[k][2]} | {G[k][3]} |"
        if k == 1:
            affichage += "\n------------------"
        affichage += "\n" + "-"*(len(G)**2 + 2)
    return affichage

# print(afficher(grille))

def verification(G):
    for k in range(len(G)):
        if not verifier_ligne(G, k):
            return False
        if not verifier_bloc(G, k):
            return False
        if not verify_column(G, k):
            return False
        """ if not est_complete(G): # ce bloc casse la résolution, y aura toujours des 0 avant
                                   # d'avoir trouvé une solution donc on peut pas le mettre
            return False"""
    return True
# print(verification(grille))

def generationgrille(N):
    nb = random.randint(abs(N//3 - 1), N//3) # on ne rempli qu'a peu près 1/3 de la grille au préalable (difficulté)
    grid = [[0]*N for _ in range(N)] # ambiguité de python on ne peut pas écrire [[0]*N]*N (a cause de la mutabilitée)
    i = 0
    while i < nb:
        x, y = (random.randint(0, N-1), random.randint(0, N-1))
        #print(x,y, grid[x][y], i)
        if grid[x][y] == 0:
            i += 1
            print(i)
            grid[x][y] = random.randint(0, N)
    if not verification(grid):
        return generationgrille(N)
    return grid

#print(generationgrille(4))

def resolution(G):
    verif = verification(G)
    if len(G) == 0 or not verif:
        return None
    if est_complete(G):
        return afficher(G)
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] == 0:
                x, y = i, j
    for k in range(1,len(G)+1):
        G[x][y] = k
        res = resolution(G)
        if res != None:
            return res


# print(resolution(grille))
print(resolution(grille_test_aresoudre))
