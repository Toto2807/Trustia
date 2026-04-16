Menu = {
    "entrées": {
        "plats": [
            {"nom": "Salade César", "prix": 8, "disponible": True},
            {"nom": "Soupe du jour", "prix": 6, "disponible": False}
        ],
        "active": True
    },
    "plats": {
        "plats": [
            {"nom": "Steak frites", "prix": 15, "disponible": True},
            {"nom": "Poisson grillé", "prix": 14, "disponible": True},
            {"nom": "Plat du chef", "prix": 18, "disponible": False}
        ],
        "active": True
    },
    "desserts": {
        "plats": [
            {"nom": "Tiramisu", "prix": 7, "disponible": True},
            {"nom": "Glace", "prix": 5, "disponible": True},
            {"nom": "Dessert mystère", "prix": 9, "disponible": False}
        ],
        "active": True
    }
}

def afficher_menu(menu):
    for section, config in menu.items():
        if not config["active"]:
            continue
        print(f"-- {section.lower()} --")
        for item in config["plats"]:
            if not item["disponible"]:
                continue
            print(f" {item['nom'].lower()} - {item['prix']}€")
        print()

if __name__ == "__main__":
    afficher_menu(Menu)