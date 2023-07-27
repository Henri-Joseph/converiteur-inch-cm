# Initialisation des valeurs par default (pouce - centimetre / centimetre - pouce) - ETAPE 1
POUCE = 2.54
CM = 0.394

# Choix de l'opération a effectué - ETAPE 2
def demande_convertion():
    print("1 - Convertion de pouce à cm | 2 - Convertion de cm à pouce")
    print()
    choix_int = 0
    while choix_int == 0:
        choix = input("Entrer 1 ou 2 pour le choix de votre convertion : ")
        try:
            choix_int = int(choix)
        except ValueError:
            print("ERREUR : Entrer une valeur comme indiquer")
    return choix_int


# Converstion de pouce à cm avec les contraintes - ETAPE 4a
def convertion_un():
    valPouceFloat = "x"
    # Verification du type de la vaariable
    while valPouceFloat == "x":
        valPouce = input("Entrer la valeur (Entier/Réel) à convertir de pouce à cm ")
        try:
            valPouceFloat = float(valPouce)
        except ValueError:
            print("Respectez l'instruction ci-dessous")
    # Validation du type de la variable et convertion
    x = isinstance(valPouceFloat, (float, int))
    if x:
        valPoucetoCm = valPouceFloat * POUCE
    else:
        valPoucetoCm = "x"
    return valPoucetoCm

# Converstion de pouce à cm avec les contraintes - ETAPE 4b
def convertion_deux():
    valPouceFloatD = "y"
    # Verification du type de la vaariable
    while valPouceFloatD == "y":
        valPouceD = input("Entrer la valeur (Entier/Réel) à convertir de cm à pouce ")
        try:
            valPouceFloatD = float(valPouceD)
        except ValueError:
            print("Respectez l'instruction ci-dessous")
    # Validation du type de la variable et convertion
    x = isinstance(valPouceFloatD, (float, int))
    if x:
        valCmtoPouce = valPouceFloatD * CM
    else:
        valCmtoPouce = "y"
    return valCmtoPouce


# Verification de l'instruction demandée - ETAPE 3
vChoix = 0
while not vChoix == 1 and not vChoix == 2:
    vChoix = demande_convertion()

# Convertion selon le mode choisi
if vChoix == 1:
    resulCon = "x"
    while resulCon == "x":
        resulCon = convertion_un()
    print(f"Le resultat de la convetion est {resulCon} Cm")
elif vChoix == 2:
    resulConD = "y"
    while resulConD == "y":
        resulConD = convertion_deux()
    print(f"Le resultat de la convertion est {resulConD} Inch")
else:
    print("Respecter les consignes suivantes")

