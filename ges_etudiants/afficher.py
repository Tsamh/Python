def afficher_etu(nom ,matricule ,etudiant, list_etu):
    if etudiant in list_etu:
        for key , value in etudiant.items():
            if etudiant["nom"] == nom:
                return etudiant
            if etudiant['matricule'] == matricule:
                return etudiant
    else:
        return "L'étudiant n'est pas sur la liste!!"