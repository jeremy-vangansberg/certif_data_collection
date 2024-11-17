import os
from azure.storage.blob import BlobClient


def load_env_variables(env_file):
    """
    Charger les variables d'environnement depuis un fichier .env.
    """
    if not os.path.exists(env_file):
        raise FileNotFoundError(f"Erreur : Le fichier {env_file} est introuvable.")

    with open(env_file, "r") as file:
        for line in file:
            # Ignorer les commentaires et les lignes vides
            if line.strip() and not line.startswith("#"):
                key, value = line.strip().split("=", 1)
                os.environ[key] = value.strip('"')  # Supprimer les guillemets éventuels


def fetch_parquet(blob_url, local_file):
    """
    Télécharger le fichier Parquet depuis Azure Blob Storage et le sauvegarder localement.
    """
    print(f"Téléchargement du fichier Parquet depuis : {blob_url}")
    try:
        # Créer une instance de BlobClient
        blob_client = BlobClient.from_blob_url(blob_url)

        # Télécharger le fichier et l'enregistrer localement
        with open(local_file, "wb") as file:
            download_stream = blob_client.download_blob()
            file.write(download_stream.readall())

        print(f"Fichier téléchargé avec succès : {local_file}")
    except Exception as e:
        print(f"Erreur lors du téléchargement du fichier blob : {e}")
        raise


def main():
    # Charger les variables d'environnement
    env_file = ".env"
    try:
        load_env_variables(env_file)
    except FileNotFoundError as e:
        print(e)
        return

    # Récupérer les variables nécessaires
    blob_url = os.getenv("BLOB_URL")
    local_file = os.getenv("LOCAL_PARQUET_FILE", "local_data.parquet")

    if not blob_url:
        print("Erreur : La variable BLOB_URL n'est pas définie dans le fichier .env.")
        return

    # Télécharger le fichier Parquet
    try:
        fetch_parquet(blob_url, local_file)
    except Exception as e:
        print(f"Une erreur est survenue : {e}")


if __name__ == "__main__":
    main()
