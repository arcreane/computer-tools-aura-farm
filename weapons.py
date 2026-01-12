import random as r
import math
import time





class Weapon:
    def __init__(self, name):
        self.name = name

class Normal(Weapon):
    def __init__(self):
        super().__init__("Normal")

    def giveVector(self):
        return tuple((1,0))

class Spread(Weapon):
    def __init__(self):
        super().__init__("Spread")
    def giveVector(self):
        Fx = 1
        Fy = r.randrange(0,11,1)
        Fy = Fy*0.1
        F = tuple((Fx,Fy))
        return F