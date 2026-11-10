# Inventaire électronique
inventaire = [
    {"nom": "Arduino Uno", "categorie": "Carte électronique", "quantite": 2, "prix": 5000},
    {"nom": "LED", "categorie": "Composant électronique", "quantite": 10, "prix": 100},
    {"nom": "Résistance", "categorie": "Composant électronique", "quantite": 20, "prix": 50},
    {"nom": "Capteur ultrason", "categorie": "Capteur", "quantite": 3, "prix": 2500},
    {"nom": "Buzzer", "categorie": "Composant électronique", "quantite": 4, "prix": 500},
    {"nom": "Servo moteur", "categorie": "Actionneur", "quantite": 2, "prix": 3000}
]

def rechercher_composant():
    recherche = input("Entrez le nom du composant : ")
    trouve = False
    for composant in inventaire:
        if composant["nom"].lower() == recherche.lower():
            trouve = True
            print("Composant trouvé")
            print("Nom :", composant["nom"])
            print("Categorie:", composant["categorie"])
            print("Quantité :", composant["quantite"])
            print("Prix :", composant["prix"], "FCFA")
    if trouve == False:
        print("Composant introuvable")

# Ajouter un composant
def ajouter_composant():
    nom = input("Entrez le nom du composant : ")
    categorie = input("Entrez la catégorie : ")
    quantite = int(input("Entrez la quantité : "))
    prix = int(input("Entrez le prix unitaire : "))
    nouveau_composant = {
        "nom": nom,
        "categorie": categorie,
        "quantite": quantite,
        "prix": prix
    }
    inventaire.append(nouveau_composant)
    print("Composant ajouté avec succès !")

# Afficher l'inventaire
def afficher_inventaire():
    print("===== INVENTAIRE ELECTRONIQUE =====")
    for composant in inventaire:
        print("Nom :", composant["nom"])
        print("Catégorie :", composant["categorie"])
        print("Quantité :", composant["quantite"])
        print("Prix :", composant["prix"], "FCFA")
        print("----------------------")

# Calculer la valeur totale du stock
def calculer_valeur_stock():
    total = 0
    for composant in inventaire:
        total += composant["quantite"] * composant["prix"]
    print("Valeur totale du stock :", total, "FCFA")

import os

def menu():
    while True:
        os.system("clear")
        print("\n===== GESTION D'INVENTAIRE =====")
        print("1. Afficher l'inventaire")
        print("2. Rechercher un composant")
        print("3. Ajouter un composant")
        print("4. Calculer la valeur du stock")
        print("5. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            afficher_inventaire()
            input("\nAppuyez sur Entrée pour revenir au menu...")
        elif choix == "2":
            rechercher_composant()
            input("\nAppuyez sur Entrée pour revenir au menu...")
        elif choix == "3":
            ajouter_composant()
            input("\nAppuyez sur Entrée pour revenir au menu...")
        elif choix == "4":
            calculer_valeur_stock()
            input("\nAppuyez sur Entrée pour revenir au menu...")
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide !")
            input("\nAppuyez sur Entrée pour continuer...")

menu()