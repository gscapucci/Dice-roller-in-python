from tracemalloc import stop
import dice_roller

def main():
    roller = dice_roller.DiceRoller()
    while True:
        print("Type a number of dices you want to roll and number of faces each dice has.")
        dices = int(input("Dices:"))
        faces = int(input("Faces:"))
        roller.roll(dices, faces)
        continue_rolling = input("Continue")