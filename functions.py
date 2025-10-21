import pygame
import sys # it is use to exit from the game and so on ...
Back=None
Start=pygame.image.load("image/StartB.png")
rect_Start = Start.get_rect(topleft=(480, 500))

Back_Start=pygame.image.load("image/Start.png")
Back_Start=pygame.transform.scale(Back_Start,(1400,800))
start=False
def event(screen, bat,Static):
    global start
    for Click in pygame.event.get():
        if Click.type == pygame.QUIT:
            sys.exit()
        if Click.type == pygame.MOUSEBUTTONDOWN:
            if rect_Start.collidepoint(Click.pos):
              # print("Start ")
               start=True
               
        if Click.type == pygame.MOUSEBUTTONDOWN:
         if Static.Again_rect.collidepoint(Click.pos):
               
               Static.Lifes=3
               Static.Score = 0
               bat.reset_position()
               start =True
        if Click.type == pygame.KEYDOWN:
            if Click.key==pygame.K_RETURN :
               Static.Lifes=3
               Static.Score = 0
               bat.reset_position()
               start =True
            if Click.key==pygame.K_SPACE:
               start=True
            if Click.key == pygame.K_UP:
                bat.Bat_up = True
                bat.Bat_G = False
            elif Click.key == pygame.K_DOWN:
                bat.Bat_down = True
                bat.Bat_G = False
            if Click.key==pygame.K_RIGHT:
                bat.Bat_right=True
            elif Click.key==pygame.K_LEFT:
                bat.Bat_left=True
        elif Click.type == pygame.KEYUP:
            if Click.key == pygame.K_UP:
                bat.Bat_up = False
                bat.Bat_G = True
            elif Click.key == pygame.K_DOWN:
                bat.Bat_down = False
                bat.Bat_G = True
            elif Click.key==pygame.K_RIGHT:
                bat.Bat_right=False
            elif Click.key==pygame.K_LEFT:
                bat.Bat_left=False
def Screen_up(screen_settings,screen,bat,ob,Ob,Static):
    
    if not start:
        bat.reset_position()
        screen_settings.Start_Sound.play()
        screen.blit(Back_Start,(0,0))
        screen.blit(Start,(480,500))
    elif start and Static.Lifes>0:
     global Back
     screen_settings.Start_Sound.stop()
     screen_settings.Back_Sound.play()
     if Back == None:
      Back=pygame.image.load("image/Night Back.png")
      Back=pygame.transform.scale(Back , (screen_settings.W,screen_settings.H))
     
     screen.blit(Back,(0,0))
     screen_settings.Back_X-=screen_settings.BackG_Moving
     if screen_settings.Back_X <=-screen_settings.W:
        screen_settings.Back_X=0

     screen.blit(Back, (screen_settings.Back_X, 0))
     screen.blit(Back, (screen_settings.Back_X + screen_settings.W, 0))
     
    
     for ob in Ob:
      ob.Mov(Ob,Static)
      ob.draw()
      if ob.G(bat):
         screen_settings.Back_Sound.stop()
         screen_settings.damage.play()
         bat.sad_level=3
         Static.Lifes=0
      if ob.Check(bat) :
         screen_settings.Back_Sound.stop()
         screen_settings.damage.play()
         bat.sad_level+=1
         Static.Lifes-=1
         Ob.remove(ob)
     Static.life_draw(screen)
     bat.draw()
    
    else:
       
       screen_settings.Back_Sound.stop()
       screen_settings.Start_Sound.play()
       Static.Game_over(screen)
    pygame.display.flip() 
