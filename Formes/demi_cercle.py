def demi_cercle(fichier, centre: tuple, rayon, direction, color):
    x, y = centre
    if direction == "bas":
        for i in range(x, x + rayon):
            for j in range(y - rayon, y + rayon):
                if 0 <= i < len(fichier[5]) and 0 <= j < len(fichier[5]):
                    if (x - i) ** 2 + (y - j) ** 2 <= rayon**2:
                        if fichier[i][j] is not rgb("noir"):
                            fichier[i][j] = colormixer(fichier[i][j],color)
                        else:
                            fichier[i][j] = color
    elif direction == "gauche":
        for i in range(x-rayon, x + rayon):
            for j in range(y - rayon, y):
                if 0 <= i < len(fichier[5]) and 0 <= j < len(fichier[5]):
                    if (x - i) ** 2 + (y - j) ** 2 <= rayon**2:
                        if fichier[i][j] is not rgb("noir"):
                            fichier[i][j] = colormixer(fichier[i][j],color)
                        else:
                            fichier[i][j] = color
    elif direction == "haut":
        for i in range(x, x - rayon):
            for j in range(y - rayon, y + rayon):
                if 0 <= i < len(fichier[5]) and 0 <= j < len(fichier[5]):
                    if (x - i) ** 2 + (y - j) ** 2 <= rayon**2:
                        if fichier[i][j] is not rgb("noir"):
                            fichier[i][j] = colormixer(fichier[i][j],color)
                        else:
                            fichier[i][j] = color
    elif direction == "droite":
        for i in range(x-rayon, x + rayon):
            for j in range(y, y + rayon):
                if 0 <= i < len(fichier[5]) and 0 <= j < len(fichier[5]):
                    if (x - i) ** 2 + (y - j) ** 2 <= rayon**2:
                        if fichier[i][j] is not rgb("noir"):
                            fichier[i][j] = colormixer(fichier[i][j],color)
                        else:
                            fichier[i][j] = color
    
