from fonctions import *

#t = [[2,3,1,4],[0,4,0,0,],[0,1,4,0],[0,0,0,1]]
"""t = [[1,0,2,0], [2,4,0,3], [3,0,4,0], [0,0,0,2]]
afficher(resolution(t))"""


compteur = 0
L = []
for i in range(1000):
    G = gen_grille(4, 0)
    x = resolution(G)
    L.append(G.copy())
    if x is None:
        compteur += 1
    else:
        L.pop()
print(compteur)
print(L[0])


"""G = gen_grille(4, 0)
afficher(G)
afficher(resolution(G))
"""
"""G = generationgrille(4)
print(afficher(G))
print(afficher(resolution(G)))"""
