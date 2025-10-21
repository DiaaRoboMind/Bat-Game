import pygame

class static:
    def __init__(self):
        self.Lifes = 3
        self.Score = 0
        self.Life = pygame.image.load("image/Life.png")
        self.Life = pygame.transform.scale(self.Life, (50, 50))
        self.last_swap = pygame.time.get_ticks()
        self.over1 = pygame.transform.scale(pygame.image.load("image/Life.png"), (220, 220))
        self.over2 = pygame.transform.scale(pygame.image.load("image/LifeSmail.png"), (220, 220))
        self.Over = self.over1
        self.GameOver=pygame.image.load("image/Gameover.png")
        self.Again=pygame.image.load("image/Play Again.png")
        self.Again=pygame.transform.scale(self.Again,(150,150))
        self.Again_rect=self.Again.get_rect(topleft=(1200,600))




    def life_draw(self, screen):
        if self.Lifes >= 1:
            screen.blit(self.Life, (40, 30))
        if self.Lifes >= 2:
            screen.blit(self.Life, (100, 30))
        if self.Lifes >= 3:
            screen.blit(self.Life, (160, 30))

    def Game_over(self, screen):

        now = pygame.time.get_ticks()
        if now - self.last_swap >= 1000:
            self.last_swap = now
            self.Over = self.over2 if self.Over == self.over1 else self.over1
        self.font = pygame.font.Font(None, 48) 
        text = self.font.render(f"Score : {self.Score}", True, (255, 255, 255)) 
        screen.blit(self.GameOver,(160,50))  
        screen.blit(text, (600,700))
        screen.blit(self.Over, (570, 190))
        screen.blit(self.Again,(1200,600))