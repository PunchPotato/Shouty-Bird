import pygame 

class Background():
    def __init__(self) -> None:
        self.background = pygame.image.load('assets/background-day.png')
        self.background_speed = 2
        self.pos_x = 0

    def scrolling(self, screen):
        self.pos_x -= self.background_speed
        if self.pos_x <= -self.background.get_width():
            self.pos_x = 0

        screen.blit(self.background, (self.pos_x, 0))
        screen.blit(self.background, (self.pos_x + self.background.get_width(), 0))