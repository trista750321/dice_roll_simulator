import random


while True:
    dice_rolled = random.randint(1, 6)
    roll_again = str(input("Roll the Dices? Y for yes or N for no : ").upper())
    if roll_again == "Y":
        print("Roll the Dices")
        print("The value is :")
        print(dice_rolled)
    else:
        break
