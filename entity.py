#class defining entities
import pygame
import pygame as pg
import time as t
import random as r
import math as m
from FX import VFX
import weapons as w
shootTimer = t.perf_counter()
moveTimer = t.perf_counter()
lastUpdate = t.perf_counter()
class Entity:
    def __init__(self,name,position=(0,0),devMode=False):
        self._name = name
        self._position = position
        self._hitboxRectangle = pg.rect.Rect(5,3,5,5)
        self._spriteSheet = None
        self._spawned = False
        self._devMode = devMode
    def spawn(self):
        self._spawned = True

    def despawn(self):
        self._spawned = False

    def draw(self):
        if self._spawned:
            VFX.afficher(self)

class Bullet(Entity):
    def __init__(self,vector:tuple,devMode:bool = False):
        super().__init__('Bullet',position=(0,0),devMode = devMode)
        self._vector = vector
        self._damage = 5
        self._hitboxRectangle = pg.rect.Rect(1,2,1,1)
        self._lastUpdate = t.perf_counter()
    def __str__(self):
        return str([self._name,self._position,self._vector])
    def update(self,player):
        if t.perf_counter() - self._lastUpdate > 1:
            self._position = (self._position[0] + self._vector[0], self._position[1] + self._vector[1])
            #hitBoxCheck(self._hitboxRectangle,player)
            self._lastUpdate = t.perf_counter()

            if self._devMode:
                print(f'{self._name} a la position {self._position}')
class Player(Entity):
    def __init__(self,devMode:bool = False):
        super().__init__('Player',devMode = devMode)
        self._hp = 100
        self._weapons = [w.Normal(),w.Spread()]
        self._selectedWeaponId = 0
        self._selectedWeapon = self._weapons[self._selectedWeaponId]
        self._bonusList = []
        self._bulletList = []
    def hit(self, damage):
        self._hp -= damage

    def addBullet(self,bullet):
        print(f"{bullet._vector} vecteur du bullet")
        self._bulletList.append(bullet)

    def move(self,event):
        global moveTimer
        if event.type == pygame.KEYDOWN:
            print(f'keydown')
            print(f'{t.perf_counter() - moveTimer} temps cooldown move')
            if t.perf_counter() - moveTimer > 0.2:
                if event.key == pygame.K_LEFT:
                    print('player left')
                    if self._position[1] >= 2:
                        self._position = (self._position[0],self._position[1]-2)
                    moveTimer = t.perf_counter()
                elif event.key == pygame.K_RIGHT:
                    print('player right')
                    self._position = (self._position[0],self._position[1] + 2)
                    moveTimer = t.perf_counter()
                if event.key == pygame.K_UP:
                    print('player up')
                    self._position = (self._position[0] + 2, self._position[1])
                    moveTimer = t.perf_counter()
                elif event.key == pygame.K_DOWN:
                    print('player down')
                    if self._position[0] >= 2:
                     self._position =  ( self._position[0] - 2, self._position[1])
                    moveTimer = t.perf_counter()
        if self._devMode:
            print(f'{self._position} position joueur')
    def shoot(self):
        global shootTimer
        print('player shoot OK')
        givenVector = self._selectedWeapon.giveVector()
        print(f'{t.perf_counter() - shootTimer} temps cooldown')
        if t.perf_counter() - shootTimer > 0.2:
            self.addBullet(Bullet((0,1),True))
            print(f'{str(self._bulletList)} new bullet')
            shootTimer = t.perf_counter()

class Enemy(Entity):
    def __init__(self,name,hp,devMode=False):
        super().__init__(name,devMode = devMode)
        self._hp = hp


def hitBoxCheck(rectangle1,rectangle2):
    if rectangle1.colliderect(rectangle2):
        print('hitbox True')
        return True
    else:
        print('hitbox False')
        return False

def test():
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode((1000,700))
    clock = pygame.time.Clock()
    clock.tick(60)
    mobList = []
    run = True
    player = Player(devMode=True)
    mob1 = Enemy("mob1", 100, devMode=True)
    mobList.append(mob1)
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                player.move(event)
                if event.type == pg.MOUSEBUTTONDOWN:
                    print(player._bulletList)
                    player.shoot()
        for bullets in player._bulletList:
            bullets.update(player)

test()
