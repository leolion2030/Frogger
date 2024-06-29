import pygame
from game_obj import GameObj

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1000, 800))
        self.game_obj = GameObj(0, 0, 50 ,50)
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
        self.game_obj.draw(self.window)
        pygame.display.update()

    def key_handler(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w] == True:
            self.player.y -= self.player.speed
        elif pressed_keys[pygame.K_s] == True:
            self.player.y += self.player.speed
        elif pressed_keys[pygame.K_a] == True:
            self.player.x -= self.player.speed
        elif pressed_keys[pygame.K_d] == True:
            self.player.x += self.player.speed