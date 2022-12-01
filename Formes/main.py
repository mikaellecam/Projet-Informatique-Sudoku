from fonctions import *

def main(Fichier ,forme : list,) :
    for index in range (len(forme)):
        if forme[index] == 'rectangle':
            a = float(input('coord1'))
            b = float(input('coord2'))
            c = rgb(str(input('rgb')))
            rectangle(Fichier,a,b,c)

        elif forme[index] == 'cercle' : 
            a = float(input('coord1'))
            b = int(input('rayon'))
            c = rgb(str(input('rgb')))
            cercle(Fichier,a,b,c)

        elif forme[index] == 'segements' :
            a = float(input('coord1'))
            b = float(input('coord2'))
            c = rgb(str(input('rgb')))
            segment(Fichier,a,b,c)
        
        elif forme[index] == 'polygone' : 
            a = float(input('coord'))
            b = rgb(str(input('rgb')))
            polygone(Fichier,a,b)


Fichier = createfile(1024,1024)
cercle(Fichier,(1000,1000),300,"blanc")

with open('Formes\output.ppm', 'w') as f:
    for i in range(4):
        f.write(Fichier[i][0]+ "\n")
    for k in range(4,int(Fichier[1][0])+4):
        for j in range(int(Fichier[2][0])):
            f.write(" ".join((str(Fichier[k][j][0]), str(Fichier[k][j][1]), str(Fichier[k][j][2]))) + "\n")
    f.close()
