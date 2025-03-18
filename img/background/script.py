#!/usr/bin/env python3
import os
from PIL import Image

def crop_center(img, crop_width, crop_height):
    """
    Recadre l'image en centrant sur une zone de taille crop_width x crop_height.
    """
    img_width, img_height = img.size
    left = (img_width - crop_width) // 2
    top = (img_height - crop_height) // 2
    right = left + crop_width
    bottom = top + crop_height
    return img.crop((left, top, right, bottom))

# Paramètres cibles
TARGET_WIDTH = 856
TARGET_HEIGHT = 540

# Liste pour enregistrer les noms de fichiers qui ne remplissent pas les conditions
to_fix_files = []

# Parcours de tous les fichiers du dossier courant
for filename in os.listdir('.'):
    if filename.lower().endswith('.jpg'):
        try:
            with Image.open(filename) as img:
                # S'assurer que l'image est en mode RGB (pour éviter certains problèmes)
                img = img.convert("RGB")
                width, height = img.size
                processed = False

                # Cas 1: l'image a des dimensions suffisantes pour un crop direct
                if width >= TARGET_WIDTH and height >= TARGET_HEIGHT:
                    cropped = crop_center(img, TARGET_WIDTH, TARGET_HEIGHT)
                    new_filename = "card_" + filename
                    cropped.save(new_filename)
                    processed = True
                    print(f"Traitée (crop direct): {filename} -> {new_filename}")

                # Cas 2: on essaie en rotation de 90° si le crop direct n'est pas possible
                elif height >= TARGET_WIDTH and width >= TARGET_HEIGHT:
                    # Utilisation de transpose pour une rotation de 90° (dans le sens horaire)
                    rotated = img.transpose(Image.ROTATE_90)
                    r_width, r_height = rotated.size
                    if r_width >= TARGET_WIDTH and r_height >= TARGET_HEIGHT:
                        cropped = crop_center(rotated, TARGET_WIDTH, TARGET_HEIGHT)
                        new_filename = "card_" + filename
                        cropped.save(new_filename)
                        processed = True
                        print(f"Traitée (rotation 90°): {filename} -> {new_filename}")

                # Si aucune condition n'est remplie, on note le fichier pour correction manuelle
                if not processed:
                    to_fix_files.append(filename)
                    print(f"Ne répond pas aux conditions: {filename}")

        except Exception as e:
            print(f"Erreur lors du traitement du fichier {filename}: {e}")
            to_fix_files.append(filename)

# Sauvegarde la liste des fichiers à corriger dans _tofix.txt
with open("_tofix.txt", "w") as f:
    for f_name in to_fix_files:
        f.write(f_name + "\n")

print("Traitement terminé.")
