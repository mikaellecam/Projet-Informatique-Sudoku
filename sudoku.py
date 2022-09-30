from fonctions import verifier_bloc,verifier_ligne,verify_column,est_complete

# N = int(input("Taille de grille: "))
grille = [[1,4,3,2], [3,2,0,4], [4,1,2,3], [2,3,4,1]]
grille_test_aresoudre = [[0,1,0,0], [0,4,0,0], [0,0,0,0], [1,0,0,4]]

def generationgrille(N):
    pass

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
