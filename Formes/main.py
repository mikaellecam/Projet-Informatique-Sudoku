from fonctions import *

taillex = int(input("Taille x de l'image: "));tailley = int(input("Taille y de l'image: "))
Fichier = createfile(taillex,tailley)

main(Fichier)


with open('Formes\output.ppm', 'w') as f:
    for i in range(4):
        f.write(Fichier[i][0]+ "\n")
    for k in range(4,int(Fichier[1][0])+4):
        for j in range(int(Fichier[2][0])):
            f.write(" ".join((str(Fichier[k][j][0]), str(Fichier[k][j][1]), str(Fichier[k][j][2]))) + "\n")
    f.close()


