import pygame
from game_obj import GameObj

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1000, 800))
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.game_obj = GameObj(0, 0, 50 ,50)
        self.player = GameObj(500, 760, 40, 40)
        self.car = GameObj(0, 600, 160, 40)
        self.raft = GameObj(0, 400, 160, 40,)
        self.starting_point = GameObj(0, 760, 1000, 40)
        self.road = GameObj(0, 560, 1000, 200)
        self.safe = GameObj(0, 520, 1000, 40)
        self.water = GameObj(0, 320, 1000, 200)
        self.main_game_loop()
        
    def main_game_loop(self):
        while True: 
            self.clock.tick(self.fps)
            self.event_handler()
            self.key_handler()
            self.move()
            self.collide()
            self.draw()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player.y -= 40
                if event.key == pygame.K_s:
                    self.player.y += 40
                if event.key == pygame.K_a:
                    self.player.x -= 40
                if event.key == pygame.K_d:
                    self.player.x += 40

    def draw(self):
        self.starting_point.draw(self.window, (255, 255, 0))
        self.road.draw(self.window,(0, 0, 0))
        self.safe.draw(self.window, (255, 255, 0))
        self.water.draw(self.window, (0, 0, 255))
        self.game_obj.draw(self.window, (0, 255, 0))
        self.car.draw(self.window, (255, 0, 0))
        self.raft.draw(self.window, (255, 0 ,255))
        self.player.draw(self.window, (0, 255, 0))
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

    def move(self):
        self.car.x += 10
        self.raft.x += 10
        if self.car.x >= 1000:
            self.car.x = 0 - self.raft.width
        if self.raft.x >= 1000:
            self.raft.x = 0 - self.raft.width

    def collide(self):
        if pygame.Rect.colliderect(self.player, self.car):
            print("hi")