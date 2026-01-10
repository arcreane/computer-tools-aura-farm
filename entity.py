#class defining entities
import pygame as pg
import time as t
import random as r
import math as m
from FX import VFX

class Entity:
    def __init__(self,name):
        self._name = name
        self._position = (0,0)
        self._hitboxRectangle = pg.rect.Rect(0,0,0,0)
        self._spriteSheet = None
        self._spawned = False
    def spawn(self):
        self._spawned = True

    def despawn(self):
        self._spawned = False

    def draw(self):
        if self._spawned:
            VFX.afficher(self)

class Bullet(Entity):
    def __init__(self,vector:tuple):
        super().__init__('Bullet')
        self._vector = vector

class Player(Entity):
    def __init__(self):
        super().__init__('Player')
        self._hp = 100
        self._weapons = []
        self._bonusList = []
        self._bulletList = []
    def hit(self, damage):
        self._hp -= damage

    def addBullet(self,bullet:Bullet):
        self._bulletList.append(bullet)

class Enemy(Entity):
    def __init__(self,name,hp):
        super().__init__(name)
        self._hp = hp


def hitBoxCheck(rectangle1,rectangle2):
    if rectangle1.colliderect(rectangle2):
        return True
    else:
        return False