#class defining entities
import pygame
import pygame as pg
import time as t
import random as r
import math as m
from FX import VFX
import weapons as w
class Entity:
    def __init__(self,name,position=(0,0),devMode=False):
        self._name = name
        self._position = position
        self._hitboxRectangle = pg.rect.Rect(0,0,0,0)
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
        super().__init__('Bullet',devMode)
        self._vector = vector
        self._damage = 5
        self._hitboxRectangle = pg.rect.Rect(1,2,1,1)
    def update(self,player):
        lastUpdate = t.perf_counter()
        if t.perf_counter() - lastUpdate > 0.2:
            self._position[0] += self._vector[0]
            self._position[1] += self._vector[1]
            hitBoxCheck(self._hitboxRectangle,player)

        if self._devMode:
            print(self._position)
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

    def addBullet(self,bullet:Bullet):
        self._bulletList.append(bullet)

    def move(self,event):
        moveTimer = t.time()
        if event.type == pygame.KEYDOWN:
            print(f'keydown')
            if moveTimer - t.time() > 0.2:
                if event.key == pygame.K_a:
                    print('player left')
                    if self._position[0] >= 2:
                        self._position[1] -= 2
                elif event.key == pygame.K_RIGHT:
                    print('player right')
                    self._position[1] += 2
                if event.key == pygame.K_UP:
                    print('player up')
                    self._position[0] += 2
                elif event.key == pygame.K_DOWN:
                    print('player down')
                    if self._position[0] >= 2:
                        self._position[0] -= 2
        if self._devMode:
            print(f'{self._position} position joueur')
    def shoot(self,event):
        print('player shoot OK')
        shootTimer = t.perf_counter()
        givenVector = self._selectedWeapon.giveVector()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and shootTimer - t.perf_counter() > 0.2:
            print(f'{self._bulletList} new bullet')
            self._bulletList.append(Bullet(givenVector))

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
    screen = pygame.display.set_mode((800,600))
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
                player.shoot(event)
        for bullets in player._bulletList:
            bullets.update(player)

test()