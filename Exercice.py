#Ex1 Somme de deux nombres
def Add(Nbr1=0,Nbr2=0):
    return Nbr1+Nbr2

#Ex2
def LigneCar(n=1,ca=""):
    compt=1
    ch=""
    while compt<=n:
        ch=ch+ca
        compt+=1
    return ch

#Exec3 surface d'un cercle

def SurfaceCercle(rayon):
    from math import pi
    
    sur = pi*rayon**2
    return sur

#Exerc5
def mult(nbr1=1,nbr2=1):
    return nbr1*nbr2
def div(nbr1=1,nbr2=1):
    if nbr2==0:
        return "Erreur division par 0"
    return nbr1/nbr2
def mod(nbr1=1,nbr2=1):
    return nbr1%nbr2
def signe(nbr=0):
    return -nbr
def fact(nbr):
    fac=1
    if nbr>1:
        for i in range(2,nbr+1):
            fac*=i
    elif nbr>=0:
        fac=1
    else:
        fac = "N'existe pas"
    return fac
def log(nbr):
    from math import log10
    if nbr<0:
        return "N'existe pas"
    return log10(nbr)
def ln(nbr):
    from math import log
    if nbr<0:
        return "N'existe pas"
    return log(nbr)
def expo(nbr):
    from math import e
    return e**nbr
def calculer(expression):
    return eval(expression)
def equation2(a,b,c):
    from cmath import sqrt
    delta=b**2-4*a*c
    x1=(-b+sqrt(delta))/(2*a)
    x2=(-b-sqrt(delta))/(2*a)
    sort = "l'equation : "+str(a)+"x^2+"+str(b)+"x+"+str(c)+"=0\n A pour racines:\n x1="+str(x1)+"\n x2="+str(x2)
    return sort
# Ex7 Nombre premier
def EstPremier(Nbre):
    for i in range(2,Nbre):
        if Nbre%i==0:
            return "Non"
    return "Oui"

def Premier(Nbre):
    for i in range(2,Nbre):
        if Nbre%i==0:
            return False
    return True
#Ex8
def FindPremier(start,stop):
    prem=""
    for i in range(start,stop+1):
        val=True
        for j in range(2,i):
            if i%j==0:
                val=False
                break
        if val:
            prem=prem+str(i)+" "
    sort ="La liste des nombres premier situe entre "+str(start)+" et "+str(stop)+" est :\n"+prem
    return sort

#Ex11 Nombre amis

def NbreAmi(start,stop):
    NbrAmi=""
    for i in range(start,stop+1):
        cumul1=0
        cumul2=0
        if Premier(i):
            continue
        for k in range(1,i):
            if i%k==0:
                cumul1+=k
        for j in range(i+1,stop):
            cumul2=0
            for t in range(1,j):
                if j%t==0:
                    cumul2+=t
            if cumul2==i and cumul1==j:
                NbrAmi=NbrAmi+"("+str(i)+","+str(j)+") "
                break       
    return "-----Nombre Ami-----\n"+NbrAmi

from math import e
termine="continue"
while termine != "fin":
    exp=input("---Effectuer un nouveau calcul---\n Expression : ")
    if exp=="fin":
        termine=exp
    else:
        print(calculer(exp))
print("----Terminer----")
        
