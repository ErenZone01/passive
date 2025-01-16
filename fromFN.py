import requests
import sys
import Displaye
sys.dont_write_bytecode = True

def search_pages_blanches(name):
    tab = name.split()
    firstname = " ".join(tab[:-1])  # Tous les éléments sauf le dernier
    lastname = tab[-1]             # Dernier élément

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
            print(f"Firstname : {firstname}")
            print(f"Lastname : {lastname}")
            print(f"Number : {phone}")
            print(f"Adress : {address}")
            result = f"Firstname : {firstname}\n"+ f"Lastname : {lastname}\n" + f"Number : {phone}\n" + f"Adress : {address}"
    except requests.RequestException as e:
        print(f"Erreur lors de la requête HTTP : {e}")
    Displaye.Display(result)

