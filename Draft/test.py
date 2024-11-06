import json

# Chemin vers votre fichier JSON existant
file_path = 'DDX51_human.json'  # Remplacez par le chemin vers votre fichier existant


# Étape 1 : Lire le fichier JSON existant
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)  # Charger le contenu JSON existant
except FileNotFoundError:
    print(f"Erreur : Le fichier '{file_path}' n'existe pas.")
except json.JSONDecodeError:
    print(f"Erreur : Le fichier '{file_path}' ne contient pas un JSON valide.")
else:
    # Étape 2 : Écrire les données dans le fichier avec indentations
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)  # Écrire les données avec une indentation de 4 espaces

    print(f"Données écrites dans le fichier '{file_path}' avec succès avec indentation.")
