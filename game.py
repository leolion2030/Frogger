import pygame
from game_obj import GameObj

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1000, 800))
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.game_obj = GameObj(0, 0, 50 ,50)
        self.player = GameObj(500, 500, 20, 20)
        self.car = GameObj(0, 400, 60, 20 )
        self.main_game_loop()
        
    def main_game_loop(self):
        while True: 
            self.clock.tick(self.fps)
            self.event_handler()
            self.key_handler()
            self.car_move()
            self.draw()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player.y -= 20
                if event.key == pygame.K_s:
                    self.player.y += 20
                if event.key == pygame.K_a:
                    self.player.x -= 20
                if event.key == pygame.K_d:
                    self.player.x += 20

    def draw(self):
        self.game_obj.draw(self.window)
        self.player.draw(self.window)
        self.car.draw(self.window)
        pygame.display.update()

    def key_handler(self):
        return
        wait = pygame.time.get_ticks()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w] == True:
            self.player.y -= 5
            if wait >= 2000:
                pass
        elif pressed_keys[pygame.K_s] == True:
            self.player.y += 5
        elif pressed_keys[pygame.K_a] == True:
            self.player.x -= 5
        elif pressed_keys[pygame.K_d] == True:
            self.player.x += 5

    def car_move(self):
        self.car.x += 10