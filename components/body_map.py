from PIL import Image, ImageDraw

BODY_IMG_PATH = "assets/player__figure_injures.png"

ZONAS_COORDS = {
    "Cabeza": (150, 50),
    "Espalda": (150, 150),
    "Brazo": (220, 160),
    "Muslo": (150, 260),
    "Rodilla": (150, 320),
    "Tobillo": (150, 380),
    "Pie": (150, 430),
}

def draw_body_with_markers(zonas):
    base = Image.open(BODY_IMG_PATH).convert("RGBA")
    draw = ImageDraw.Draw(base)

    for zona in zonas:
        if zona in ZONAS_COORDS:
            x, y = ZONAS_COORDS[zona]
            r = 10
            draw.ellipse((x - r, y - r, x + r, y + r), fill=(255, 0, 0, 200))

    return base
