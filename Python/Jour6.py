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
 "quantite":20,                    "prix": 50
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
