def rechercher_etu(matricule, etudiant, list_etu):
    if etudiant in list_etu:
        if etudiant['matricule'] == matricule:
           return etudiant["Prenom"]
        else :
            return "L'etudiant n'est pas dans la liste"
    else :
       return "L'étudiant n'est pas dans la liste"
