Etudiant=["Jospin",
          "Baraka",
          "Eugide",
         "Emma",
         "Marie",
         "Christophe",
         "Lucien"
          ]
UE=["Complexe",
    "Numerique",
   "Algorithme","Anglais",
    "Physique"]
Cote=[]
for ue in UE:
    print("----{}----".format(ue))
    lis=[ue]
    for et in Etudiant:
        point=float(input(et+" : "))
        lis.append(point)
    Cote.append(lis)
Cote=list(zip(*Cote))
#print(Cote)
moyenne=[]
for cot in Cote[1:]:
    moy=sum(cot)/len(UE)
    moyenne.append(moy)
pourcentage=[pts*5 for pts in moyenne]

#print(moyenne)
#print(pourcentage)

print(" "*10+"|",end="")
for ue in UE:
    print(f"{ue:^10}|",end="")
m="moyenne"
p="%"
print(f"{m:^10}|{p:^10}|")
print("-"*(len(UE)*14+15))
compt=0
for cote in Cote[1:]:
    print(f'''{Etudiant[compt]:<10}|{cote[0]:^10}|{cote[1]:^10}|{cote[2]:^10}|{cote[3]:^10}|{cote[4]:^10}|{moyenne[compt]:^10}|{pourcentage[compt]:^10}|''')
    print("-"*(len(UE)*14+15))
    compt+=1
