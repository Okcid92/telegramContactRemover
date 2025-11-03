# Telegram Contact Remover

Un petit script Python pour supprimer tous vos contacts Telegram de manière sécurisée et automatisée grâce à l'API Telegram et la librairie Telethon.

## 🚀 Fonctionnalités

- Récupère tous les contacts Telegram de votre compte
- Supprime tous les contacts en un seul passage
- Gestion sécurisée des informations sensibles via un fichier `config.yaml`
- Facile à configurer et à exécuter

## ⚙️ Prérequis

- Python ≥ 3.10
- Compte Telegram actif
- API ID et API Hash (récupérables sur [Telegram API](https://my.telegram.org))
- pip installé

## 📝 Installation

1. **Clonez le projet :**

```bash
git clone https://github.com/votre-utilisateur/telegram-contact-remover.git
cd telegram-contact-remover
```

2. **Créez un environnement virtuel (optionnel mais recommandé) :**

```bash
# Linux/macOS
python -m venv .env
source .env/bin/activate

# Windows
python -m venv .env
.env\Scripts\activate
```

3. **Installez les dépendances :**

```bash
pip install -r requirements.txt
```

## 🔐 Configuration

Créez un fichier `config.yaml` à la racine du projet avec le contenu suivant :

```yaml
api_id: VOTRE_API_ID
api_hash: 'VOTRE_API_HASH'
phone_number: '+VOTRE_NUMERO'
```

> **⚠️ Important :** Ce fichier contient des informations sensibles. Ajoutez `config.yaml` dans votre `.gitignore` pour ne pas le pousser sur GitHub :

```gitignore
config.yaml
```

## 💻 Utilisation

Exécutez le script avec Python :

```bash
python main.py
```

Le script va :
1. Se connecter à votre compte Telegram
2. Récupérer tous vos contacts
3. Les supprimer automatiquement

Vous verrez des messages dans le terminal confirmant le nombre de contacts trouvés et supprimés.

## 📦 Générer requirements.txt

Pour générer la liste des dépendances de votre environnement actuel :

```bash
pip freeze > requirements.txt
```

## ⚠️ Avertissement

- Utilisez ce script à vos propres risques
- Telegram peut détecter des actions massives et limiter certaines fonctionnalités
- **Ne partagez jamais votre `config.yaml` publiquement**
- Assurez-vous de vouloir vraiment supprimer tous vos contacts avant d'exécuter le script

## 📄 Licence

[Choisissez votre licence - MIT, GPL, etc.]

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

---

**Note :** Ce projet est fourni à des fins éducatives. Respectez les conditions d'utilisation de Telegram.