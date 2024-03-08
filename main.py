import requests
import json

# Configuration du client
server_url = 'http://127.0.0.1:33800'  # Remplacez par l'adresse du serveur

print("Entrer le nombre de joueurs")
nb_joueurs = int(input())
# Liste pour stocker les informations des joueurs
players = []

for i in range(1, nb_joueurs + 1):
    print(f"Entrer le nom du joueur {i}")
    nom_joueur = input()

    # Demander si le joueur est un bot
    est_bot = input(f"Le joueur {nom_joueur} est-il un bot ? (Oui/Non) ").lower() == 'oui'

    # Ajouter les informations du joueur à la liste
    joueur = {"name": nom_joueur, "bot": est_bot}
    players.append(joueur)

# Construction du JSON
json_data = {"action": "launch", "players": players}

# Envoi de la requête POST au serveur
response = requests.post(server_url, json=json_data)

if response.json()['success']:
    print("Jeu correctement lancé")
    get_game_response = requests.get(f'{server_url}/get_game_json')
    if get_game_response.status_code == 200:
        game_json = get_game_response.json()
        print("JSON du jeu:", game_json)
    else:
        print(f"Erreur {get_game_response.status_code}: {get_game_response.json()}")
else:
    print("Échec du lancement du jeu")