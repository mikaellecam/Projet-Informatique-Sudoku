from fonctions import verifier_bloc,verifier_ligne,verify_column,est_complete

#N = int(input("Taille de grille: "))
grille = [[1,4,3,2],[3,2,0,4],[4,1,2,3],[2,3,4,1]]

def generationgrille(N):
    pass

def afficher(G):
    affichage = "------------------"
    for k in range(len(G)):
        affichage += f"\n| {G[k][0]} | {G[k][1]} || {G[k][2]} | {G[k][3]} |"
        if k==1:
            affichage += "\n------------------"
        affichage += "\n" + "-"*(len(G)**2 + 2)
    return affichage

#print(afficher(grille))

def verification(G):
    for k in range(len(G)):
        if not verifier_ligne(G,k):
            return False
        if not verifier_bloc(G,k):
            return False
        if not verify_column(G,k):
            return False
        if not est_complete(G):
            return False
    return True
#print(verification(grille))

def resolution(G):
    if len(G) == 0 or not verification(G):
        return None
    if verification(G):
        return afficher(G)
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] == 0:
                x,y = i,j
    for k in range(1,len(G)+1):
        G[x][y] = k
        res = resolution(G)
        if res != None:
            return res
        




print(resolution(grille))
