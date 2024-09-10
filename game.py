import pygame
import random
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

        self.raft1 = GameObj(0, 400, 160, 40,)
        self.raft2 = GameObj(0, 360, 160, 40,)
        self.raft3 = GameObj(0, 320, 160, 40,)

        self.random_x = random.randint(0, 980)
        self.random_y = random.randint(0, 780)
        self.fly = GameObj(self.random_x, self.random_y, 40, 40)

        self.starting_point = GameObj(0, 760, 1000, 40)
        self.road = GameObj(0, 560, 1000, 200)
        self.safe = GameObj(0, 520, 1000, 40)
        self.water = GameObj(0, 320, 1000, 200)

        self.checkpoint1 = GameObj(40, 240, 80, 80)
        self.checkpoint2 = GameObj(240, 240, 80, 80)
        self.checkpoint3 = GameObj(440, 240, 80, 80)
        self.checkpoint4 = GameObj(640, 240, 80, 80)
        self.checkpoint5 = GameObj(840, 240, 80, 80)

        self.lock_chkpoint = []

        self.background_behind = GameObj(0, 0, 1000, 800)
        self.player_speed = 40
        self.score = 0
        self.has_fly = 0
        self.limit_chk1 = 0
        self.limit_chk2 = 0
        self.limit_chk3 = 0
        self.limit_chk4 = 0
        self.limit_chk5 = 0
        self.raft_speed = 5
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
                    self.player.y -= self.player_speed
                if event.key == pygame.K_s:
                    self.player.y += self.player_speed
                if event.key == pygame.K_a:
                    self.player.x -= self.player_speed
                if event.key == pygame.K_d:
                    self.player.x += self.player_speed

    def draw(self):
        self.background_behind.draw(self.window, (0, 0, 0))
        self.starting_point.draw(self.window, (255, 255, 0))
        self.road.draw(self.window,(0, 0, 0))
        self.safe.draw(self.window, (255, 255, 0))
        self.water.draw(self.window, (0, 0, 255))
        self.game_obj.draw(self.window, (0, 255, 0))
        self.checkpoint1.draw(self.window, (0, 255, 0))
        self.checkpoint2.draw(self.window, (0, 255, 0))
        self.checkpoint3.draw(self.window, (0, 255, 0))
        self.checkpoint4.draw(self.window, (0, 255, 0))
        self.checkpoint5.draw(self.window, (0, 255, 0))
        self.fly_display()
        self.car.draw(self.window, (255, 0, 0))

        self.raft1.draw(self.window, (255, 0 ,255))
        self.raft2.draw(self.window, (255, 0 ,255))
        self.raft3.draw(self.window, (255, 0 ,255))

        self.fly.draw(self.window, (0, 0, 100))
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
        self.raft1.x += self.raft_speed
        self.raft2.x -= self.raft_speed
        self.raft3.x += self.raft_speed
        if self.car.x >= 1000:
            self.car.x = 0 - self.car.width
        if self.raft1.x >= 1000 or self.raft3.x >= 1000:
            self.raft1.x = 0 - self.raft1.width
            self.raft3.x = 0 - self.raft3.width
        if self.raft2.x < -1:
            self.raft2.x = 1000

    def collide(self):
        if self.player.get_hitbox().colliderect(self.car.get_hitbox()) == True:
            print("Your Dead Car")
            self.player.x = 500
            self.player.y = 760

        if self.player.get_hitbox().colliderect(self.raft1.get_hitbox()) == True:
            self.player.x += self.raft_speed
        if self.player.get_hitbox().colliderect(self.raft2.get_hitbox()) == True:
            self.player.x -= self.raft_speed
        if self.player.get_hitbox().colliderect(self.raft3.get_hitbox()) == True:
            self.player.x += self.raft_speed

        if self.player.get_hitbox().colliderect(self.water.get_hitbox()) == True:
            if self.player.get_hitbox().colliderect(self.raft1.get_hitbox()) != True and self.player.get_hitbox().colliderect(self.raft2.get_hitbox()) != True and self.player.get_hitbox().colliderect(self.raft3.get_hitbox()) != True:
                print("Your Dead Water")
        if self.player.get_hitbox().colliderect(self.fly.get_hitbox()) == True:
            if self.fly.x >= 1000:
                    self.fly.x = random.randint(0, 980)
                    self.fly.y = random.randint(0, 780)
            self.fly.x = random.randint(0, 980)
            self.fly.y = random.randint(0, 780)
            self.has_fly += 1
            if self.fly.x == self.raft1.x or self.raft2.x or self.raft3.x and self.fly.y == self.raft1.y:
                self.fly.x += self.raft_speed
        if self.player.get_hitbox().colliderect(self.checkpoint1.get_hitbox()) == True and self.has_fly >= 1:
            if self.limit_chk1 == 0: 
                if self.has_fly >= 1:
                    self.score += 1
                    self.has_fly -= 1
                    print("Score: " , self.score)
                    self.limit_chk1 += 1
                    self.lock_chkpoint.append("chkpnt1")
        if self.player.get_hitbox().colliderect(self.checkpoint2.get_hitbox()) == True and self.has_fly >= 1:
            if self.limit_chk2 == 0: 
                if self.has_fly >= 1:    
                    self.score += 1
                    self.has_fly -= 1
                    print("Score: " , self.score)
                    self.limit_chk2 += 1
                    self.lock_chkpoint.append("chkpnt2")
        if self.player.get_hitbox().colliderect(self.checkpoint3.get_hitbox()) == True and self.has_fly >= 1:
            if self.limit_chk3 == 0:
                if self.has_fly >= 1:     
                    self.score += 1
                    self.has_fly -= 1
                    print("Score: " , self.score)
                    self.limit_chk3 += 1
                    self.lock_chkpoint.append("chkpnt3")
        if self.player.get_hitbox().colliderect(self.checkpoint4.get_hitbox()) == True and self.has_fly >= 1:
            if self.limit_chk4 == 0:
                if self.has_fly >= 1:
                    self.score += 1
                    self.has_fly -= 1
                    print("Score: " , self.score)
                    self.limit_chk4 += 1
                    self.lock_chkpoint.append("chkpnt4")
        if self.player.get_hitbox().colliderect(self.checkpoint5.get_hitbox()) == True and self.has_fly >= 1:
            if self.limit_chk5 == 0:     
                if self.has_fly >= 1:
                    self.score += 1
                    self.has_fly -= 1
                    print("Score: " , self.score)
                    self.limit_chk5 += 1
                    self.lock_chkpoint.append("chkpnt5")

    def fly_display(self):
        if "chkpnt1" in self.lock_chkpoint:
            self.fly_complete = GameObj(self.checkpoint1.x, self.checkpoint1.y, 40, 40)
            self.fly_complete.draw(self.window, (0, 0, 100))
        if "chkpnt2" in self.lock_chkpoint:
            self.fly_complete = GameObj(self.checkpoint2.x, self.checkpoint2.y, 40, 40)
            self.fly_complete.draw(self.window, (0, 0, 100))
        if "chkpnt3" in self.lock_chkpoint:
            self.fly_complete = GameObj(self.checkpoint3.x, self.checkpoint3.y, 40, 40)
            self.fly_complete.draw(self.window, (0, 0, 100))
        if "chkpnt4" in self.lock_chkpoint:
            self.fly_complete = GameObj(self.checkpoint4.x, self.checkpoint4.y, 40, 40)
            self.fly_complete.draw(self.window, (0, 0, 100))
        if "chkpnt5" in self.lock_chkpoint:
            self.fly_complete = GameObj(self.checkpoint5.x, self.checkpoint5.y, 40, 40)
            self.fly_complete.draw(self.window, (0, 0, 100))
        