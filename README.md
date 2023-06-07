# FASTAPI-EXAMPLE

## 1. Installation de Python

Le projet requiert l'environnement d'exécution **Python** pour s'exécuter voici comment l'installer sur Windows ou des distro linux utilisant le package manager **apt**:

### 1.a Windows
Pour installer **Python** sur **Windows** veuillez aller sur ce [lien](https://www.python.org/downloads/), puis télécharger l'exécutable d'installation et suivre les indications d'installations.

### 1.b Linux
Pour installer **Python** sur **Linux** veuillez lancer les lignes de commandes suivantes:
```bash
sudo apt-get update
sudo apt-get install python3.6 #ou python3.10
```
## 2. Installation des librairies

Le projet nécessite plusieurs librairies pour pouvoir 
s'exécuter correctement. Pour les installer lancer les lignes de commandes suivantes: 
```bash
pip install fastapi
pip install "uvicorn[standard]"
pip install requests
```

Si jamais vous recevez l'erreur:
```bash
error: externally-managed-environment
```

Veuillez lancer ces lignes de commandes à la racine du projet:
```bash
sudo apt install python3-full
python3 -m venv .venv
source .venv/bin/activate
```
Vous pouvez maintenant réexécuter les commandes ci-dessus

## 3. Exécution

Pour lancer le serveur placez-vous à la racine du projet et lancez la commande suivante:
```bash
uvicorn main:app --reload
```