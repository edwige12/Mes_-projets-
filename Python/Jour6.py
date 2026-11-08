# Inventaire électronique
inventaire = [{ "nom": "arduino uno",  "categorie": "carte électronique", "quantite": 2,
"prix": 5000},   {
 "nom": "led",
 "categorie": "Composant électronique",
 "quantite": 10,
 "prix":100                     
 },                              
  {
 "nom": "résistance",
 "categorie": "Composant électronique",
 "quantite":20,    
 "prix": 50
   },
   {
 "nom": "capteur ultrason",
 "categorie": "Capteur",
 "quantite": 3,
 "prix": 2500
   },
    {
 "nom": "buzzer",
 "categorie": "Actionneur",
 "quantite": 4,
 "prix":500   },
    {
 "nom": "servo moteur",
 "categorie": "Actionneur",
 "quantite": 2,               
 "prix": 3000
    }]
def rechercher_composant():
  recherche = input("Entrez le nom du composant: ")
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
