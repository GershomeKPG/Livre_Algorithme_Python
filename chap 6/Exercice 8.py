

class book(object):
    " creation d'un livre"
    def __init__(self,titre,auteur,annee):
        self._titre=titre
        self._auteur=auteur
        self._annee=annee
    def getTitre(self):
        return self._titre
    def getAuteur(self):
        return self._auteur
    def getAnnee(self):
        return self._annee

class bibliotheque(object):
    "creation d'une bliotheque"
    def __init__(self,nom):
        self._nom=nom
        self._livres=self.data()
    def add_book(self,book):
        self._livres.append(book)
        self.saveData()
    def remove_book(self, book):
        self._livres.remove(book)
        self.saveData()
    def Find_book_by_author(self,author):
        livreAut=[]
        for bk in self._livres:
            if bk.getAuteur()==author:
                livreAut.append(bk)
        listeliv="Les livre de l'auteur "+author+" sont:\n"
        for liv in livreAut:
            listeliv+="-{},{}\n".format(liv.getTitre(),liv.getAnnee())
        return listeliv
    def Find_book_by_year(self,year):
        livreYear=[]
        for bk in self._livres:
            if bk.getAnnee()==year:
                livreYear.append(bk)
        listeliv="Les livre de l'annee "+str(year)+" sont:\n"
        for liv in livreYear:
            listeliv+="-{},{}\n".format(liv.getAuteur(),liv.getTitre())
        return listeliv
    def saveData(self):
        import pickle
        with open("data",'wb') as f:
            pickle.dump(self._livres,f)
    def data(self):
        import pickle
        dat=""
        with open("data",'rb') as f:
            dat=pickle.load(f)
        return dat
    
