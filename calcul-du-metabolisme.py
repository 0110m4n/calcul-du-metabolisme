# Fonction pour calculer le BRM pour les hommes
def BRM_homme():
    # Demande du poids, de la taille et de l'âge
    poids_en_kilos_homme = int(input("veuillez entrer votre poids en kg : \n"))
    hauteur_en_centimetre_homme = int(input("veuillez entrer votre taille en centimétres : \n"))
    age_homme = int(input("veuillez entrer votre age : \n"))
    # Calcul du BRM selon la formule de Harris-Benedict pour les hommes
    BRM = 66 + 13.7 * poids_en_kilos_homme + 5 * hauteur_en_centimetre_homme - 6.8 * age_homme
    print(f"votre BRM est de {BRM:.2f}\n")
    return BRM

# Fonction pour calculer le BRMa (BRM ajusté par le niveau d'activité) pour les hommes
def BRMa_homme(a):
    Niveau_activite = int(input("Pour calculer votre BRMa (Nombre de calories par jour pour garder un poids constant) , veuillez entrer niveau d'activité :\n 5 choix possibles : \n sedentaire : choix 1\n Tres_faible_activite : choix 2 \n Activite_legere : choix 3 \n Activite_modere : choix 4 \n Haute_activite : choix 5 \n Activite_extreme : choix 6 \n"))
    dict_niveau_activite = {
        1 : 1,
        2 : 1.2,
        3 : 1.4,
        4 : 1.6,
        5 : 1.8,
        6 : 2
        }
    Niveau_activite = dict_niveau_activite.get(Niveau_activite)
    BRMa = a * Niveau_activite
    BRMa = float(BRMa)
    print(f"votre BRMa est de {BRMa:.2f}")
    return BRMa


# Fonction pour ajuster le BRMa en fonction de l'objectif (maigrir ou grossir) pour les hommes
def objectif_homme(a):
    souhait = ""
    # Demande de l'objectif utilisateur jusqu'à recevoir une réponse valide
    while souhait != "maigrir" and souhait != "grossir":
        souhait = input("souhaitez vous maigrir ou grossir ? \n").lower()
        # Calcul du métabolisme ajusté pour maigrir
        if souhait == "maigrir":
            calcul_final = a - a * 10 / 100
            print(f"{calcul_final:.2f} est votre metablisme de base pour maigrir doucement et sainement \n")
        # Calcul du métabolisme ajusté pour grossir
        elif souhait == "grossir":
            calcul_final = a + a * 10 / 100
            print(f"{calcul_final:.2f} est votre metablisme de base pour grossir doucement et sainement \n")
        else:
            print("Veuillez entrer un souhait valide (maigrir ou grossir) :\n")
    return souhait

# Fonction pour calculer le BRM pour les femmes (même logique que pour les hommes)
def BRM_femme():
    poids_en_kilos_femme = int(input("veuillez entrer votre poids en kg : \n"))
    hauteur_en_centimetre_femme = int(input("veuillez entrer votre taille en centimétres : \n"))
    age_femme = int(input("veuillez entrer votre age : \n"))
    BRM = 655 + 9.6 * poids_en_kilos_femme + 1.7 * hauteur_en_centimetre_femme - 4.7 * age_femme
    print(f"votre BRM est de {BRM:.2f}\n")
    return BRM

# Fonction pour calculer le BRMa pour les femmes (même logique que pour les hommes)
def BRMa_femme(a):
    Niveau_activite = int(input("Pour calculer votre BRMa (Nombre de calories par jour pour garder un poids constant) , veuillez entrer niveau d'activité :\n 5 choix possibles : \n sedentaire : choix 1\n Tres_faible_activite : choix 2 \n Activite_legere : choix 3 \n Activite_modere : choix 4 \n Haute_activite : choix 5 \n Activite_extreme : choix 6 \n"))
    dict_niveau_activite = {
        1 : 1,
        2 : 1.2,
        3 : 1.4,
        4 : 1.6,
        5 : 1.8,
        6 : 2
        }
    Niveau_activite = dict_niveau_activite.get(Niveau_activite)
    BRMa = a * Niveau_activite
    BRMa = float(BRMa)
    print(f"votre BRMa est de {BRMa:.2f}")
    return BRMa

# Fonction pour ajuster le BRMa en fonction de l'objectif pour les femmes
def objectif_femme(a):
    souhait = ""
    while souhait != "maigrir" and souhait != "grossir":
        souhait = input("souhaitez-vous maigrir ou grossir ? \n").lower()
        if souhait == "maigrir":
            calcul_final = a - a * 10 / 100
            print(f"{calcul_final:.2f} est votre métabolisme de base pour maigrir doucement et sainement \n")
        elif souhait == "grossir":
            calcul_final = a + a * 10 / 100
            print(f"{calcul_final:.2f} est votre métabolisme de base pour grossir doucement et sainement \n")
        else:
            print("Veuillez entrer un souhait valide (maigrir ou grossir) :\n")
    return souhait

# Demande du sexe utilisateur pour ajuster le calcul
sexe = ""

while sexe != "homme" and sexe != "femme":
    sexe = input("Quel est votre sexe, homme/femme ? : \n").lower()
    if sexe == "homme":
        # Calcul du BRM, BRMa et objectif pour un homme
        BRM = BRM_homme()
        BRMa = BRMa_homme(BRM)
        objectif_homme(BRMa)
    elif sexe == "femme":
        # Calcul du BRM, BRMa et objectif pour une femme
        BRM = BRM_femme()
        BRMa = BRMa_femme(BRM)
        objectif_femme(BRMa)
    else:
        print("Veuillez entrer un sexe valide (homme ou femme) :\n")
