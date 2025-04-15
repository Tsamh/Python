from ges_livres import ajouter_livre
from ges_livres import rechercher_livre
from random import randint

liste_livres = []

n = int(input("Enter le nombre de livres: "))


for i in range(n):
    livre = {}
    livre["titre"] = input("Entrer le titre du livre: ")
    livre["auteur"] = input("Entrer l'auteur du livre: ")
    livre["année"] = int(input("Entrer l'année du livre: "))
    livre["nombre"] = int(input("Entrer le nbre d'exemplaire du livre: "))
    livre["id"] = randint(1,50)
    print(ajouter_livre(liste_livres,livre))

titre = input("entrer le livre à rechercher: ")
id = int(input("Entrer l'id du livre à rechercher: "))
print(rechercher_livre(titre,id,liste_livres,livre))