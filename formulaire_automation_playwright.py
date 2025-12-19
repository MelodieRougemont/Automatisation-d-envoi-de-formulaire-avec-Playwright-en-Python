# Plus d'informatins lire le README.md

# Etapes des modifications à faire :
# Etapes 1 : Aller sur le site dont on veut automatiser le formulaire 
# Etape 2 : Inspecter la page > Réseau > XHR et envoyer un formulaire test
# Etape 3 : Inspecter la requête POST reçue et récupérer l'URL POST XHR du formulaire
# Etape 4 : Récupérer le header de la requête 
# Etape 5 : Ajouter et ajuster les cookies si besoin 
# Etape 6 : Récupérer les données de formulaire
# Etape 7 : Récupérer le message de la réponse json dans l'onglet Réponse 

# Les modules 
from playwright.sync_api import sync_playwright # Automatise un navigateur
import json # Pour lire les json

# Etape 3 (A modifier selon votre résultat)
URL_POST = "https://www.exemple.com/ajax/contact-envoi-debug.php" 

# Etape 6
# Exemple de données type (A modifier selon vos résultats)
payload = {
    "contact[nom]": "NomTest",
    "contact[prenom]": "PrenomTest",
    "contact[email]": "email@test.com",
    "contact[telephone]": "0123456789",
    "contact[sujet]": "SujetTest",
    "contact[texte]": "TexteTest",
    "sigleLangue": "fr",
    "idLangue": "1"
}

# Etape 5 (A modifier selon vos résultats)
# cookies = {
#     "name1": "value1",
#     "name2": "value2",
# }
# cookie_header = "; ".join([f"{k}={v}" for k, v in cookies.items()]) # Ou directement ce format

# Etape 4 (A modifier selon vos résultats)
headers = {
    "Content-Type": "text/html; charset=utf-8",
    "X-Requested-With": "XMLHttpRequest", 
    "User-Agent": "Mozilla/5.0 (platform; rv:gecko-version) Gecko/gecko-trail Firefox/firefox-version",
    "Origin": "https://www.exemple.com",
    "Referer": "https://www.exemple.com/page-exemple.htm", # Où se trouve le formulaire
    #"Cookie": cookie_header  # Si besoin
}

def run():
    with sync_playwright() as p: # Lancement du module
        browser = p.chromium.launch(headless=False)
        context = browser.new_context() # Création d'une navigation
        page = context.new_page() # Nouvel onglet

        # Envoi de la requête avec le payload et le header
        response = page.request.post(URL_POST, data=payload, headers=headers)

        # Vérifications
        if response.status == 200:
            try:
                data = json.loads(response.text()) # Pour analyser la réponse json
                if data.get("statut") is True and "VotreMessage" in data.get("message", ""): # Etape 7 (modifier "VotreMessage")
                    print("Formulaire envoyé avec succès, statut 200")
                else:
                    print("Réponse reçue mais message inattendu:", data)
            except json.JSONDecodeError:
                print("Réponse 200 mais non JSON:", response.text()[:200])
        else:
            print("Échec de l'envoi, status:", response.status)

        browser.close() # Fermeture du navigateur

# Lancement du script
if __name__ == "__main__":
    run()
