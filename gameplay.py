import pygame
import sys
from player import Player
from audio import Audio
from background import Background
from tubes import Tubes

class FlappyBird:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.initialize_game()
        pygame.mixer.init()

    def initialize_game(self):
        self.WIDTH, self.HEIGHT = 320, 480
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.caption = pygame.display.set_caption("Flappy Bird with a twist")
        self.player = Player(self.WIDTH, self.HEIGHT)
        self.audio_instance = Audio()
        self.background_speed = 2
        self.background_instance = Background(self.background_speed)
        self.tube_speed = 2
        self.tubes_instance = Tubes(self.WIDTH, self.HEIGHT, 0, self.tube_speed)
        self.tubes_instance2 = Tubes(self.WIDTH, self.HEIGHT, 190, self.tube_speed)
        self.score = 0
        self.font = pygame.font.Font('assets/flappy-bird-font.ttf', 36)
        self.running = True
        self.point_audio = pygame.mixer.Sound('assets/point.wav')

    def restart_game(self):
        self.initialize_game()
        self.run_game()
    
    def run_game(self):
        pygame.init()

        self.audio_instance.capture_audio()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.background_instance.scrolling(self.screen)

            self.tubes_instance.update()
            self.tubes_instance.draw(self.screen)
            self.tubes_instance2.update()
            self.tubes_instance2.draw(self.screen)

            if self.tubes_instance.check_collision(self.player.rect, self.restart_game):
                return
            if self.tubes_instance2.check_collision(self.player.rect, self.restart_game):
                return

            if self.tubes_instance.check_if_passed(self.player):
                self.score += 1
                self.point_audio.play()
            if self.tubes_instance2.check_if_passed(self.player):
                self.score += 1
                self.point_audio.play()

            self.player.update()
            self.player.draw(self.screen)

            score_text = self.font.render(str(self.score), True, (0, 0, 0))
            self.screen.blit(score_text, (10, 10))

            pygame.display.flip()
            pygame.time.Clock().tick(60)

        pygame.quit()
        sys.exit()

game = FlappyBird()
game.run_game()