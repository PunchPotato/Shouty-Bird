import pygame
from audio import Audio
from audio import audio_instance

class Player(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.bird_up_flap_img = pygame.image.load('assets/redbird-upflap.png')
        self.bird_mid_flap_img = pygame.image.load('assets/redbird-midflap.png')
        self.bird_down_flap_img = pygame.image.load('assets/redbird-downflap.png')
        
        self.rotated_bird_up_flap = pygame.transform.rotate(self.bird_up_flap_img, 30)
        self.rotated_bird_mid_flap = pygame.transform.rotate(self.bird_mid_flap_img, 30)
        self.rotated_bird_down_flap = pygame.transform.rotate(self.bird_down_flap_img, 30)
        self.rotated_sprite_sheet = [
            (self.rotated_bird_down_flap, self.rotated_bird_down_flap.get_rect()),
            (self.rotated_bird_mid_flap, self.rotated_bird_mid_flap.get_rect()),
            (self.rotated_bird_up_flap, self.rotated_bird_up_flap.get_rect())
        ]

        self.rotated2_bird_up_flap = pygame.transform.rotate(self.bird_up_flap_img, -40)
        self.rotated2_sprite_sheet = [
            (self.rotated2_bird_up_flap, self.rotated2_bird_up_flap.get_rect())
        ]

        self.pos = (WIDTH // 2, HEIGHT // 2)
        self.rect = self.rotated_sprite_sheet[0][1]
        self.audio_instance = Audio()
        self.gravity = 4
        self.frame_index = 0 
        self.flying = False
        self.wing_audio = pygame.mixer.Sound('assets/wing.wav')

    def draw(self, screen):
        if self.flying:
            self.sprite = screen.blit(self.rotated_sprite_sheet[self.frame_index][0], self.pos)
        else:
            self.sprite = screen.blit(self.rotated2_sprite_sheet[self.frame_index][0], self.pos)

    def update(self):
        amplitude = audio_instance.latest_amplitude
        if amplitude <= audio_instance.quiet_threshold:
            self.flying = False
        elif audio_instance.quiet_threshold < amplitude <= audio_instance.moderate_threshold:
            self.pos = (self.pos[0], self.pos[1] - 7)
            self.flying = True
            self.wing_audio.play()
        else:
            self.pos = (self.pos[0], self.pos[1] - 10)
            self.flying = True
            self.wing_audio.play()

        self.pos = (self.pos[0], self.pos[1] + self.gravity)
        self.rect.topleft = self.pos

        if self.flying:
            self.frame_index = (self.frame_index + 1) % len(self.rotated_sprite_sheet)
        else:
            self.frame_index = (self.frame_index + 1) % len(self.rotated2_sprite_sheet)

        