def compte_lettres(phrase):
  """
  Compte les occurrences de chaque lettre dans une phrase et retourne un dictionnaire avec les résultats.

  Args:
      phrase (str): La phrase à analyser.

  Returns:
      dict: Un dictionnaire avec les lettres comme clés et leurs occurrences comme valeurs.
  """
  lettres = {}
  for lettre in phrase:
    if lettre not in lettres:
      lettres[lettre] = 0
    lettres[lettre] += 1
  return lettres

# Demande à l'utilisateur de saisir une phrase
phrase = input("Entrez une phrase : ")

# Compte les occurrences des lettres
lettres = compte_lettres(phrase)

# Affiche les résultats
print("Occurrences des lettres dans la phrase :")
for lettre, occurrence in lettres.items():
  print(f"{lettre}: {occurrence}")
