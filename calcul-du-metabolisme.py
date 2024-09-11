def BRM_homme():
    poids_en_kilos_homme = int(input("veuillez entrer votre poids en kg : \n"))
    hauteur_en_centimetre_homme = int(input("veuillez entrer votre taille en centimétres : \n"))
    age_homme = int(input("veuillez entrer votre age : \n"))
    BRM = 66 + 13.7 * poids_en_kilos_homme + 5 * hauteur_en_centimetre_homme - 6.8 * age_homme
    print(f"votre BRM est de {BRM}\n")
    return BRM


def BRMa_homme(a):
    Niveau_activite = int(input("Pour calculer votre BRMa (Nombre de calories par jour pour garder un poids constant) , veuillez entrer niveau d'activité : \n 5 choix possibles : \n sedentaire : choix 1\n Tres_faible_activite : choix 2 \n Activite_legere : choix 3 \n Activite_modere : choix 4 \n Haute_activite : choix 5 \n Activite_extreme : choix 6 \n"))
    sedentaire = 1
    Tres_faible_activite = 1.2
    Activite_legere = 1.4
    Activite_modere = 1.6
    Haute_activite = 1.8
    Activite_extreme = 2
    if Niveau_activite == 1:
        Niveau_activite = sedentaire
    elif Niveau_activite == 2:
        Niveau_activite = Tres_faible_activite
    elif Niveau_activite == 3:
        Niveau_activite = Activite_legere
    elif Niveau_activite == 4:
        Niveau_activite = Activite_modere
    elif Niveau_activite == 5:
        Niveau_activite = Haute_activite
    elif Niveau_activite == 6:
        Niveau_activite = Activite_extreme
    else:
        print("Veuillez entrer un chiffre valide entre 1 et 6")
    BRMa = a * Niveau_activite
    BRMa = float(BRMa)
    print(f"votre BRMa est de {BRMa}\n")
    return BRMa

def objectif_homme(a):
    souhait = ""
    while souhait != "maigrir" and souhait != "grossir":
        souhait = input("souhaitez vous maigrir ou grossir ? \n").lower()
        if souhait == "maigrir":
            calcul_final = a - a*10/ 100
            print(f"{calcul_final} est votre metablisme de base pour maigrir doucement et sainement \n")
        elif souhait == "grossir":
            calcul_final = a + a*10 / 100
            print(f"{calcul_final} est votre metablisme de base pour grossir doucement et sainement \n")
        else:
            print("Veuillez entrer un souhait valide (maigrir ou grossir) :\n")
    return souhait






def BRM_femme():
    poids_en_kilos_femme = int(input("veuillez entrer votre poids en kg : \n"))
    hauteur_en_centimetre_femme = int(input("veuillez entrer votre taille en centimétres : \n"))
    age_femme = int(input("veuillez entrer votre age : \n"))
    BRM = 655 + 9.6 * poids_en_kilos_femme + 1.7 * hauteur_en_centimetre_femme - 4.7 * age_femme
    print(f"votre BRM est de {BRM}\n")
    return BRM

def BRMa_femme(a):
    Niveau_activite = int(input("Pour calculer votre BRMa (Nombre de calories par jour pour garder un poids constant) , veuillez entrer niveau d'activité :\n 5 choix possibles : \n sedentaire : choix 1\n Tres_faible_activite : choix 2 \n Activite_legere : choix 3 \n Activite_modere : choix 4 \n Haute_activite : choix 5 \n Activite_extreme : choix 6 \n"))
    sedentaire = 1
    Tres_faible_activite = 1.2
    Activite_legere = 1.4
    Activite_modere = 1.6
    Haute_activite = 1.8
    Activite_extreme = 2
    if Niveau_activite == 1:
        Niveau_activite = sedentaire
    elif Niveau_activite == 2:
        Niveau_activite = Tres_faible_activite
    elif Niveau_activite == 3:
        Niveau_activite = Activite_legere
    elif Niveau_activite == 4:
        Niveau_activite = Activite_modere
    elif Niveau_activite == 5:
        Niveau_activite = Haute_activite
    elif Niveau_activite == 6:
        Niveau_activite = Activite_extreme
    else:
        print("Veuillez entrer un chiffre valide entre 1 et 6")
    BRMa = a * Niveau_activite
    BRMa = float(BRMa)
    print(f"votre BRMa est de {BRMa}")
    return BRMa

def objectif_femme(a):
    souhait = ""
    while souhait != "maigrir" and souhait != "grossir":
        souhait = input("souhaitez-vous maigrir ou grossir ? \n").lower()
        if souhait == "maigrir":
            calcul_final = a - a * 10 / 100
            print(f"{calcul_final} est votre métabolisme de base pour maigrir doucement et sainement \n")
        elif souhait == "grossir":
            calcul_final = a + a * 10 / 100
            print(f"{calcul_final} est votre métabolisme de base pour grossir doucement et sainement \n")
        else:
            print("Veuillez entrer un souhait valide (maigrir ou grossir) :\n")
    return souhait

sexe = ""

while sexe != "homme" and sexe != "femme":
    sexe = input("Quel est votre sexe, homme/femme ? : \n").lower()
    if sexe == "homme":
        # On récupère le BRM
        BRM = BRM_homme()
        # On calcule le BRMa avec la valeur de BRM
        BRMa = BRMa_homme(BRM)
        # On définit l'objectif (maigrir ou grossir) avec la valeur de BRMa
        objectif_homme(BRMa)
    elif sexe == "femme":
        # On récupère le BRM
        BRM = BRM_femme()
        # On calcule le BRMa avec la valeur de BRM
        BRMa = BRMa_femme(BRM)
        # On définit l'objectif (maigrir ou grossir) avec la valeur de BRMa
        objectif_femme(BRMa)
    else:
        print("Veuillez entrer un sexe valide (homme ou femme) :\n")



