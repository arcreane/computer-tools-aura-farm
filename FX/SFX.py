import pygame
import time

pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)

pygame.mixer.music.load("bgm1.wav")

pew = pygame.mixer.Sound("bone-undertale-sound-effect.mp3")
# pew.play()

# Wait for the sound to finish playing (for testing only, game will loop and won't need it)
# time.sleep(pew.get_length())  

pygame.mixer.music.play(-1)  # Loop forever

while True:
    pygame.time.Clock().tick(10)