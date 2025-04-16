def rendre_livre():
    id = input("Entrez l'id du livre à rendre: ")
    livre = trouver_livre(id)
    if livre:
        nombre = int(input(f"Entrez le nombre de livre à rendre : "))
        livre["nombre"] += nombre
        print(f"Livre rendu ! Le livre {livre['Titre']} a maintenant {livre['nombre']} exemplairs dans notre stock !")
    else:
        print("Livre introuvable !")