#Mise en place du test unitaire de la classe Calculatrice

from calculatrice import Calculatrice
import pytest

#Test unitaire pour la fonction somme
def test_somme():
    cal1 = Calculatrice(2, 4)
    cal2 = Calculatrice(10, 20)
    
    assert cal1.somme() == 6
    assert cal2.somme() == 30
    
#Test unitaire pour le produit
def test_produit():
    cal1 = Calculatrice(2, 3)
    cal2 = Calculatrice(10, 20)
    
    assert cal1.produit() == 6
    assert cal2.produit() == 200