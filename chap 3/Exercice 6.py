
# Equation du second degre ax**2+bx+c=0
a=float(input("entre le coeficiant du terme en x au carre"))
b=float(input("celui pour le coeficiant en x"))
c=float(input("le terme indepandent"))
d=(b**2)-4*a*c
if d<0:
	print("Pas des racines reelles")
else:
	d=(d)**(1/2)
	x1=(-b+d)/(2*a)
	x2=(-b-d)/(2*a)
	print ("les racines de l'équation sont," "x1=",x1, "x2=",x2)
