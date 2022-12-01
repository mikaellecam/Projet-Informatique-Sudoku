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
            segements(Fichier,a,b,c)
        
        elif forme[index] == 'polygone' : 
            a = float(input('coord'))
            b = rgb(str(input('rgb')))
            polygone(Fichier,a,b)

def rectangle(Fichier ,cord1 , cord2 ,rgb):
    cord1 = list(cord1) 
    cord2 = list(cord2)
    l = int(cord2[0]-cord1[0])
    L = int(cord2[1]-cord1[1])
    l= abs(l)
    L = abs(L)
    for index1 in range (l):
        for index2 in range (L):
            if 0<index1<int(Fichier[1][0]) and 0<index2<int(Fichier[2][0]):
                Fichier[index2+4][index1] = rgb


Fichier = createfile(1024,1024)
cercle(Fichier,(1000,1000),300,"blanc")

with open('Formes\output.ppm', 'w') as f:
    for i in range(4):
        f.write(Fichier[i][0]+ "\n")
    for k in range(4,int(Fichier[1][0])+4):
        for j in range(int(Fichier[2][0])):
            f.write(" ".join((str(Fichier[k][j][0]), str(Fichier[k][j][1]), str(Fichier[k][j][2]))) + "\n")
    f.close()
