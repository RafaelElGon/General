import random

Damage_class = ""

Damage_type1 = ["perfurante","concussão","cortante"]
Damage_type2 = ["concussão-perfurante","cortante-perfurante"]
Weapon_type = ["DES","FOR","MDR"]

while( Damage_class != "x"):
    print()
    print("Tipos de danos: ",Damage_type1)
    print()
    print("Tipos de danos: ", Damage_type2)
    print()
    Damage_class = str.lower(input("Tipo de dano: "))
    
    if(Damage_class not in Damage_type1):
        while (Damage_class not in Damage_type1):
            Damage_class = str.lower(input("Tipo de dano informado não corresponde, tente novamente: "))

    if(Damage_class in Damage_type1):
        d8 = 8
        dice_result = random.randint(1,d8)
        print(dice_result)
    elif(Damage_class in Damage_type2):
        d12 = 12
        dice_result = random.randint(1,d12)
        print(dice_result)
    
    print()
    print("Opções de classes de armas: ",Weapon_type)
    print()
    Weapon_class = str.upper(input("Classe da arma: "))

    if(Weapon_class not in Weapon_type):
        while (Weapon_class not in Weapon_type):
            Weapon_class = str.upper(input("Tipo de classe informada não corresponde, tente novamente: "))

    for i in range(len(Weapon_type)):
        if(Weapon_class in Weapon_type[i]):
            d4 = random.randint(1,4)
    
    if(Weapon_class == "DES"):
        DES = int(input("Modificador de destreza: "))
        damage = (dice_result // 1.2) + DES + d4
    elif(Weapon_class == "FOR"):
        FOR = int(input("Modificador de força: "))
        damage = (dice_result // 1.2) + FOR + d4
    else:
        DES = int(input("Modificador de destreza: "))
        FOR = int(input("Modificador de força: "))
        
        if(FOR > DES):
            damage = (dice_result // 1.2) + FOR
        else:
            damage = (dice_result // 1.2) + DES
    print()
    print("O dano é de: ", damage)
    print()
    Damage_class = str.lower(input("digite x para fechar, se quiser continuar rolando, aperte qualquer tecla "))
