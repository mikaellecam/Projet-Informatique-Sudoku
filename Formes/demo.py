#Fichier permettant l'affichage des figures sans besoin de taper les informations dans la console. 
from fonctions import *

Fichier = createfile(1024,1024)

###Rectangle###
"""
rectangle(Fichier,(100,100),(500,500),"magenta")
rectangle(Fichier,(700,650),(420,294),"jaune")
rectangle(Fichier,(700,700),(800,900),"vert")
rectangle(Fichier,(800,700),(900,900),"blanc")
rectangle(Fichier,(900,700),(1000,900),"rouge")
"""
###Cercle###
"""
cercle(Fichier,(500,500),300,"rouge")
cercle(Fichier,(900,900),200,"magenta")
cercle(Fichier,(200,300),100,"cyan")
"""

###Ellipse###
"""
ellipse(Fichier,(250,250),200,100,"jaune")
ellipse(Fichier,(700,700),150,50,"bleu")
ellipse(Fichier,(400,400),200,150,"rouge")
"""
###Segment###
"""
segment(Fichier,(300,300),(800,800),"rouge")
segment(Fichier,(650,800),(650,950),"vert",4)
segment(Fichier,(150,150),(750,150),"cyan",8)
"""
###Polygone###
#polygone(Fichier,[(300,300),(504,294),(294,573)],"cyan")



with open('Formes\output.ppm', 'w') as f:
    for i in range(4):
        f.write(Fichier[i][0]+ "\n")
    for k in range(4,int(Fichier[1][0])+4):
        for j in range(int(Fichier[2][0])):
            f.write(" ".join((str(Fichier[k][j][0]), str(Fichier[k][j][1]), str(Fichier[k][j][2]))) + "\n")
    f.close()
