#Création d'une calculatrice
class Calculatrice():
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def somme(self):
        return   self.a + self.b
    
    def produit(self):
        return (self.a)*(self.b)
        
    def division(self):
        if self.b ==0:
            raise ValueError("Le dénominateur est zéro")
        else:
            return self.a/self.b