import pygame

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1000, 800))
        self.main_game_loop()
        
    def main_game_loop(self):
        while True: 
            self.event_handler()
            self.draw()
            
    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
    def draw(self):
        pygame.draw.rect(self.window, (0, 255, 0), pygame.Rect(500, 400, 20, 20))
        pygame.display.update()