# chap6 Ex2
class Satellite(object):
    "Simulation d'un satellite"
    
    def __init__(self,nom='Sat 2.0',masse=0,vit=0):
        self._nom=nom
        self._masse=masse
        self._vitesse=vit
    def getNom(self):
        return self._nom
    def setNom(self,nom):
        self._nom=nom
    def getVitesse(self):
        return self._vitesse
    def setVitesse(self,vit):
        self._vitesse=vit
    def getMasse(self):
        return self._masse
    def affiche_vitesse(self):
        aff= "Le satellite {} a pour vitesse {} m/s"
        return aff.format(self._nom,self._vitesse)
    def energie(self):
        energie=(self._masse*self._vitesse**2)/2
        aff="L'energie du satellite {} est {} Joule"
        return aff.format(self._nom,energie)
    def impulsion(self,force,duree):
        from random import randrange
        dv=(force*duree)/self._masse
        sign=randrange(1,3)
        self._vitesse=self._vitesse+((-1)**sign)*dv
        
 
