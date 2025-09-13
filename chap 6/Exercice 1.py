## Chap6
#1 CompteBacaire

class CompteBacaire(object):
    "Creation des objets compte bacaire"
    def __init__(self,nom='Dupond',solde=1000):
        self._nom=nom
        self._solde=solde
    def setNom(self,nom):
        self._nom=nom
    def getNom(self):
        return self._nom
    def getSolde(self):
        return "Le solde est : {} $".format(self._solde)
    def depot(self,somme):
        self._solde+=somme
    def retrait(self,somme):
        if somme<=self._solde:
            self._solde-=somme
            return "Vous avez retire {} $ de votre compte \nle solde {} $".format(somme,self._solde)
        else :
            return "Solde insuffisant"
    def affiche(self):
        aff="Le solde du compte {0} est {1} $"
        return aff.format(self._nom,self._solde)

# Programme principal
if __name__=="__main__":
    comp1 = CompteBacaire('Romain',0) #creation d'un objet CompteBacaire
    comp1.depot(50)                 # depot de 50$ dans le comp1
    print(comp1.retrait(30))               # retrait de 60$
    print(comp1.affiche())                 #affiche les caracteristique du compte
