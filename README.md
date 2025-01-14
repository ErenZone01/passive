# 🔍 passive.py - Recherche d'informations en ligne

**passive.py** est un outil de recherche passif permettant de récupérer des informations sur des personnes ou des adresses IP en interrogeant différentes sources en ligne. Il permet de vérifier l'existence de comptes sur les réseaux sociaux, de rechercher des informations personnelles telles que des numéros de téléphone ou des adresses, ainsi que des informations sur la provenance d'une adresse IP.

---

## 🧩 Fonctionnalités

1. **Recherche de nom d'utilisateur sur les réseaux sociaux**  
   Vérifie si un nom d'utilisateur existe sur **au moins 5 réseaux sociaux**, notamment :
   - Instagram
   - Twitter (X)
   - Tumblr
   - Reddit
   - Youtube

2. **Recherche de nom complet (`fullname`)**  
   Permet de récupérer des informations telles que :
   - Numéro de téléphone
   - Adresse postale
   - Informations associées au nom complet

3. **Recherche d'adresse IP (`ip`)**  
   Permet d'obtenir des informations sur une adresse IP :
   - Fournisseur d'accès à Internet (ISP)
   - Région géographique d'origine
   - Informations de localisation

---

## 🖥️ Commandes disponibles

### 🔎 Recherche par nom d'utilisateur (`-u`)
Cette commande permet de vérifier si un nom d'utilisateur est enregistré sur plusieurs réseaux sociaux :

```bash
python3 passive.py -u "@username"

# Crée un environnement virtuel nommé "env"
bash ´python3 -m venv env´

# Active l'environnement virtuel
bash ´source env/bin/activate´

# Installer les dependances ou utiliser le fichier requirement.txt
   #Installation manuelle
   bash ´pip install socialscan´
   bash ´pip install requests´
   #Installation avec Requirement.txt
   bash ´pip install -r requirements.txt´
   #mettre a jour les dependances
   bash ´pip freeze > requirements.txt´


# Execution -u (Username)
bash ´python3 passive.py -u "@username"´

# Execution -fn (Full Name)
bash ´python3 passive.py -fn "fullname"´

# Execution -ip (Ip Address)
bash ´python3 passive.py -ip "ip address"´

# Desactiver l'envirionnement virutel
bash ´deactivate´