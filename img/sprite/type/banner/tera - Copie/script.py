#!/usr/bin/env python3
import os
from PIL import Image

def process_image(filename):
    # Ouvre l'image et récupère ses dimensions
    with Image.open(filename) as img:
        width, height = img.size
        target_size = 140

        # Vérifie que la largeur est bien de 140 pixels
        if width != target_size:
            print(f"Image {filename} ignorée : la largeur n'est pas de {target_size}px (trouvée {width}px).")
            return

        # Si l'image a déjà la hauteur désirée, on ne fait rien
        if height == target_size:
            print(f"Image {filename} déjà au format {target_size}x{target_size}.")
            return

        # Crée une nouvelle image avec fond transparent (mode RGBA)
        new_img = Image.new("RGBA", (target_size, target_size), (255, 255, 255, 0))

        # Calcule le décalage vertical pour centrer l'image d'origine
        top = (target_size - height) // 2

        # Colle l'image d'origine dans la nouvelle image
        new_img.paste(img, (0, top))

        # Sauvegarde l'image en écrasant l'originale
        new_img.save(filename)
        print(f"Image {filename} traitée : nouvelle taille {target_size}x{target_size}.")

def main():
    # Parcours tous les fichiers du répertoire courant
    for file in os.listdir('.'):
        if file.lower().endswith(".png"):
            process_image(file)

if __name__ == "__main__":
    main()
