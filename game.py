import pygame
from game_obj import GameObj

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1000, 800))
        self.game_obj = GameObj()
        self.main_game_loop()
        
    def main_game_loop(self):
        while True: 
            self.event_handler()
            self.game_obj.draw()
            self.draw()
            
    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()