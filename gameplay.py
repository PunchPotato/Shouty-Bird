import pygame
import sys
from player import Player
from audio import Audio

class FlappyBird():
    def __init__(self) -> None:
        self.WIDTH, self.HEIGHT = 320, 480
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.caption = pygame.display.set_caption("Flappy Bird with a twist")
        self.player = Player( self.WIDTH, self.HEIGHT)
        self.audio_instance = Audio()

    def background(self):
        pass

    def start_screen(self):
        pass

    def end_screen(self):
        pass

    def run_game(self):
        pygame.init()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill('white')
            
            self.player.player_movement()
            self.player.draw_sprite(self.screen)
           
            pygame.display.flip()

            pygame.time.Clock().tick(60)

        pygame.quit()
        sys.exit()

game = FlappyBird()
game.run_game()