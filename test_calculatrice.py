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
    
#Test unitaire de la division
def test_division():
    cal1 = Calculatrice(2,2)
    cal2 = Calculatrice(6,2)
    
    assert cal1.division() == 1
    assert cal2.division() == 3