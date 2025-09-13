print("-----Calcul de factoriel de n----")
nombre=0
fact=1
nombre=int(input("Entrer un nombre : "))
if nombre==0 or nombre==1:
    fact=1
    print("Le factoriel de", nombre, "est",fact)
elif nombre>0 :
    for nb in range(1,nombre+1):
        fact*=nb
    print("Le factoriel de", nombre, "est",fact)
else:
    print("Le factoriel de", nombre, "n'existe pas")

    
print("-----Produit de nombre pair n----")
nombre=0
fact=1
nombre=int(input("Entrer un nombre : "))
for nb in range(2,nombre+1,2):
    fact*=nb
print("Le factoriel de", nombre, "est",fact)

print("-----Les diviseur d'un nombre n----")
nombre=int(input("Entrer un nombre : "))
print("Les diviseurs de", nombre,"sont ", end =" ")
for nb in range(1,nombre+1):
    if nombre%nb==0:
        print(nb,end=",")

print("-----Le nombre parfait----")
somme=0
nombre=int(input("Entrer un nombre : "))

for nb in range(1,nombre):
    if nombre%nb==0:
        somme+=nb
if somme==nombre:
    print("Le nombre", nombre,"est parfait")
else:
    print("Le nombre", nombre,"n'est pas parfait")


print("----Nombre fort----")
nombre =int(input("Entrer un nombre"))
nbr=nombre
somme=0
if nombre <1000:
    ch1=nombre//100
    fact=1
    for nb in range(1,ch1+1):
        fact*=nb
    nombre=nombre-ch1*100
    somme+=fact
if nombre <100:
    ch2=nombre//10
    fact=1
    for nb in range(1,ch2+1):
        fact*=nb
    nombre=nombre-ch2*10
    somme+=fact
if nombre<10:
    ch3=nombre//1
    fact=1
    for nb in range(1,ch3+1):
        fact*=nb
    somme+=fact

if somme==nbr:
    print("le nombre",nbr,"est fort")
else:
    print("le nombre",nbr,"n'est pas fort")
    



