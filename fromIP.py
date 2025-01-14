import requests
import Displaye

def Ip(ip):
    result=""
    try:
        # Si l'IP est 127.0.0.1, récupérer l'IP publique
        if ip == "127.0.0.1" :
            ip_response = requests.get("https://api64.ipify.org?format=json")
            ip_response.raise_for_status()  # Vérifie les erreurs HTTP
            ip = ip_response.json().get("ip")  # Récupère l'IP publique            
        # Rechercher les informations de l'IP
        response = requests.get(f'http://ip-api.com/json/{ip}')
        response.raise_for_status()  # Lève une exception pour les erreurs HTTP
        
        location_info = response.json()
        
        # Gérer les erreurs de l'API
        if location_info.get("status") == "fail":
            return {"error": location_info.get("message", "Erreur inconnue")}
        
        status = "Status: "+location_info["status"]
        country = "Country: " + location_info["country"]
        countryCode = "CountryCode: " + location_info["countryCode"]
        region = "Region: " + location_info["region"]
        regionName = "RegionName: " + location_info["regionName"]
        city = "City: " + location_info["city"]
        isp = "Isp: "+ location_info["isp"]
        As = "As: " + location_info["as"]
        result = status+"\n"+country+"\n"+countryCode+"\n"+region+"\n"+regionName+"\n"+city+"\n"+isp+"\n"+As
        print(result)
        Displaye.Display(result)
    
    except requests.RequestException as e:
        print({"error": f"Erreur de connexion : {str(e)}"})
        Displaye.Display(result)
