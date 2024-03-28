import pygame
from audio import Audio
from audio import audio_instance

class Player():
    def __init__(self, WIDTH, HEIGHT) -> None:
        self.bird_up_flap_img = pygame.image.load('assets/redbird-upflap.png')
        self.bird_mid_flap_img = pygame.image.load('assets/redbird-midflap.png')
        self.bird_down_flap_img = pygame.image.load('assets/redbird-downflap.png')
        self.bird_up_flap_rect = self.bird_up_flap_img.get_rect()
        self.bird_mid_flap_rect = self.bird_mid_flap_img.get_rect()
        self.bird_down_flap_rect = self.bird_down_flap_img.get_rect()
        self.pos = (WIDTH // 2, HEIGHT // 2)
        self.audio_instance = Audio()

    def draw_sprite(self, screen):
        self.bird_up_flap_rect.center = self.pos
        screen.blit(self.bird_up_flap_img, self.bird_up_flap_rect)

    def player_movement(self):
        amplitude = audio_instance.latest_amplitude
        if amplitude <= audio_instance.quiet_threshold:
            pass
        elif audio_instance.quiet_threshold < amplitude <= audio_instance.moderate_threshold:
           self.pos = (self.pos[0], self.pos[1] - 1)
        else:
            self.pos = (self.pos[0], self.pos[1] - 5)