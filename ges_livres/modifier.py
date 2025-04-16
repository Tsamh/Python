def modifier_livre(titre,choix,new,liste_livres,livre):
    for livre in liste_livres:
        for key in livre.items():
            if livre["titre"] == titre:
                if (choix == "titre"):
                    livre["titre"] = new
                    return livre
                elif (choix == "auteur"):
                    livre["auteur"] = new
                    return livre
                elif (choix == "annee"):
                    livre["annee"] = new
                    return livre
                elif (choix == "id"):
                    livre["id"] = new
                    return livre
                else:
                    livre["nombre"] = new
                    return livre