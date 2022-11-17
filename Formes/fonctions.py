def rgb(name):
    if name in ["blanc","rouge",'bleu',"vert","jaune","magenta","cyan"]:
        name.lower()
        if name == "blanc":
            return (255,255,255)
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
    for i in range(x):
        for j in range(y):
            File.append("0 0 0")
    return File