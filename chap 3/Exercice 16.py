#Exe 16 chap3

def EstPremier(nombre):
    validite=True
    for i in range(2,nombre):
       if nombre%i==0:
           validite=False
           break
    return validite

def EstValide(nombre):
    return str(nombre) in ['1','2','3','4','5','6','7']

CumulJoueur1=0
CumulJoueur2=0
termine=False
compt=1
pre1=False
pre2=False

while not termine:
    compt+=1
    val=False
    while not val:
        nombre=int(input("----Joueur "+str(compt%2+1)+"--\n Entrer le nombre : "))
        val=EstValide(nombre)
        if not val:
            print("Entrer un nombre valide (compris entre 1 et 7)")
    if compt%2==0:
        CumulJoueur1+=nombre
        if 100>CumulJoueur1>15:
            pre1=EstPremier(CumulJoueur1)
    else:
        CumulJoueur2+=nombre
        if 100>CumulJoueur2>15:
            pre2=EstPremier(CumulJoueur2)
    if pre1 or pre2:
        termine=True

print("__________Jeu Termine_________")
if pre1:
    print("Le joueur 1 a gagne")
else:
    print("Le joueur 2 a gagne")
