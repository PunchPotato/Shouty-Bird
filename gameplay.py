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
        self.background_instance = Background()
        self.tubes_instance = Tubes(self.WIDTH, self.HEIGHT, 0)
        self.tubes_instance2 = Tubes(self.WIDTH, self.HEIGHT, 190)

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
            
            self.player.update()
            self.player.draw(self.screen)
           
            pygame.display.flip()

            pygame.time.Clock().tick(60)

        pygame.quit()
        sys.exit()

game = FlappyBird()
game.run_game()