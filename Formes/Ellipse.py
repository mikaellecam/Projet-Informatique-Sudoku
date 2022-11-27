def ellipse(fichier, centre: tuple, grand, petit: float, color):
    
    color = rgb(color)
    cx,cy=centre
    for x in range(cx-grand,cx+grand):
        for y in range(cy-petit,cy+petit):
            verif= ((x-cx)**2)/(grand**2) + (((y-cy)**2)/(petit**2))
            print(verif)
            if 0 <= y < int(fichier[2][0]) and 0 <= x < int(fichier[1][0]):
                if (verif <= 1):
                    fichier[x][y]=color
                    #print("zbi")
                #else : print("pain")
    




def rgb(name):
    if type(name) == str:
        if name in ["blanc", "noir", "rouge",'bleu',"vert","jaune","magenta","cyan"]:
            name.lower()
            if name == "blanc":
                return (255,255,255)
            elif name == "noir":
                return (0,0,0)
            elif name == "rouge":
                return (255,0,0)
            elif name == "bleu":
                return (0,0,255)
            elif name == "vert":
                return (0,255,0)
            elif name == "jaune":
                return (255,255,0)
            elif name == "magenta":
                return (255,0,255)
            elif name == "cyan":
                return (0,255,255)
            else:
                return "Le nom de la couleur n'est pas reconnu"
    elif type(name)==tuple and len(name)==3:
        return name
    else: return "La couleur n'est pas reconnue" 
    
                   
def createfile(x, y):
    File = [["P3"], [str(x)], [str(y)], ["255"]]
    for i in range(y):
        File.append([rgb("noir")] * x)
    return File


# TODO La fonction dans laquelle on passe en paramètre une liste de formes et on les ajoute au fichier
# TODO faut aussi qu'on bascule toutes les fonctions de formes dans le fichier fonctions pour clear le main

Fichier = createfile(1024, 1024)
#print(len(Fichier), len(Fichier[5]))
#cercle(Fichier, (512, 206), 200, "blanc")
ellipse(Fichier,(500,360), 100,50, "rouge")
#print(point_inter1((166,143), (19,19)), ())
#segment(Fichier, (100,100), (200,100), "rouge")

with open('output.ppm', 'w') as f:
    for i in range(4):
        f.write(Fichier[i][0] + "\n")
    for k in range(4, int(Fichier[2][0]) + 4):
        for j in range(int(Fichier[1][0])):
            f.write(" ".join((str(Fichier[k][j][0]), str(Fichier[k][j][1]), str(Fichier[k][j][2]))) + "\n")
    f.close()
