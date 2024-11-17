#!/bin/bash

# Charger les variables depuis le fichier .env
if [ -f ".env" ]; then
    export $(grep -v '^#' .env | xargs)
else
    echo "Erreur : Fichier .env introuvable."
    exit 1
fi

if [ -z "$SUBSCRIPTION_ID" ]; then
    echo "Erreur : La variable SUBSCRIPTION_ID n'est pas définie dans le fichier .env."
    exit 1
fi

# Vérifier si l'utilisateur est déjà connecté
echo "Vérification de l'état de connexion à Azure..."
if az account show &>/dev/null; then
    echo "Vous êtes déjà connecté à Azure."
else
    echo "Connexion à Azure..."
    if az login; then
        echo "Connexion réussie."
    else
        echo "Erreur : La connexion à Azure a échoué."
        exit 1
    fi
fi

# Configurer l'abonnement actif
CURRENT_SUBSCRIPTION=$(az account show --query "id" -o tsv)

if [ "$CURRENT_SUBSCRIPTION" = "$SUBSCRIPTION_ID" ]; then
    echo "L'abonnement $SUBSCRIPTION_ID est déjà actif."
else
    echo "Basculer vers l'abonnement $SUBSCRIPTION_ID..."
    if az account set --subscription "$SUBSCRIPTION_ID"; then
        echo "Abonnement actif défini sur $SUBSCRIPTION_ID."
    else
        echo "Erreur : Impossible de définir l'abonnement actif."
        exit 1
    fi
fi

# Afficher l'abonnement actif
echo "Abonnement actuellement actif :"
az account show --query "{Abonnement:subscriptionName, ID:id}" -o table
