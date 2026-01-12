import pygame
import time

pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)

pew = pygame.mixer.Sound("bone-undertale-sound-effect.mp3")
pew.play()

# Wait for the sound to finish playing (for testng only, game will loop and won't need it)
time.sleep(pew.get_length())  