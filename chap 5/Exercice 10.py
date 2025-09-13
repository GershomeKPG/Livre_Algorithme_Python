def echanger_cles_valeurs(dictionnaire):
  dictionnaire_inverse = {}
  for cle, valeur in dictionnaire.items():
    dictionnaire_inverse[valeur] = cle
  return dictionnaire_inverse
dictionnaire = {"anglais": "english", "français": "french"}
dictionnaire_inverse = echanger_cles_valeurs(dictionnaire)
print(f"Dictionnaire original : {dictionnaire}")
print(f"Dictionnaire inversé : {dictionnaire_inverse}")