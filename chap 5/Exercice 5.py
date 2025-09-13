from cmath import*

equat=input("Entrer une equation ax^2+bx+c=0 : ")
eq=equat.split('x')
a=float(eq[0])
b=float(eq[1][2:])
c=float(eq[2][:-2])
det=b**2-4*a*c
det=sqrt(det)
x1=(-b+det)/(2*a)
x2=(-b-det)/(2*a)

result="l'equation {0} a pour racines x1={1} et x2={2}"
result=result.format(equat,x1,x2)
print(result)
