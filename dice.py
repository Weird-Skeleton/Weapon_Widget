
import random
from random import randint

class Dice:

    def __init__(self, x: int, y: int, z = 0):
        self.num_dice = x
        self.num_faces = y
        self.modifier = z

    def __init__(self, input: String, z = 0):
        input_list = map(split(input))
        self.num_dice = input_list[0]
        self.num_faces = input_list[1]
        self.modifier = z

    def roll(self):
        result = 0
        for a in range(self.x):
            result += randint(1,self.y)
        result += self.z
        return result

    @staticmethod
    def roll(x: int, y: int, z = 0):
        result = 0
        for a in range(x):
            result += randint(1,y)
        result += z
        return result
