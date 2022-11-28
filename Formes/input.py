rep= str(input("Bienvenu(e) ! Voulez-vous créer quelque-chose aujourd'hui ? (y/n)  "))
formes=[]
first=True


while rep.lower()=="y":
    formeTest =False
    forme_cara=[]
    if first:
        forme=str(input("Quelle magnifique forme voulez-vous ajouter?  (Cercle - Segment - Rectangle - Polygone )"))
    else:
        forme= str(input("Pouvez-vous reformuler? "))
        
    while not formeTest:
        if (forme.lower() in ["cercle","segment","rectangle","polygone", "ellipse"]):
            print(f"La forme: '{forme}' sera dessinée")
            forme_cara.append(forme)
            formeTest=True
            first= True    
        else :
            print("Désolé, je ne reconnais pas cette forme.")
            first= False
            break
        
    if forme.lower()== "cercle":
        ...
    elif forme.lower()== "segment":
        ...
    elif forme.lower()== "rectangle":
        ...
    elif forme.lower()== "polygone":
        ...
    elif forme.lower()== "ellipse":
        ...
    else: "???"
    
    while formeTest:
        colorrep=str(input("Voulez-vous donnez une couleur en RGB ou le nom de la couleur?"))
        if colorrep.lower() == "rgb":
            color=(0,0,0)
            color[0]=int(input("Valeur de R"))
            color[1]=int(input("Valeur de V"))
            color[2]=int(input("Valeur de B"))
            if 0<=color[0]<=255 and 0<=color[1]<=255 and 0<=color[2]<=255:
                break
            else: print("Il y'a un problème avec votre couleur")
        else:
            color= str(input("Quel est le nom de la couleur?"))
            """if rgb(color)!="Le nom de la couleur n'est pas reconnu":
                break
            else: print("Il y'a un problème avec votre couleur")"""
    forme_cara.append(color)
    
            
    formes.append(forme_cara)
    rep = str(input("Voulez-vous continuer?"))
