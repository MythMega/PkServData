import os
from PIL import Image

def convert_webp_to_png(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".webp"):
            filepath = os.path.join(directory, filename)
            with Image.open(filepath) as img:
                png_filename = filename.rsplit(".", 1)[0] + ".png"
                png_filepath = os.path.join(directory, png_filename)
                img.save(png_filepath, "PNG")
                print(f"Converti: {filename} -> {png_filename}")

if __name__ == "__main__":
    current_directory = os.getcwd()
    convert_webp_to_png(current_directory)
