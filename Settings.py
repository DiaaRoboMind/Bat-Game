import pygame
class setting():
    def __init__(self):
        self.W=1400 
        self.H=800 
        self.Icon=pygame.image.load("image/Icon.png")
        self.Gravity=1
        self.Jump=2
        self.BackG_Moving =4
        self.Back_X=0
        self.Gap=800
        self.Ob_Space=5

        self.Start_Sound=pygame.mixer.Sound("Sound/MEGALOVANIA.mp3")
        self.Start_Sound.set_volume(0.1)
        self.Back_Sound=pygame.mixer.Sound("Sound/Undertale OST_ 009 - Enemy Approaching.mp3")
        self.Back_Sound.set_volume(0.05)
        self.damage=pygame.mixer.Sound("Sound/Arcade Retro Game Over - Sound Effect (Final Cut) (mp3cut.net).mp3")
        self.damage.set_volume(0.7)
        