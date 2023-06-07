# FASTAPI-EXAMPLE

## 1. Installation de Python

Le projet requiert l'environement d'exécution **Python** pour s'exécuter voici comment l'installer sur Windows ou des distro linux utilisant le package manager **apt**:

### 1.a Windows
Pour installer **Python** sur windows veuillez allez sur ce [lien](https://www.python.org/downloads/), puis telecharger l'exécutable d'intallation et suivre les indications d'installations.

### 1.b Linux
Pour installer **Python** sur linux veuillez lancer les lignes de commandes suivantes:
```bash
sudo apt-get update
sudo apt-get install python3.6 #ou python3.10
```
## 2. Installation des librairies

Le project nécéssite plusieur librairies pour pouvoir 
s'exécuter correctement. Pour les installer lancer les lignes de commandes suivantes: 
```bash
pip install fastapi
pip install "uvicorn[standard]"
pip install requests
```

Si jamais vous revevez l'erreur:
```bash
error: externally-managed-environment
```

Veuillez lancer ces lignes de commandes à la racine du project:
```bash
sudo apt install python3-full
python3 -m venv .venv
source .venv/bin/activate
```
Vous pouvez maintenant réexécuter les commandes ci-desssus

## 1. Exécution

Pour lancer le serveur placer vous à la racine du projet et lancer la commande suivantes:
```bash
uvicorn main:app --reload
```