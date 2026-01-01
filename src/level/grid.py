import pygame
from utils.const import dgrid
import tilemanager as tile

# Grid structure:
# Tuple[x, y, Tuple[]]

class Grid:
    def __init__(self, grid: list|None = dgrid, tilemap: list|None = None):
        if grid == None:
            grid = dgrid
        # Assume it's a correct grid, never check except usng asserts
        # Asserts only trigger if incorrect grid given, if this triggers, something's wrong
        assert len(grid) == 3
        assert isinstance(grid[0], int) and isinstance(grid[1], int)
        assert isinstance(grid[2], list) and len(grid[2]) == (grid[0] * grid[1]) and all(isinstance(x, int) for x in grid[2])
        self.length, self.height = grid[0], grid[1]
        self.grid = grid[2]
        self.coords = self.cache_world_coords()
        self.tilemap = (False,)
        assert self.tilemap[0] == False
        assert all(self.grid[x] in tilemap for x in self.grid)
        
    def update_tile_surf(self, idx: int):
        tile_surf = pygame.Surface((32, 32))
        for i in range(64):
            x = (i % 8) * 8
            y = (idx // 8) * 8
            pygame.draw.rect(tile_surf, self.grid[i], (x, y, 8, 8))
        return tile_surf
    def get_world_coords(self, idx):
        return (idx % self.length) * 32, (idx // self.height) * 32
    def get_index(self, x, y):
        return (y // 32) * self.length + (x // 32)
    def cache_world_coords(self):
        # Cache coords so don't have to recalculate every render
        self.coords = []
        for i in range(len(self.grid)):
            self.coords.append(self.get_world_coords(i))
        self.coords = tuple(self.coords) # Fast lookup
    def colliding(self, player):
        return tile.colliding(self.tilemap, self.grid, player, self.get_index)