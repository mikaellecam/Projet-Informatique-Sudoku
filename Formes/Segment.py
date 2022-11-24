#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:44:35 2022

@author: k22015223
"""
from math import sqrt



def segment(entete,fichier, coords1, coords2: tuple, color: tuple):
    longueur=int(entete[1])
    largeur=int(entete[2])
    
    if coords1[1]<coords2[1]:
        x1,y1=coords1 #x1 y1 plus en haut
        x2,y2=coords2
    else:
        x1,y1=coords2
        x2,y2=coords1
    print(x1)
    if x1<largeur and x2<largeur and y1<longueur and y2<longueur:
        if x1==x2:
            for i in range(y1,y2):
                fichier[x1][i]= color
                print(fichier[x1][i])
                print(i)
        elif y1==y2:
            for i in range(min(x1,x2),max(x1,x2)):
                fichier[i][y1]= color
        else:
            a=-(y1-y2)/(x1-x2)

            for i in range(y1,y2):
                for j in range(-largeur//2,largeur//2):
                    if (abs(a*(x1+j)+i)/abs(sqrt(a**2+1)))<0.5:
                        fichier[x1+j][i]=color
                if a<0 and x1<largeur and fichier[x1][y1+i]!=color:
                    x1=x1+1

                elif a>0 and x1>0 and fichier[x1][y1+i]!=color :
                    x1=x1-1
                   
                        

                    
                    
def rgb(name):
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
def createfile(x,y):
    File = ["P3", str(x), str(y), "255"]
    F=[]
    for i in range(x):
        F.append([rgb("noir")]*y)
    return F,File

Fichier, entete = createfile(256,256)
#mettre tests ici
segment(entete,Fichier, (150,150), (255,255), (255,255,255))
with open('output.ppm', 'w') as f:
    for i in range(4):
        f.write(str(entete[i])+ "\n")
    for k in range(int(entete[2])):
        for j in range(int(entete[1])):
            f.write(" ".join((str(Fichier[k][j][0]), str(Fichier[k][j][1]), str(Fichier[k][j][2]))) + "\n")
    f.close()
