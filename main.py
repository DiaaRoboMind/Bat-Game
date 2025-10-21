#DiaaRoboMind
import pygame
from Settings import setting
import functions
from Bat import Bat
from ObstaclesTop import Obstacles
from pygame import sprite
from static import static
def Run():

    pygame.init()
    pygame.mixer.init()
    screen_settings=setting()
    screen=pygame.display.set_mode((screen_settings.W,screen_settings.H))
    pygame.display.set_caption("Cave Bat ")
    pygame.display.set_icon(screen_settings.Icon)
    bat=Bat(screen)
    Ob=pygame.sprite.Group()
    O=Obstacles(screen,screen_settings)
    S=static()
    Ob.add(O)
    while True:
        functions.event(screen,bat,S)
        functions.Screen_up(screen_settings,screen,bat,O,Ob,S)
        bat.Moving(screen_settings)
Run()