import pygame
import random

class Tubes:
    def __init__(self, screen_width, screen_height, x_offset, tube_speed):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.tube_img = pygame.image.load('assets/pipe-green.png')
        self.rect = self.tube_img.get_rect()
        self.gap = 150
        self.tube_speed = tube_speed
        self.x_offset = x_offset
        self.first_reset = True
        self.passed = False
        self.rect_top = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        self.rect_bottom = pygame.Rect(self.rect.x, self.rect.y + self.gap + self.rect.height, self.rect.width, self.rect.height)
        self.reset()
        self.hit_audio = pygame.mixer.Sound('assets/hit.wav')

    def reset(self):
        if self.first_reset:
            self.rect.x = self.screen_width + self.x_offset
            self.first_reset = False
        else:
            self.rect.x = self.screen_width
        self.rect.y = random.randint(-300, 0)
        self.bottom_tube_y = self.rect.y + self.tube_img.get_height() + self.gap
        
        self.rect_top.y = self.rect.y
        self.rect_top.x = self.rect.x
        self.rect_bottom.y = self.bottom_tube_y
        self.rect_bottom.x = self.rect.x

        self.passed = False

    def check_if_passed(self, player):
        if player.rect.x > self.rect.x + self.rect.width and not self.passed:
            self.passed = True
            return True
        return False

    def update(self):
        self.rect.x -= self.tube_speed
        
        self.rect_top.x = self.rect.x
        self.rect_bottom.x = self.rect.x
        
        if self.rect.right < 0:
            self.reset()
            
    def draw(self, screen):
        top_tube_rect = self.rect.copy()
        top_tube_rect.height -= self.gap
        screen.blit(pygame.transform.flip(self.tube_img, False, True), top_tube_rect)

        bottom_tube_rect = self.rect.copy()
        bottom_tube_rect.y = self.bottom_tube_y
        screen.blit(self.tube_img, bottom_tube_rect)

    def check_collision(self, player_rect, restart_game):
        if self.rect_top.colliderect(player_rect):
            self.hit_audio.play()
            restart_game()
            return True
        
        if self.rect_bottom.colliderect(player_rect):
            self.hit_audio.play()
            restart_game()
            return True
        
        return False