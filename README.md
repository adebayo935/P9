# P9

## Initialisation et Infos

Pour pouvoir utiliser le projet, il vous faudra au préalable récupérer l'intégralité du dossier merchex.

Dans un premier temps, vous devez créer le répertoire de l'application puis cloner y le dossier et enfin créer votre environnement python. Ensuite il faudra installer les modules présents dans le fichier requirements.txt. 

### Creer un environnement virtuel

```bash
py -m venv env
```

### Activer l'environnement virtuel

```bash
env\Scripts\activate.bat
```

### Installer les dépendances

Tapez cette commande:

```bash
pip install -r requirements.txt
```

### Lancer le serveur

Ouvrez votre terminal et tapez:

```bash
python manage.py runserver
```

### Navigation sur le site

Une fois le serveur lancé rendez-vous à l'adresse http://127.0.0.1:8000/home/ pour accéder au site.

#### Login

Pour créer un utilisateur utilisez le lien correspondant sinon utilisez le lien de connection.
Le mot de passe ne doit pas être commun et contenir au moins 8 caractères.

#### Flux

Une fois connecté vous accèderez au flux principal du site, naviguez entre les différentes sections via la barre de menu en haut à droite.

Cliquez sur "Demander un critique" pour créer un nouveau ticket ou bien "Publier une critique" pour créer une nouvelle critique. Sinon, répondez directement à un ticket en cliquant sur "Répondre"
sur le ticket correspondant.
L'image n'est pas obligatoire dans le formulaire.

#### Posts

Cette section vous permet de consulter,modifier et supprimer tous les tickets et critiques que vous avez publiés.

#### Abonnements

Cette section vous permet de consulter,suivre, se désabonner des autres utilisateurs. Selectionnez l'utilisateur à ajouter via le menu déroulant.

#### Déconnection

Utilisez le lien en haut à gauche
