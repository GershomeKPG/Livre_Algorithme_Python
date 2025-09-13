num=int(input("Saisir un nombre : "))

for l in range(0,2):
    numb=int(input("Saisir un nombre : "))
    if numb>num:
        num=numb
print("Le grand nombre est",num)


num1=int(input("Saisir un nombre : "))
num2=int(input("Saisir un nombre : "))
num3=int(input("Saisir un nombre : "))

if num1>num2:
    numbsup=num1
else:
    numbsup=num2
if num3>numbsup:
    numbsup=num3
print("Le grand nombre est",numbsup)
