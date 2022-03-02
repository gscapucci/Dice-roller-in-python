import dice_roller as dr

def main():
    roller = dr.DiceRoller()
    
    while True:
        print('Type a number of dices you want to roll and number of faces each dice has.')
        dices = int(input('Dices:'))
        faces = int(input('Faces:'))
        roller.roll(dices, faces)
        continue_rolling = input('Continue(Y(Yes)/N(No))? ')
        if continue_rolling == 'N' or continue_rolling == 'No':
            break
        elif continue_rolling == 'Y' or continue_rolling == 'Yes':
            pass
        else:
            raise Exception("Input error, input must to be Y(Yes) or N(No)")

if __name__ == "__main__":
    main()
