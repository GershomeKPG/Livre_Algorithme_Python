def trouver_mot_le_plus_long(phrase):
  """
  Fonction qui recherche le mot le plus long dans une phrase.

  Args:
    phrase (str): La phrase à analyser.

  Returns:
    Le mot le plus long de la phrase.
  """

  # Séparation de la phrase en mots
  mots = phrase.split()

  # Initialisation du mot le plus long
  mot_le_plus_long = ""

  # Parcours de chaque mot
  for mot in mots:
    # Comparaison de la longueur du mot actuel avec celle du mot le plus long
    if len(mot) > len(mot_le_plus_long):
      # Le mot actuel devient le mot le plus long
      mot_le_plus_long = mot

  return mot_le_plus_long

# Exemple d'utilisation
phrase = input("Entrez une phrase : ")
mot_le_plus_long = trouver_mot_le_plus_long(phrase)

print(f"Le mot le plus long de la phrase est : {mot_le_plus_long}")