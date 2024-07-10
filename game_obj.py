import pygame

class GameObj:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, window, color):
        pygame.draw.rect(window, color, pygame.Rect(self.x, self.y, self.width, self.height))