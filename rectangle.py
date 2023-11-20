#class Rectangle:
   # def _init_(self,older):
    #    self.longueur = older.longueur
     #   self.largeur = older.largeur
       

#class Rectangle:
    #def _init_(self):
       # self.longueur = 0
       # self.largeur = 0

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)

    def aire(self):
        return self.longueur * self.largeur

    def est_carre(self):
        return self.longueur == self.largeur

    def afficher_rectangle(self):
        print("Longueur:", self.longueur)
        print("Largeur:", self.largeur)
        print("Périmètre:", self.perimetre())
        print("Aire:", self.aire())
        if self.est_carre():
            print("Il s'agit d'un carré")
        else:
            print("Il ne s'agit pas d'un carré")
