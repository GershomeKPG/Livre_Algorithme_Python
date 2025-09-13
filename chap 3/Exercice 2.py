#exercice 2

num=int(input("Entrer le nombre : "))
while num%3!=0 or num%13!=0:
    print(num,"n'est pas divisible par 3 et par 13")
    num=int(input("Entrer le nombre : "))

print(num,"est divisible par 3 et par 13")
        
