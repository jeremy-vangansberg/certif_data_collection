#!/bin/bash

# Charger les variables depuis le fichier .env
if [ -f ".env" ]; then
    export $(grep -v '^#' .env | xargs)
else
    echo "Fichier .env introuvable. Création d'un nouveau fichier .env..."
    touch .env
fi

# Variables nécessaires pour le conteneur et le fichier
STORAGE_ACCOUNT="adlsjv"  # Nom de ton compte de stockage
CONTAINER="fsnjv"         # Nom du conteneur
BLOB_NAME="big_data_store/Sales_SalesOrderHeader_20200723.parquet"  # Chemin du fichier dans le conteneur
EXPIRATION="2024-11-17T23:59:59Z"          # Expiration du SAS token

# Générer le SAS token avec Azure CLI
echo "Génération du SAS token pour le blob : $BLOB_NAME"
SAS_TOKEN=$(az storage blob generate-sas \
    --account-name "$STORAGE_ACCOUNT" \
    --container-name "$CONTAINER" \
    --name "$BLOB_NAME" \
    --permissions r \
    --expiry "$EXPIRATION" \
    --https-only \
    --output tsv)

# Vérifier si le SAS token est généré
if [ -z "$SAS_TOKEN" ]; then
    echo "Erreur : Impossible de générer le SAS token. Vérifiez vos paramètres et permissions."
    exit 1
fi

# Générer l'URL complète avec le SAS token
BLOB_URL="https://$STORAGE_ACCOUNT.blob.core.windows.net/$CONTAINER/$BLOB_NAME?$SAS_TOKEN"

# Supprimer l'entrée existante pour BLOB_URL si elle existe
sed -i '/^BLOB_URL=/d' .env

# Ajouter la nouvelle valeur pour BLOB_URL à la fin du fichier
echo "BLOB_URL=\"$BLOB_URL\"" >> .env

echo "SAS token généré avec succès et enregistré dans .env"
