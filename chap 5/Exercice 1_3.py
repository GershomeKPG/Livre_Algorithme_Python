#Chapitre 5

#-------1
text=input("Entrer un texte : ")
if 'e' in text:
    print("e appartient a ce texte {}".format(text))
else:
    print("e n'appartient pas a ce texte {}".format(text))


#---------3
def compteCar(text,ch):
    return text.count(ch)
