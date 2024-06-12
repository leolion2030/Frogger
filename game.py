import pygame

class Game:

    def __init__(self):
        self.window = pygame.display.set_mode((1000, 800))
        self.main_game_loop()
        
    def main_game_loop(self):
        while True:
            self.event_handler()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()