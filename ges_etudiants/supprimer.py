def supprimer_etu(matricule, list_etu):
    for etudiant in list_etu:
        if etudiant['matricule'] == matricule:
            list_etu.remove(etudiant)
            return list_etu
        else:
            return "L'étudiant n'est pas sur la liste!!"