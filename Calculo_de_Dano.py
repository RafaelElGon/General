import random

Damage_class = ""

Damage_type1 = ["perfurante","concussão","cortante"]
Damage_type2 = ["concussão-perfurante","cortante-perfurante"]
Weapon_type = ["DES","FOR","MDR"]

print()
print(">>Bem vindo ao programa de cálculo de dano! Informação importante, a formatação das respostas do usuário deve seguir a padronização de possuir acentos e caracteres especiais necessários; Ex: concussão-perfurante e CONCUSSÃO-PERFURANTE estão corretos, mas concussao ou cortante perfurante ou perfurante cortante, entre outros, não serão admitidos pelo código<<")

while( Damage_class != "x"):
    print()
    print("Tipos de danos: ",Damage_type1)
    print()
    print("Tipos de danos: ", Damage_type2)
    print()
    Damage_class = str.lower(input("Tipo de dano: "))
    
    if(Damage_class not in Damage_type1) and (Damage_class not in Damage_type2):
        while (Damage_class not in Damage_type1) and (Damage_class not in Damage_type2):
            Damage_class = str.lower(input("Tipo de dano informado não corresponde, tente novamente: "))

    if(Damage_class in Damage_type1):
        d8 = 8
        dice_result = random.randint(1,d8)
        print("Resultado do d8 > ",dice_result)
    elif(Damage_class in Damage_type2):
        d12 = 12
        dice_result = random.randint(1,d12)
        print("Resultado do d12 > ",dice_result)
    
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
            print("Resultado do d4 > ",d4)
    
    DES = int(input("Modificador de destreza: "))
    FOR = int(input("Modificador de força: "))

    if(Weapon_class == "DES"):
        damage = ((dice_result + DES + d4) // 1.2) - FOR
    elif(Weapon_class == "FOR"):
        damage = ((dice_result + FOR + d4) // 1.2) - DES
    else:
        if(FOR > DES):
            damage = (dice_result + FOR // 1.2) - DES
        else:
            damage = (dice_result + DES // 1.2) - FOR
    print()
    print("O dano é de: ", damage)
    print()
    Damage_class = str.lower(input("Digite x para fechar, se quiser continuar rolando, pressione ENTER "))
