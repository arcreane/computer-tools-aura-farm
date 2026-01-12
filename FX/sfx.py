import pygame

pygame.init()

pygame.mixer.init(44100, -16, 2, 2048)

pygame.mixer.music.load("musicfilename")

pew = pygame.mixer.Sound("bone-undertale-sound-effect")

#playing music 
# -1 is for looping, to test 

pygame.mixer.music.play(-1)

#playing sounds

pew.play()

#stopping music

pygame.mixer.music.stop()