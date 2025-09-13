print("Question 1")
def Add(Nbr1,Nbr2):
    result=Nbr1+Nbr2
    return result
def div(Nbr1,Nbr2):
    return Nbr1/Nbr2
def mod(Nbr1,Nbr2):
    return Nbr1%Nbr2
from math import * 
def expo(Nbr1):
    return exp(Nbr1)

print("----Question 6----")

from cmath import*
def resolution(a,b,c):
    delta=b**2-4*a*c
    x1=(-b+sqrt(delta))/(2*a)
    x2=(-b-sqrt(delta))/(2*a)
    return x1,x2

print("Resolution de l'equation ax**2+bx+c=0")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
resultat=resolution(a,b,c)
print("la solution de l'equation",a,"x**2+",b,"x+",c,"=0 est ",resultat,sep="")

rest=Add(3,8)
print(rest)

print("Question 11")

def SommeDiviseur(Nbr):
    somme=0
    for n in range(1,Nbr):
        if Nbr%n==0:
            somme+=n
    return somme

Max=int(input("Entrer un nombre : "))

for n in range(1,Max+1):
    sommeN=SommeDiviseur(n)
    for m in range(n+1,Max+1):
        sommeM=SommeDiviseur(m)
        if n==sommeM and m==sommeN:
            print("(",n,",",m,")",end=",")
        

print("Question 12")
print("Les nombre de Amstrong sont : ",end=" ")
def Cube(ch1):
    return pow(ch1,3)
def Chiffre(Nbre):
    ch1=Nbre//100
    ch2=(Nbre-ch1*100)//10
    ch3=Nbre-ch1*100-ch2*10
    return Cube(ch1)+Cube(ch2)+Cube(ch3)
for n in range(100,500):
    nb=Chiffre(n)
    if nb==n:
        print(n,end=",")
        
