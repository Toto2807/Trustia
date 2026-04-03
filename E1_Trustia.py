#Exercice 1

Max_Width = 100
phrases = {
    "maintenance":    "Le code propre facilite la maintenance",
    "tester":         "Tester souvent évite beaucoup d erreurs",
    "pas_afficher_1": "Cette phrase ne doit pas s afficher",
    "simple":         "Un bon code doit rester simple et clair",
    "simplicite":     "La simplicité améliore la qualité du code",
    "refacto":        "Refactoriser améliore la compréhension",
    "pas_afficher_2": "Cette phrase ne doit pas s afficher",
}

blocs = [    
    ["maintenance"],
    ["tester"],
    ["pas_afficher_2","simplicite","refacto"]
]

def affiche(cles):
    lignes = [phrases[cle] for cle in cles]
    largeur = min(Max_Width , max(len(ligne) for ligne in lignes) + 4)
    bordure = "-" * largeur
    print(bordure)
    for ligne in lignes:
        contenu = ligne.rjust(largeur - 4)
        print(f"| {contenu} |")
    print(bordure)

for bloc in blocs:
    affiche(bloc)
    print()