import pandas as pd
import os


def convert_parquet_to_csv(parquet_file, csv_file):
    """
    Lire un fichier Parquet local et le convertir en CSV.
    """
    if not os.path.exists(parquet_file):
        raise FileNotFoundError(f"Erreur : Le fichier Parquet {parquet_file} est introuvable.")

    print(f"Conversion du fichier Parquet : {parquet_file} -> CSV : {csv_file}")
    try:
        # Lire le fichier Parquet
        df = pd.read_parquet(parquet_file, engine="pyarrow")  # Assure-toi d'avoir pyarrow installé

        # Sauvegarder le DataFrame en CSV
        df.to_csv(csv_file, index=False)
        print(f"Fichier CSV généré avec succès : {csv_file}")
    except Exception as e:
        print(f"Erreur lors de la conversion : {e}")
        raise


def main():
    # Charger les variables d'environnement
    env_file = ".env"
    try:
        if os.path.exists(env_file):
            with open(env_file, "r") as file:
                for line in file:
                    # Ignorer les commentaires et lignes vides
                    if line.strip() and not line.startswith("#"):
                        key, value = line.strip().split("=", 1)
                        os.environ[key] = value.strip('"')  # Supprimer les guillemets
    except FileNotFoundError as e:
        print(e)
        return

    # Récupérer les fichiers à traiter
    parquet_file = os.getenv("LOCAL_PARQUET_FILE", "local_data.parquet")
    csv_file = os.getenv("OUTPUT_CSV_FILE", "output_data.csv")

    # Convertir le fichier Parquet en CSV
    try:
        convert_parquet_to_csv(parquet_file, csv_file)
    except Exception as e:
        print(f"Une erreur est survenue : {e}")


if __name__ == "__main__":
    main()
