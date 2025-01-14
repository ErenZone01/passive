import os

def Display(text):
    base_filename = "result"
    extension = ".txt"
    filename = base_filename + extension
    counter = 1

    # Vérifier si le fichier existe déjà et incrémenter le compteur
    while os.path.exists(filename):
        filename = f"{base_filename}_{counter}{extension}"
        counter += 1

    # Créer et écrire dans le fichier
    with open(filename, "w") as fichier:
        fichier.write(text + "\n")

    print(f"Saved in : {filename}")
