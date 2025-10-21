import pygame
from Settings import setting
class Bat:
    def __init__(self,screen):
        self.screen =screen
        self.Bat=pygame.image.load("image/Bat.png")
        self.Sad1=pygame.image.load("image/Sad Bat.png")
        self.Sad2=pygame.image.load("image/Sad 2.png")
        self.Sad3=pygame.image.load("image/die bat.png")
        self.Bat=pygame.transform.scale(self.Bat,(100,100))
        self.Sad1=pygame.transform.scale(self.Sad1,(100,100))
        self.Sad2=pygame.transform.scale(self.Sad2,(100,100))
        self.Sad3=pygame.transform.scale(self.Sad3,(100,100))
        self.Bat_rect=self.Bat.get_rect()
        self.screen_rect=self.screen.get_rect()
        self.Bat_rect.centerx=200
        self.Bat_rect.bottom=200
        self.Bat_down=False
        self.Bat_up=False
        self.Bat_G=True
        self.Bat_right=False
        self.Bat_left=False
        self.sad_level=0


    def Moving(self,setting):
        if self.Bat_G and self.Bat_rect.bottom<=self.screen_rect.bottom :
            self.Bat_rect.bottom+=setting.Gravity
        if self.Bat_down and self.Bat_rect.bottom<=self.screen_rect.bottom:
             self.Bat_rect.bottom+=setting.Gravity
        if self.Bat_up and self.Bat_rect.top>=0:
            self.Bat_rect.bottom-=setting.Jump
        if self.Bat_right and self.Bat_rect.right <= setting.W/2-300 :
            self.Bat_rect.centerx+=5
        if self.Bat_left and self.Bat_rect.left >=0 :
            self.Bat_rect.centerx-=5
    def reset_position(self):
     self.Bat_rect.centerx = 200
     self.Bat_rect.bottom = 300
     self.sad_level = 0
     self.Bat_up = False
     self.Bat_down = False
     self.Bat_right = False
     self.Bat_left = False
     self.Bat_G = True
    def draw(self):
        if self.sad_level==1 : 
            self.screen.blit(self.Sad1,self.Bat_rect)
        elif self.sad_level==2:
            self.screen.blit(self.Sad2,self.Bat_rect)
        
        elif self.sad_level==3:
            self.screen.blit(self.Sad3,self.Bat_rect)
        else: 
         self.screen.blit(self.Bat,self.Bat_rect)