def ajouter_etu(etudiant, list_etu):
    list_etu.append(etudiant)
    return list_etu

def rechercher_etu(matricule, etudiant, list_etu):
    if etudiant in list_etu:
        if etudiant['matricule'] == matricule:
           return etudiant["Prénom"]
        else :
            return "L'etudiant n'est pas dans la liste"
    else :
       return "L'étudiant n'est pas dans la liste"

        
def supprimer_etu(matricule, list_etu):
    for etudiant in list_etu:
        if etudiant['matricule'] == matricule:
            list_etu.remove(etudiant)
            return list_etu
        else:
            return "L'étudiant n'est pas sur la liste!!"
        
def afficher_etu(nom ,matricule ,etudiant, list_etu):
    if etudiant in list_etu:
        for key , value in etudiant.items():
            if etudiant["nom"] == nom:
                return etudiant
            if etudiant['matricule'] == matricule:
                return etudiant
    else:
        return "L'étudiant n'est pas sur la liste!!"
    
def lister(list_etu):
    print(list_etu)

def modifier_etu(etudiant, list_etu):
    rechercher_etu(etudiant, list_etu)
    etudiant.update (etudiant)