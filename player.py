import pygame
from audio import Audio
from audio import audio_instance

class Player(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT) -> None:
        pygame.sprite.Sprite.__init__
        self.bird_up_flap_img = pygame.image.load('assets/redbird-upflap.png')
        self.bird_mid_flap_img = pygame.image.load('assets/redbird-midflap.png')
        self.bird_down_flap_img = pygame.image.load('assets/redbird-downflap.png')
        self.bird_up_flap_rect = self.bird_up_flap_img.get_rect()
        self.bird_mid_flap_rect = self.bird_mid_flap_img.get_rect()
        self.bird_down_flap_rect = self.bird_down_flap_img.get_rect()
        self.pos = (WIDTH // 2, HEIGHT // 2)
        self.audio_instance = Audio()
        self.gravity = 3
        self.sprite_sheet = [(self.bird_down_flap_img, self.bird_down_flap_rect),
                             (self.bird_mid_flap_img, self.bird_mid_flap_rect),
                             (self.bird_up_flap_img, self.bird_up_flap_rect)]
        self.frame_index = 0 
        self.flying = False

    def draw(self, screen):
        self.bird_up_flap_rect.center = self.pos
        screen.blit(self.sprite_sheet[self.frame_index][0], self.pos)

    def update(self):
        amplitude = audio_instance.latest_amplitude
        if amplitude <= audio_instance.quiet_threshold:
            self.flying = False
        elif audio_instance.quiet_threshold < amplitude <= audio_instance.moderate_threshold:
           self.pos = (self.pos[0], self.pos[1] - 7)
           self.flying = True
        else:
            self.pos = (self.pos[0], self.pos[1] - 10)
            self.flying = True

        self.pos = (self.pos[0], self.pos[1] + self.gravity)

        if self.flying:
           self.frame_index = (self.frame_index + 1) % len(self.sprite_sheet)
           print(self.frame_index)