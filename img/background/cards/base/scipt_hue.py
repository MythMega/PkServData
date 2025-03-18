import cv2
import numpy as np

# Chargement de l'image de base
img = cv2.imread("base_card_blue.jpg")
if img is None:
    print("Erreur : L'image 'base_card_blue.jpg' n'a pas pu être chargée.")
    exit(1)

# Conversion de BGR à HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Liste de noms de couleurs en anglais pour chaque nuance (approximativement selon le cercle chromatique)
color_names = [
    "red",           # 0° (0 en OpenCV)
    "red_orange",    # 18°
    "orange",        # 36°
    "yellow_orange", # 54°
    "yellow",        # 72°
    "chartreuse",    # 90°
    "green",         # 108°
    "teal",          # 126° (équivalent à vert d'eau)
    "turquoise",     # 144°
    "cyan",          # 162°
    "blue_cyan",     # 180°
    "blue",          # 198°
    "blue_violet",   # 216°
    "violet",        # 234°
    "magenta",       # 252°
    "purple",        # 270°
    "pink",          # 288°
    "hot_pink",      # 306°
    "fuchsia",       # 324°
    "burgundy"       # 342°
]

# Pour 20 couleurs, on va incrémenter le canal Hue par un pas de 9 (car 9 * 20 = 180)
for i, name in enumerate(color_names):
    new_hue = i * 9  # Nouvelle valeur de Hue (entre 0 et 171)

    # Copie de l'image en HSV pour modification
    hsv_mod = hsv_img.copy()
    
    # Modification du canal Hue pour tous les pixels (les canaux Saturation et Value restent inchangés)
    hsv_mod[:, :, 0] = new_hue

    # Conversion retour de HSV vers BGR
    bgr_mod = cv2.cvtColor(hsv_mod, cv2.COLOR_HSV2BGR)

    # Nom de fichier de sortie
    filename = f"base_card_{name}.jpg"

    # Sauvegarde de l'image modifiée
    cv2.imwrite(filename, bgr_mod)

print("Les images ont été générées avec succès.")
