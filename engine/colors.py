# Egyedi RGB színek definiálása
player_palette = [
    (128, 128, 128),  # Szürke
    (0, 255, 0),  # Zöld
    (255, 0, 0),  # Piros
    (0, 0, 255),  # Kék
    (255, 255, 0),  # Sárga
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cián
    (128, 0, 0),  # Sötét piros
    (0, 128, 0),  # Sötét zöld
    (0, 0, 128),  # Sötét kék
    (128, 128, 0),  # Sötét sárga
    (128, 0, 128),  # Sötét magenta
    (0, 128, 128),  # Sötét cián
    (192, 192, 192),  # Ezüst
    (255, 165, 0),  # Narancs
    (0, 128, 0),  # Olíva
    (128, 0, 0),  # Barna
    (255, 192, 203),  # Rózsaszín
    (255, 218, 185),  # Gyöngyházfehér
    (0, 0, 128),  # Tengerészkék
    (0, 128, 128),  # Menta
    (0, 0, 0),  # Fekete
    (255, 255, 255)  # Fehér
]


def get_distinct_color(index):
    """
    Választ egy színt egyedi RGB értékekkel egy adott index alapján.

    Parameters:
    - index (int): Az index, amely alapján a színt kiválasztjuk (0-31).

    Returns:
    - color (tuple): Az RGB színtérben kifejezett szín.
    """
    # Ellenőrzés, hogy az index 0 és 31 közé essen
    index = max(0, min(index, 31))

    return player_palette[index]
