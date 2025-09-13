###Resolution systeme d'equation

print("Equation :")
print("[ax+by=c")
print("|dx+ey=f")
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
d=int(input("d = "))
e=int(input("e = "))
f=int(input("f = "))
D=a*e-b*d
Dx=c*e-b*f
Dy=a*f-d*c
x=Dx/D
y=Dy/D
print("Equation :")
print("[",a,"x+",b,"y=",c,sep='')
print("|",d,"x+",e,"y=",f,sep='')
print("A pour racine le couple x=",x,'y=',y)
