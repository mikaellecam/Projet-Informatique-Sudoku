from fonctions import *

def main(Fichier):
    forme = input("Quelle forme voulez vous parmis: rectangle, ellipse, cercle, segment, polygone: ")
    print("Rentrez les coordonnées comme ceci: x,y.")
    if forme == 'rectangle':
        a = input('1er Point: ').split(","); a = (int(a[0]),int(a[1]))
        b = input('2e Point: ').split(","); b= (int(b[0]),int(b[1]))
        c = input('Couleur: ')
        rectangle(Fichier,a,b,c)
        return main(Fichier)


    elif forme == 'cercle': 
        a = input('Point de centre: ').split(","); a = (int(a[0]),int(a[1]))
        b = int(input('Rayon: '))
        c = input('Couleur: ')
        cercle(Fichier,a,b,c)
        return main(Fichier)


    elif forme == 'segment' :
        a = input('1er Point: ').split(","); a = (int(a[0]),int(a[1]))
        b = input('2e Point: ').split(","); b = (int(b[0]),int(b[1]))
        l = int(input("Largeur du segment (valeur de défaut = 1): "))
        c = input('Couleur: ')
        segment(Fichier,a,b,c,l)
        return main(Fichier)

    
    elif forme == 'polygone' : 
        nb = input("Nombre de points du polygone: ")
        a = []
        for i in range(1,nb+1):
            a.append(input(f"Coordonnée du Point {i}: "))
        b = input('Couleur: ')
        polygone(Fichier,a,b)
        return main(Fichier)
    
    elif forme == "ellipse":
        a = input("Point de centre: ").split(","); a = (int(a[0]),int(a[1]))
        b = int(input("Rayon vertical: "))
        c = int(input('Rayon horizontal: '))
        d = input("Couleur: ")
        ellipse(Fichier,a,b,c,d)
        return main(Fichier)
    
    elif forme == "":
        return None
    else:
        print("La forme n'est pas reconnue!")
        return main(Fichier)

Fichier = createfile(1024,1024)

main(Fichier)



with open('Formes\output.ppm', 'w') as f:
    for i in range(4):
        f.write(Fichier[i][0]+ "\n")
    for k in range(4,int(Fichier[1][0])+4):
        for j in range(int(Fichier[2][0])):
            f.write(" ".join((str(Fichier[k][j][0]), str(Fichier[k][j][1]), str(Fichier[k][j][2]))) + "\n")
    f.close()


