import pygame
from grid import Grid

class Level:
    def __init__(self, screen, level: list|None = None):
        self.level = level
        self.screen = screen
        if level == None:
            grid = None
            tilemap = None
        self.grid = Grid(grid, tilemap) # Acceptable if False because Grid() defaults to dgrid

    def colliding(self, player: pygame.Rect):
        return self.grid.colliding(player)
    def draw(self):
        pass