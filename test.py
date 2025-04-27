from ges_etudiants.ajouter import ajouter_etu
from ges_etudiants.modifier import modifier_etu
from ges_livres.ajouter import ajouter_livre
from ges_livres.rechercher import rechercher_livre

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
    # Ajout livres
    print(ajouter_livre(liste_livres,livre))

# Recherche livre
titre = input("Entrer le livre à rechercher: ")
id = int(input("Entrer l'id du livre à rechercher: "))
print(rechercher_livre(titre,id,liste_livres,livre))