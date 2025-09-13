def supprimer_doublons_trier(liste):
  
  ensemble = set(liste)

  liste_sans_doublons = sorted(list(ensemble))

  return liste_sans_doublons


liste_o = input("entrer une suite de nombre")
liste=[]
for i in liste_o:
	liste.append(i)
liste_sans_doublons = supprimer_doublons_trier(liste)

print(f"Liste originale : {liste_o}")
print(f"Liste sans doublons : {liste_sans_doublons}")

