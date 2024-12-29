import os
import unicodedata

def normalize_filename(filename):
    # Sépare le nom de fichier et son extension
    if "." in filename:
        name, extension = filename.rsplit(".", 1)
        extension = "." + extension
    else:
        name, extension = filename, ""

    # Remplace les espaces et tirets par des underscores dans le nom (pas l'extension)
    name = name.replace(" ", "_").replace("-", "_")
    # Remplace plusieurs underscores consécutifs par un seul
    while "__" in name:
        name = name.replace("__", "_")
    # Remplace "_." par "."
    if name.endswith("_."):
        name = name[:-2] + "."
    # Met en minuscules
    name = name.lower()
    # Supprime les accents
    name = ''.join(
        (c for c in unicodedata.normalize('NFD', name) if unicodedata.category(c) != 'Mn')
    )

    return name + extension

def rename_files_and_directories(directory):
    try:
        for root, dirs, files in os.walk(directory, topdown=False):
            # Renommer les fichiers
            for filename in files:
                old_path = os.path.join(root, filename)
                new_filename = normalize_filename(filename)
                new_path = os.path.join(root, new_filename)
                if old_path != new_path:  # Évite les erreurs si le nom ne change pas
                    os.rename(old_path, new_path)
                    print(f'Renamed file: "{old_path}" -> "{new_path}"')

            # Renommer les dossiers
            for dirname in dirs:
                old_path = os.path.join(root, dirname)
                new_dirname = normalize_filename(dirname)
                new_path = os.path.join(root, new_dirname)
                if old_path != new_path:  # Évite les erreurs si le nom ne change pas
                    os.rename(old_path, new_path)
                    print(f'Renamed directory: "{old_path}" -> "{new_path}"')

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    directory = input("Enter the directory path: ").strip()
    if os.path.isdir(directory):
        rename_files_and_directories(directory)
    else:
        print("The provided path is not a valid directory.")
