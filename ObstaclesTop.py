import pygame
import random
class Obstacles(pygame.sprite.Sprite):
    def __init__(self,screen,screen_setting):
        super().__init__()   
        self.genrated=False
        self.screen=screen
        self.screen_settings=screen_setting
        self.image=pygame.image.load("image/Glowing_Crystals_in_Stalagmite_Formation-removebg-preview.png")#to top
       
        self.image=pygame.transform.scale(self.image,(100,500))
        self.Top_image=pygame.transform.flip(self.image , False,True)
        self.rect=self.image.get_rect()
        self.rect_Top = self.Top_image.get_rect()
        self.height = random.randint(-400,-10)
        self.rect.topleft = (screen_setting.W, self.height)
        self.rect_Top.topleft=(self.screen_settings.W,self.height+self.screen_settings.Gap)
        self.speed = screen_setting.BackG_Moving
        self.genrated=True
        
    def Mov(self,G_Ob,Static):
        self.rect.x -= self.speed
        self.rect_Top.x-=self.speed
        if self.genrated and self.rect.x<(self.screen_settings.W/2-200):
           new_Ob=Obstacles(self.screen,self.screen_settings)
           G_Ob.add(new_Ob)
           self.genrated=False
        if self.rect.x<-200:
           G_Ob.remove(self)
           Static.Score+=1
           
    def Check(self,Bat):
        return self.rect.colliderect(Bat.Bat_rect) or self.rect_Top.colliderect(Bat.Bat_rect) 
    def G(self,Bat):
        return self.screen_settings.H==Bat.Bat_rect.bottom

    def draw(self):
        self.screen.blit(self.image,self.rect)
        self.screen.blit(self.Top_image,self.rect_Top)

    
