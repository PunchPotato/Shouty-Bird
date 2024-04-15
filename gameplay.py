import pygame
import sys
from player import Player
from audio import Audio
from background import Background
from tubes import Tubes

class FlappyBird():
    def __init__(self) -> None:
        self.WIDTH, self.HEIGHT = 320, 480
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.caption = pygame.display.set_caption("Flappy Bird with a twist")
        self.player = Player( self.WIDTH, self.HEIGHT)
        self.audio_instance = Audio()
        self.background_speed = 2
        self.background_instance = Background(self.background_speed)
        self.tube_speed = 2
        self.tubes_instance = Tubes(self.WIDTH, self.HEIGHT, 0, self.tube_speed)
        self.tubes_instance2 = Tubes(self.WIDTH, self.HEIGHT, 190, self.tube_speed)

    def start_screen(self):
        pass

    def end_screen(self):
        pass

    def run_game(self):
        pygame.init()

        self.audio_instance.capture_audio()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.background_instance.scrolling(self.screen)

            self.tubes_instance.update()
            self.tubes_instance.draw(self.screen)
            self.tubes_instance2.update()
            self.tubes_instance2.draw(self.screen)
            
            pygame.draw.rect(self.screen, (255, 0, 0), self.player.rect, 2) # Red rectangle around player
            pygame.draw.rect(self.screen, (0, 255, 0), self.tubes_instance.rect, 2)  # Green rectangle around first pipe
            pygame.draw.rect(self.screen, (255, 255, 0), self.tubes_instance2.rect, 2)

            self.player.update()
            self.player.draw(self.screen)
            self.player.collision([self.tubes_instance, self.tubes_instance2], self.tube_speed, self.background_speed)
           
            pygame.display.flip()

            pygame.time.Clock().tick(60)

        pygame.quit()
        sys.exit()

game = FlappyBird()
game.run_game()