# class Etudiant:
#     def __init__(self, nom:str, not1:float, not2:float):
#         self.nom = nom
#         self.not1 = not1
#         self.not2 = not2
#     def calc_moy(self):
#         moy = (self.not1 + self.not2) / 2
#         return moy
#     def afficher(self):
#         print("L'etudant s'apelle : ",self.nom," et  a sa note moyenne est : ",self.calc_moy())
# if __name__ == "__main__":
#     nom = input("nom ")
#     note1 = float(input("note 1 "))
#     note2 = float(input("note 2 "))
#     etudiant = Etudiant(nom, note1, note2)
#     etudiant.calc_moy()
# #     etudiant.afficher()
# from math import sqrt
# class Point:
#     def __init__(self, x: float, y: float):
#         self.__x = x
#         self.__y = y
#     #les accesseurs
#     def getX(self):
#         return self.__x
#     def getY(self):
#         return self.__y
#     #les modificateurs
#     def setX(self, X: float):
#         self.__x = X
#     def setY(self, Y: float):
#         self.__y = Y  
#     #definition d'une translation    
#     def deplacer(self, dx: float, dy: float):
#         self.SetX(self.getX()+dx)
#         self.setY(self.getY()+dy)
#     #la methode affiche qui ne fait qu'afficher les coordonnées
#     def afficher(self):
#         print(f"les coordonnées de ce point sont : {self.getX()} et {self.getY()}")
#     def saisir(self, x, y):
#         self.__x = x
#         self.__y = y
#     def distance(self,self1):
#         return sqrt((self1.getX()-self.getX())**2+(self1.getY()-self.getY())**2)
#     def milieu(self, self1):
#         x = (self.getX()+self1.getX())/2
#         y = (self.getY()+self1.getY())/2
#         print(f"le milieu de ce segment a pour coordonnées : ({x},{y})")  
# if __name__ == '__main__':
#     p1 = Point(1, 2)
#     p2 = Point(4, 6)
#     p1.afficher()
#     print(f"la diqtance des deux points est : {p1.distance(p2)}")
#     p1.milieu(p2)
class Account:
    def __init__(self):
        self.solde = 0
    def __int__(self, balance:float):
        self.balance = balance
    def getBalence(self):
        return self.solde
    def deposer(self, depot:float):
        self.solde+=depot
    def retirer(self, retrait:float):
        self.solde-=retrait
    def ajouter_interet(self, taux_interet:float):
        self.solde =self.solde*(1 + taux_interet)
            