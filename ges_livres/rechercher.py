def rechercher_livre(titre,id,liste_livres,livre):
    for livre in liste_livres:
        for key,values in livre.items():
            if livre["id"] == id:
                return  livre
            else:
                return "Ce livre ne fait pas partie de la bibliothèque."