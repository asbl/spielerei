import os
from PIL import Image, ExifTags

# Quell- und Zielverzeichnis
SRC = "static/images"
DEST = os.path.join(SRC, "web")
os.makedirs(DEST, exist_ok=True)

# Maximalgröße
MAX_SIZE = (1024, 1024)

# Hilfsfunktion für EXIF-Rotation
def correct_orientation(img):
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = img._getexif()
        if exif is not None:
            orientation_value = exif.get(orientation)
            if orientation_value == 3:
                img = img.rotate(180, expand=True)
            elif orientation_value == 6:
                img = img.rotate(270, expand=True)
            elif orientation_value == 8:
                img = img.rotate(90, expand=True)
    except Exception:
        pass
    return img

# Alle .jpg und .jpeg Dateien verarbeiten
for filename in os.listdir(SRC):
    if filename.lower().endswith((".jpg", ".jpeg")):
        src_path = os.path.join(SRC, filename)
        dest_path = os.path.join(DEST, filename)

        with Image.open(src_path) as img:
            img = correct_orientation(img)  # EXIF-Rotation korrigieren
            img.thumbnail(MAX_SIZE)
            img.save(dest_path, "JPEG", optimize=True, quality=85)

        print(f"Verarbeitet: {filename}")
