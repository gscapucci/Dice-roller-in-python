import random
import sys


class DiceRoller :
    
    def __init__(self) -> None:
        self.number_of_rolls = 0
        self._numbers = []
        self._sum = 0

    def _print(self) -> None:
        print(self._numbers, " = ", self._sum)
        
    def _reset(self):
        self._numbers.clear()
        self._sum = 0
    
    def roll(self, number_of_dices: int, number_of_faces: int):
        if number_of_dices < 1:
            raise Exception("Number of dices less than one.")
        if number_of_faces < 1:
            raise Exception("Number of faces less than one.")
        
        for _ in range(number_of_dices):
            num = (random.randint(1, number_of_faces))
            self._numbers.append(num)
            self._sum += num
        
        self.number_of_rolls += 1
        print("Roll number {}({}D{}):".format(self.number_of_rolls, number_of_dices, number_of_faces))
        self._print()
        self._reset()



if __name__ == "__main__":
    argv = sys.argv[1:]
    if len(argv) < 2:
        raise Exception("Usage: python " + sys.argv[0] + " <number of dices> <number of faces>")

    roller = DiceRoller()
    roller.roll(int(argv[0]), int(argv[1]))


