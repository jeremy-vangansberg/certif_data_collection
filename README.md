# Projet de Traitement de Fichiers Parquet et CSV

## Description
Ce projet contient des scripts pour :
- Télécharger des fichiers Parquet depuis Azure Blob Storage.
- Les convertir en fichiers CSV.
- Les analyser et explorer avec des notebooks Jupyter.

## Structure du Projet

```
- .env                      : Fichier de configuration des variables d'environnement.
- .gitignore                : Fichier pour ignorer certains fichiers et dossiers dans le contrôle de version.
- az_login_with_env.sh      : Script pour se connecter à Azure en utilisant les variables d'environnement.
- bdd.py                    : Script Python pour la gestion de la base de données.
- draft.txt                 : Fichier texte pour les brouillons.
- explorer-zip.ipynb        : Notebook Jupyter pour explorer les fichiers ZIP.
- file_to_upload.csv        : Exemple de fichier CSV à uploader.
- generate_sas.sh           : Script pour générer un SAS token pour Azure Blob Storage.
- main.ipynb                : Notebook Jupyter principal pour l'analyse des données.
- output_data.csv           : Fichier CSV de sortie.
- output_images/            : Dossier contenant les images de sortie.
- parquet_to_csv.py         : Script pour convertir des fichiers Parquet en CSV.
- process_blob.py           : Script pour télécharger des fichiers Parquet depuis Azure Blob Storage.
- requirements.txt          : Fichier listant les dépendances Python du projet.
- Sales_SalesOrderHeader_20200723.parquet : Exemple de fichier Parquet.
- sample3.parquet           : Exemple de fichier Parquet.
- test-00000-of-00003.parquet : Exemple de fichier Parquet.
- test.json                 : Exemple de fichier JSON.
```

## Installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/jeremy-vangansberg/simplon-data-collection-Azure-Parquet.git
   ```

2. **Créer un environnement virtuel et installer les dépendances :**
   ```bash
   python -m venv env
   source env/bin/activate  # Sur Windows : env\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configurer les variables d'environnement dans le fichier `.env` :**
   - Ajouter les variables nécessaires à la connexion Azure et à la gestion des fichiers :
     - `SUBSCRIPTION_ID` : Identifiant unique de votre abonnement Azure.
     - `LOCAL_PARQUET_FILE` : Nom ou chemin du fichier Parquet local.
     - `SP_ID_SECONDARY` : Identifiant du *Service Principal* secondaire.
     - `SP_SECONDARY_PASSWORD` : Mot de passe du *Service Principal* secondaire.
     - `SP_ID_PRINCIPAL` : Identifiant du *Service Principal* principal.
     - `TENANT_ID` : Identifiant unique du locataire Azure AD.
     - `KEYVAULT_URL` : URL du Key Vault Azure.
     - `SECRET_NAME` : Nom du secret dans le Key Vault.
     - `STORAGE_ACCOUNT_NAME` : Nom du compte de stockage Azure Blob Storage.

## Utilisation

### Télécharger un fichier Parquet depuis Azure Blob Storage

Utiliser le script `process_blob.py` pour télécharger un fichier Parquet :

```bash
python process_blob.py --blob_url <URL_DU_BLOB> --local_file <NOM_DU_FICHIER_LOCAL>
```

### Convertir un fichier Parquet en CSV

Utiliser le script `parquet_to_csv.py` pour convertir un fichier Parquet en CSV :

```bash
python parquet_to_csv.py --parquet_file <NOM_DU_FICHIER_PARQUET> --csv_file <NOM_DU_FICHIER_CSV>
```

### Explorer les données avec Jupyter Notebook

1. Ouvrir Jupyter Notebook :
   ```bash
   jupyter notebook
   ```

2. Exécuter les notebooks suivants :
   - `main.ipynb`
   - `explorer-zip.ipynb`

Ces notebooks permettent d'explorer et d'analyser les données.

## Scripts

### `process_blob.py`
- **Fonction principale :** `fetch_parquet(blob_url, local_file)`
  - Télécharge un fichier Parquet depuis Azure Blob Storage et le sauvegarde localement.

### `parquet_to_csv.py`
- **Fonction principale :** `convert_parquet_to_csv(parquet_file, csv_file)`
  - Convertit un fichier Parquet local en fichier CSV.

### `az_login_with_env.sh`
- Script pour se connecter à Azure en utilisant les variables d'environnement définies dans le fichier `.env`.

### `generate_sas.sh`
- Script pour générer un SAS token pour un blob spécifique dans Azure Blob Storage.

## Contribuer

Les contributions sont les bienvenues !
- Veuillez soumettre une pull request ou ouvrir une issue pour discuter des changements que vous souhaitez apporter.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
