
    
# liste_livres = [
#     {"Titre": "Le Hobbit", "Auteur": "Tolkien", "id": "11000", "nombre": 4},
#     {"Titre": "One Piece", "Auteur": "Eiichiro Oda", "id": "22000", "nombre": 5},
#     {"Titre": "Naruto", "Auteur": "Masashi Kishimoto", "id": "33000", "nombre": 10},
#     {"Titre": "Bleach", "Auteur": "Tite Kubo", "id": "44000", "nombre": 2}
# ]


# def trouver_livre(id):
#     for livre in liste_livres:
#         if livre["id"] == id:
#             return livre
#     return "Livre introuvable"

# trouver_livre("11000")

def prendre_livre():
    id = input("Entrez l'id du livre à emprunter : ")
    livre = trouver_livre(id)
    if livre:
        nombre = int(input(f"Entrez le nombre de livre à emprunter : "))
        livre["nombre"] -= nombre
        print(f"Livre emprunté ! Le livre {livre['Titre']} a maintenant {livre['nombre']} exemplaires dans notre stock !")
    else:
        print("Livre introuvable !")

def rendre_livre():
    id = input("Entrez l'id du livre à rendre: ")
    livre = trouver_livre(id)
    if livre:
        nombre = int(input(f"Entrez le nombre de livre à rendre : "))
        livre["nombre"] += nombre
        print(f"Livre rendu ! Le livre {livre['Titre']} a maintenant {livre['nombre']} exemplairs dans notre stock !")
    else:
        print("Livre introuvable !")









def transferer_credit():
    tel_envoyeur = input("Entrez le numéro de téléphone de l'envoyeur : ")
    envoyeur = trouver_client(tel_envoyeur)
    if not envoyeur:
        print("Envoyeur introuvable.")
        return

    tel_receveur = input("Entrez le numéro de téléphone du receveur : ")
    receveur = trouver_client(tel_receveur)
    if not receveur:
        print("Receveur introuvable.")
        return

    montant = float(input(f"Entrez le montant à transférer de {envoyeur['prenom']} à {receveur['prenom']} : "))
    if montant <= 0:
        print("Le montant doit être supérieur à 0.")
    elif montant > envoyeur["solde"]:
        print(f"Solde insuffisant. Le solde de {envoyeur['prenom']} est de {envoyeur['solde']} cfa.")
    else:
        envoyeur["solde"] -= montant
        receveur["solde"] += montant
        print(f"Transfert réussi ! Nouveau solde de {envoyeur['prenom']} : {envoyeur['solde']} cfa.")
        print(f"Nouveau solde de {receveur['prenom']} : {receveur['solde']} cfa.")

def consulter_solde():
    telephone = input("Entrez votre numéro de téléphone : ")
    client = trouver_client(telephone)
    if client:
        print(f"Le solde de {client['prenom']} est de {client['solde']} cfa.")
    else:
        print("Client introuvable.")

