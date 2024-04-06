import pygame
import random

class Tubes():
    def __init__(self, screen_width, screen_height, x_offset) -> None:
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.tube_img = pygame.image.load('assets/pipe-green.png')
        self.tube_rect = self.tube_img.get_rect()
        self.gap = 150
        self.tube_speed = 2
        self.x_offset = x_offset
        self.reset()

    def reset(self):
        self.tube_rect.x = self.screen_width + self.x_offset
        self.tube_rect.y = random.randint(-300, 0)
        self.bottom_tube_y = self.tube_rect.y + self.tube_img.get_height() + self.gap

    def update(self):
        self.tube_rect.x -= self.tube_speed
        if self.tube_rect.right < 0:
            self.reset()

    def draw(self, screen):
        top_tube_rect = self.tube_rect.copy()
        top_tube_rect.height -= self.gap
        screen.blit(pygame.transform.flip(self.tube_img, False, True), top_tube_rect)

        bottom_tube_rect = self.tube_rect.copy()
        bottom_tube_rect.y = self.bottom_tube_y
        screen.blit(self.tube_img, bottom_tube_rect)
