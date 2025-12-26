# Automatisation d'envoi de formulaire avec Playwright en Python
Script Python utilisant Playwright pour automatiser l’envoi de formulaires web via requêtes POST. Permet de tester et déboguer l’envoi de données, gérer les headers et cookies, et analyser les réponses JSON. Compatible Chromium, Firefox et WebKit.  

## Fonctionnalités :
- Envoi de requêtes POST avec données application/x-www-form-urlencoded
- Personnalisation des headers HTTP
- Simulation d’un navigateur réel via Playwright. Cela contourne certaines protections anti-bot basées sur l’environnement d’exécution.
- Analyse de la réponse serveur (statut HTTP, contenu JSON)
- Compatible Chromium, Firefox et WebKit

## Prérequis :
- Python 3.9 ou supérieur (ici 3.14.0)
- pip pour installer les modules (ici 25.3)
- Connexion internet
- Navigateurs Playwright : Chromium (Google chrome et Microsoft Edge), Firefox, WebKit (Safari)
- Les chemins système et droits d’exécution doivent permettre à Playwright de lancer Chromium

## Installation module :
pip install playwright
playwright install

## Configuration :
Modifier l’URL cible, le payload, les headers, le message json et si besoin les cookies selon l’environnement.

URL :
URL_POST = "https://www.exemple.com/ajax/contact-envoi-debug.php"

Payload :
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

Headers :
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0",
    "Origin": "https://www.exemple.com",
    "Referer": "https://www.exemple.com/page-exemple.htm"
}

Les cookies ne sont pas inclus par défaut. Certains formulaires peuvent en nécessiter selon la configuration serveur.

Exécution.

## Comportement :
- Envoi de la requête POST
- Vérification du statut HTTP (200 attendu)
- Tentative de lecture de la réponse JSON
- Affichage du résultat dans la console

## Notes et limitations :
- Navigateur lancé en mode non headless par défaut (visibilité, débogage, comportement plus proche d’un usage humain)
  l.51(p.chromium.launch(headless=False))
  Mettre True pour passer en headless (automatisation silencieuse, exécution serveur, tâches planifiées)
- Certains formulaires nécessitent des tokens dynamiques ou une session active (cookie)
- Les paramètres doivent être adaptés au site ciblé
- Usage réservé aux tests, au débogage et à l’automatisation contrôlée

## Licence :
Projet fourni à des fins éducatives et techniques. Le respect des conditions d’utilisation des sites ciblés relève de la responsabilité de l’utilisateur.
