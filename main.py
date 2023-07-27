# Initialisation des valeurs par default (pouce - centimetre / centimetre - pouce)
POUCE = 2.54
CM = 0.394

# Choix de l'opération a effectué
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


# Verification de l'instruction demandée
vChoix = 0
while not vChoix == 1 and not vChoix == 2:
    vChoix = demande_convertion()


if vChoix == 1:
    print("Convertion de pouce à cm")
elif vChoix == 2:
    print("Convertion de cm à pouce")
else:
    print("Respecter les consignes suivantes")

