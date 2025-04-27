
from ges_etudiants.rechercher import rechercher_etu
from ges_livres.rechercher import rechercher_livre

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



def emprunter_livre(nom_etudiant, titre_livre):
        if titre_livre in livres and livres[titre_livre] > 0:
            livres[titre_livre] -= 1
            if nom_etudiant not in etudiants:
                etudiants[nom_etudiant] = []
            etudiants[nom_etudiant].append(titre_livre)
            print(f"{nom_etudiant} a emprunté le livre '{titre_livre}'.")
        else:
            print(f"Le livre '{titre_livre}' n'est pas disponible dans le stock.")
            
