#Exercice 1
MAX_WIDTH = 100

data_store = {
    "bloc_1": [
        {"texte": "Le code propre facilite la maintenance", "active": True}
    ],
    "bloc_2": [
        {"texte": "Tester souvent évite beaucoup d erreurs", "active": True},
        {"texte": "Cette phrase ne doit pas s afficher", "active": False}
    ],
    "bloc_3": [
        {"texte": "Cette phrase ne doit pas s afficher", "active": True},
        {"texte": "Un bon code doit rester simple et clair", "active": False},
        {"texte": "La simplicité améliore la qualité du code", "active": True},
        {"texte": "Refactoriser améliore la compréhension", "active": True}
    ]
}


def afficher_blocs(data):
    for nom_bloc, phrases in data.items():
        ligne_afficher = [
            p["texte"].lower() for p in phrases if p["active"]
        ]
        if not ligne_afficher:
            continue
        largeur_contenu = max(len(l) for l in ligne_afficher)
        largeur_total = max(MAX_WIDTH, largeur_contenu + 4)

        bordure = "-" * largeur_total
        print(bordure)
        for ligne in ligne_afficher:
            print(f"| {ligne.rjust(largeur_total - 4)} |")
        print(bordure)
        print()

if __name__ == "__main__":
    afficher_blocs(data_store)