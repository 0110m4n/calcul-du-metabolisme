from enum import Enum

"""
Je te doit quelques explications

Il existe sur python et en programmation en général une structure de donnée appelé énumération : https://docs.python.org/3/library/enum.html

Les énumérations Sexe, NiveauActivite, et Objectif permettent de définir des ensembles de valeurs prédéfinies.
Avec cette structure, on évite les répétitions de code, les erreurs potentielles et on rajoute de la modularitée ( regarde comme c'est simple de changer les coefficients)

Pour la fonctions de calcul j'ai repris et adapté à peut près ta structure :

 - calcul_brm : Calcule le métabolisme de base (BRM) en utilisant les coefficients spécifiques au sexe.
 - calcul_brma : Ajuste le BRM en fonction du niveau d'activité.
 - calcul_objectif_calorique : Ajuste le BRMa en fonction de l'objectif calorique.

Quelques points d'améliorations à te proposer :

- Évites les boucles et les conditions : ce que tu peut faire sans, fait le sans. Pas la peine de rajouter de la compléxitée.
-  Les structures de données sont tes meilleurs amies, adaptées, elles peuvent représenter tout tes ensembles de manière cohérentes. Gaffe à pas trop partir loin dans l'Orienté Objet tu risque de faire l'effet inverse.

En bref, pour bien coder, il suffit de te poser 5min, bien réfléchir à ce que tu veux faire, comment tu peux le représenter le plus efficacement possible. 90% de structuration, 10% de programmation.

"""

# Définition de l'énumération Sexe pour les coefficients de calcul du BRM
class Sexe(Enum):
    HOMME = (88.362, 13.397, 4.799, 5.677)  # Coefficients pour les hommes
    FEMME = (447.593, 9.247, 3.098, 4.330)  # Coefficients pour les femmes

# Définition de l'énumération NiveauActivite pour les coefficients de calcul du BRMa
class NiveauActivite(Enum):
    SEDENTAIRE = 1.2
    LEGER = 1.375
    MODERE = 1.55
    ACTIF = 1.725
    EXTREME = 1.9

# Définition de l'énumération Objectif pour les ajustements caloriques
class Objectif(Enum):
    PERDRE = -500
    GROSSIR = 500
    MAINTENIR = 0

# Fonction pour calculer le métabolisme de base (BRM)
def calcul_brm(poids, taille, age, sexe: Sexe):
    coefs = sexe.value  # Récupération des coefficients en fonction du sexe
    return coefs[0] + (coefs[1] * poids) + (coefs[2] * taille) - (coefs[3] * age)

# Fonction pour calculer le métabolisme de base ajusté (BRMa)
def calcul_brma(brm, activite: NiveauActivite):
    return brm * activite.value  # Multiplication du BRM par le coefficient d'activité

# Fonction pour calculer l'objectif calorique
def calcul_objectif_calorique(brma, objectif: Objectif):
    return brma + objectif.value  # Ajustement du BRMa en fonction de l'objectif

# Fonction principale du programme
def main():
    # Entrée des données utilisateur
    poids = float(input("Entrez votre poids en kg: "))
    taille = float(input("Entrez votre taille en cm: "))
    age = int(input("Entrez votre âge en années: "))
    sexe = Sexe[input("Entrez votre sexe (homme/femme): ").upper()]
    niveau_activite = NiveauActivite[input("Entrez votre niveau d'activité (sedentaire/leger/modere/actif/extreme): ").upper()]
    objectif = Objectif[input("Entrez votre objectif (perdre/grossir/maintenir): ").upper()]

    # Calculs des différentes valeurs
    brm = calcul_brm(poids, taille, age, sexe)
    brma = calcul_brma(brm, niveau_activite)
    objectif_calorique = calcul_objectif_calorique(brma, objectif)

    # Affichage des résultats
    print(f"Votre métabolisme de base (BRM) est de {brm:.2f} calories par jour.")
    print(f"Vos besoins caloriques ajustés (BRMa) sont de {brma:.2f} calories par jour.")
    print(f"Pour atteindre votre objectif, vous devez consommer {objectif_calorique:.2f} calories par jour.")

# Point d'entrée du programme
if __name__ == "__main__":
    main()
