import pygame, sys
from pygame.locals import *
from pygame.scrap import set_mode

buttonTexture =  pygame.image.load('button.jpg')
cat = pygame.image.load('cat.png')
car = pygame.image.load('car.png')

pygame.init()                                                       #startup
pygame.font.init()
pygame.display.init()

page = pygame.display.set_mode((1000, 700))                          #makes the main screen + gives it its main color
pygame.Surface.fill(page, (224,224,224))
pygame.display.set_caption('Aura Farm')
font = pygame.font.SysFont('Arial', 30)
clock = pygame.time.Clock()
clock.tick(60)

class Button:
    def __init__(self, x, y, width, height, address, image = pygame.image.load('button.jpg')):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.address = address

    def draw(self, screen):
        screen.blit(pygame.transform.scale(self.image,(self.width,self.height)), (self.x, self.y))


def load(pageinfo,screen):
    pygame.Surface.fill(page,(224,224,224))
    for item in pageinfo['button']:
        item.draw(page)
    for item in pageinfo['text']:
        screen.blit(font.render(item[0],item[1],item[2]),item[3])
    for item in pageinfo['image']:
        screen.blit(pygame.transform.scale(item[0],(item[3],item[4])), (item[1], item[2]))
    pygame.display.update()

mainmenuStartbutton = Button(100,100,100,100,'start',buttonTexture)
mainmenuSettingsbutton = Button(0,0,100,100,'settings',buttonTexture)
mainmenuCatbutton = Button(600,0,100,100,'catpage',cat)
mainmenuText1 = ['main menu', True, (0,0,0),(0,0)]
mainmenuText2 = ['aura farm industries present: yet another space attacks clone', True, (0,0,0),(0,500)]

catText = ['mioau', True, (0,0,0), (0,0)]
catImage = [car,100,100,100,100]
catReturnbutton = Button(0,600,100,100,'mainmenu',buttonTexture)

settingsButton = Button(0,0,100,100,'keybinds',buttonTexture)
settingsBackbutton = Button(250,250,100,100,'mainmenu',buttonTexture)
settingsText = ['settings', True, (0,0,0),(0,0)]


mainmenu = {
    'name' : 'mainmenu',
    'text' : [mainmenuText1,mainmenuText2],
    'image' : [],
    'button' : [mainmenuStartbutton,mainmenuSettingsbutton,mainmenuCatbutton],
}

settings = {
    'name': 'settings',
    'text' : [settingsText],
    'image' : [],
    'button' : [settingsButton,settingsBackbutton],
}

keybinds = {
    'name': 'keybinds',
    'text' : [],
    'image' : [],
    'button' : []
}

levels = {
    'name': 'levels',
    'text' : [],
    'image' : [],
    'button' : []
}

game = {
    'name': 'game',
    'text' : [],
    'image' : [],
    'button' : [],
}

catpage = {
    'name': 'catpage',
    'text' : [catText],
    'image' : [catImage],
    'button' : [catReturnbutton],
}

load(mainmenu,page)
global loadedpage
loadedpage = mainmenu
print(loadedpage)

def addresscheck(button):
    global loadedpage
    if button.address == 'mainmenu':
        loadedpage = mainmenu
        load(mainmenu, page)
        print(loadedpage)
    if button.address == 'settings':
        loadedpage = settings
        load(settings, page)
        print(loadedpage)
    if button.address == 'keybinds':
        loadedpage = keybinds
        load(keybinds,page)
        print(loadedpage)
    if button.address == 'levels':
        loadedpage = levels
        load(levels,page)
        print(loadedpage)
    if button.address == 'game':
        loadedpage = game
        load(game,page)
        print(loadedpage)
    if button.address == 'catpage':
        loadedpage = catpage
        load(catpage,page)
        print(loadedpage)

while True: # main game loop
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mouseposition = list(pygame.mouse.get_pos())
            for item in loadedpage['button']:
                print(loadedpage['button'])
                if mouseposition[0] >= item.x and mouseposition[0] <= (item.x + item.width) and mouseposition[1] >= item.y and mouseposition[1] <= (item.y + item.height):
                    addresscheck(item)
            print(mouseposition)
        pygame.display.update()
