import random

Damage_class = ""

Damage_type1 = ["perfurante","concussão","cortante"]
Damage_type2 = ["concussão-perfurante","cortante-perfurante"]

while( Damage_class != "x"):
    print()
    print("perfurante","concussão","cortante")
    print()
    print("concussão-perfurante","cortante-perfurante")
    print()
    Damage_class = str.lower(input("Tipo de dano: "))
    
    if(Damage_class in Damage_type1):
        dice = 8
        dice_result = random.randint(1,dice)
        print(dice_result)
    elif(Damage_class in Damage_type2):
        dice = 12
        dice_result = random.randint(1,dice)
        print(dice_result)

    FOR = int(input("Modificador de força: "))
    DES = int(input("Modificador de destreza: "))

    damage = dice_result + FOR 
    
    damage_result = (damage // (1.2)) + DES
    print("Dano: ", damage_result)

    Damage_class = str.lower(input("digite x para fechar, se quiser continuar rolando, aperte qualquer tecla "))
