import pygame,pygame_widgets, sys
from pygame.locals import *
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

buttonTexture =  pygame.image.load('button.jpg')                        #loads the different placeholder textures
cat = pygame.image.load('cat.png')
car = pygame.image.load('car.png')
stars = pygame.image.load('stars.jpeg')

pygame.init()                                                           #the different .init() functions needed
pygame.font.init()
pygame.display.init()

page = pygame.display.set_mode((1000, 700))                             #makes the main screen + gives it its main color
pygame.Surface.fill(page, (224,224,224))
pygame.display.set_caption('Aura Farm')

font = pygame.font.SysFont('Arial', 30)                     #loads the font

clock = pygame.time.Clock()                                             #starts the ingame clock and sets the game at 60 fps
clock.tick(60)

class Button:                                                           #button class to give it its different properties
    def __init__(self, x, y, width, height, address, image = pygame.image.load('button.jpg')):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.address = address

    def draw(self, screen):                                             #draw method to draw the button (duh)
        screen.blit(pygame.transform.scale(self.image,(self.width,self.height)), (self.x, self.y))
'''
playerTexture = None                                                    #for Théophile: insert players position here:
playerSize = ()
playerCoords = ()
gamePlayersprite = [playerTexture,playerCoords,playerSize]
'''
def load(pageinfo,screen):                                              #load function to draw the different images, texts, buttons and widgets on the screen
    pygame.Surface.fill(page,(224,224,224))
    for item in pageinfo['button']:
        item.draw(page)
    for item in pageinfo['text']:
        screen.blit(font.render(item[0],item[1],item[2]),item[3])
    for item in pageinfo['image']:
        screen.blit(pygame.transform.scale(item[0],(item[3],item[4])), (item[1], item[2]))
    if pageinfo['name'] == 'settings' or pageinfo['name'] == 'keybinds':
        pass

mainmenuText1 = ['main menu', True, (0,0,0),(0,0)]                      #all the different items that show up on all pages, saved as variables so the game page info is more readable
mainmenuText2 = ['aura farm industries present: yet another space attacks clone', True, (0,0,0),(0,550)]
mainmenuText3 = ['pretend this is the games logo', True, (0,0,0),(250,60)]
mainmenuStartbutton = Button(100,400,200,100,'levels',buttonTexture)
mainmenuSettingsbutton = Button(400,400,200,100,'settings',buttonTexture)
mainmenuCatimage = [car,250,100,400,200]
mainmenuText4 = ['start game', True, (0,0,0),(100,360)]
mainmenuText5 = ['settings', True, (0,0,0),(400,360)]

settingsKeybindsbutton = Button(200,500,200,100,'keybinds',buttonTexture)
settingsBackbutton = Button(600,500,200,100,'mainmenu',buttonTexture)
settingsText1 = ['settings', True, (0,0,0),(0,0)]
settingsText2 = ['keybinds', True, (0,0,0),(200,460)]
settingsText3 = ['return', True, (0,0,0),(600,460)]

keybindsReturnbutton = Button(600,500,200,100,'settings',buttonTexture)
keybindsReturntext = ['return', True, (0,0,0),(600,460)]


                                                                        #the game pages info given as a dict
mainmenu = {                                                            #the different items that show up are used as keys, and their associated value being a list containing the stuff that show up on said page
    'name' : 'mainmenu',
    'text' : [mainmenuText1,mainmenuText2,mainmenuText3,mainmenuText4,mainmenuText5],
    'image' : [mainmenuCatimage],
    'button' : [mainmenuStartbutton,mainmenuSettingsbutton],
    'widget' : [False]
}

settings = {
    'name': 'settings',
    'text' : [settingsText1,settingsText2,settingsText3],
    'image' : [],
    'button' : [settingsKeybindsbutton,settingsBackbutton],
    'widget': [True]
}

keybinds = {
    'name': 'keybinds',
    'text' : [keybindsReturntext],
    'image' : [],
    'button' : [keybindsReturnbutton],
    'widget': [True]
}

levels = {
    'name': 'levels',
    'text' : [],
    'image' : [],
    'button' : [],
    'widget': [False]
}

game = {
    'name': 'game',
    'text' : [],
    'image' : [stars],
    'button' : [],
    'widget': [False]
}
def addresscheck(button):                                               #function that checks the address of the button, and loads the page associated to said address
    global loadedpage
    if button.address == 'mainmenu':
        loadedpage = mainmenu
        load(mainmenu, page)
    if button.address == 'settings':
        loadedpage = settings
        load(settings, page)
    if button.address == 'keybinds':
        loadedpage = keybinds
        load(keybinds,page)
    if button.address == 'levels':
        loadedpage = levels
        load(levels,page)
    if button.address == 'game':
        loadedpage = game
        load(game,page)

load(mainmenu,page)                                                     #loads the main menu (duh)
global loadedpage
loadedpage = mainmenu

while True:                                                             # main game loop
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
#                                                                       For Noah: insert clicking sound here:
            mouseposition = list(pygame.mouse.get_pos())                #takes the coordinates of the mouse on click, then checks if said coordinates fall within any of the buttons loaded on the page, and finally checks the destination page
            for item in loadedpage['button']:
                if mouseposition[0] >= item.x and mouseposition[0] <= (item.x + item.width) and mouseposition[1] >= item.y and mouseposition[1] <= (item.y + item.height):
                    addresscheck(item)
            if loadedpage['widget'][0] == True:
                pygame_widgets.update(events)

        pygame.display.update()
