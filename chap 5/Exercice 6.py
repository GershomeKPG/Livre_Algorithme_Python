def verifier(mot):
    liste=[]
    mot2=""
    for c in mot:
        liste.append(c)
    for c in reversed(liste):
        mot2=mot2+c
    if mot==mot2:
        return "vrai"
    else:
        return "Faux"
    
