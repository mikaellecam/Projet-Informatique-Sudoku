from math import sqrt

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
        if x>0 and x<=4:
            if x not in l or x==0:
                l.append(x)
            else:
                return False
    return True

def verify_column(G,j):
    l = []
    for i in range(len(G)):
        if G[i][j] > 0 and G[i][j] <= 4:
            if G[i][j] not in l:
                l.append(G[i][j])
            else:
                return False
    return True

def afficherline(G,l):
    affichage = f"\n| {G[l][0]} | {G[l][1]} || {G[l][2]} | {G[l][3]} |"
    return affichage


def afficherline(G,l):
    affichage = f"\n| {G[l][0]} | {G[l][1]} || {G[l][2]} | {G[l][3]} |"
    return affichage