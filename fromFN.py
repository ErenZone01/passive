import requests
import sys
import Displaye
sys.dont_write_bytecode = True

def search_pages_blanches(name):
    url = f"https://randomuser.me/api/?seed={name}"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    result=""
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse le JSON
        data = response.json()["results"]

        # Parcourir les résultats
        for person in data:
            phone = person["phone"]
            address = f'{person["location"]["street"]["number"]} {person["location"]["street"]["name"]}, {person["location"]["city"]}, {person["location"]["state"]}, {person["location"]["country"]}'
            
            # Afficher les informations
            print(f"Nom complet : {name}")
            print(f"Téléphone : {phone}")
            print(f"Adresse : {address}")
            result = f"Nom complet : {name}\n" + f"Téléphone : {phone}\n" + f"Adresse : {address}"
    except requests.RequestException as e:
        print(f"Erreur lors de la requête HTTP : {e}")
    Displaye.Display(result)

