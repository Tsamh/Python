
from bibliotheque.ges_etudiants.rechercher import rechercher_etu
from bibliotheque.ges_livres.rechercher import rechercher_livre

def emprunter_livre(matricule, id):
    etudiant = rechercher_etu(matricule)
    livre = rechercher_livre(id)
    if etudiant:
        if livre:
            nombre = int(input(f"Entrez le nombre de livre à emprunter : "))
            livre["nombre"] -= nombre
            print(f"{etudiant} a emprunté le livre {livre['Titre']}. Ce livre a maintenant {livre['nombre']} exemplaires dans notre stock !")
        else:
            print("Livre introuvable !")