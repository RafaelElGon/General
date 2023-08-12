import random

def Dice_Roll (initial_value,maximum_value):
    dice_result = random.randint(initial_value,maximum_value)
    if(maximum_value == 20):
        if(dice_result == 1):
            print("Erro crítico!")
        elif(dice_result >= 2 and dice_result <= 5):
            print("Erro ruim!")
        elif(dice_result >= 6 and dice_result <= 9):
            print("Nem acerto, nem erro.")
        elif(dice_result >= 10 and dice_result <= 15):
            print("Acerto bom!")
        elif(dice_result >= 16 and dice_result <= 19):
            print("Acerto muito bom!")
        else:
            print("Acerto crítico!")

    return dice_result
