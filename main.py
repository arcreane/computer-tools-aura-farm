#main caller
import pygame
import entity
from FX import SFX,VFX,UI
from level import *
from STAFF_ONLY import *



def main():
    pygame.init()
    clock = pygame.time.Clock()
    clock.tick(60)
    print('Pygame OK')
    SFX.init()
    VFX.init()
    print('FX loaded')
    UI.draw()