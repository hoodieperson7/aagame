import pygame

# Tile structure:
# RGB : Tuple[int, int, int]
# solid: bool

# Tuple[RGB * 64, solid * 64]

# Tilemap structure:
# List of indexes
# tilemap[0] = tile, etc

def get_tile_surf(tile: list):
    tile_surf = pygame.Surface((64, 64))
    for i in range(32):
        # tile world pos (no world pos offset)
        x = i // 8
        y = i % 8
        x *= 8
        y *= 8
        sp = pygame.Rect(x, y, 8, 8)
        pygame.draw.rect(tile_surf, tile[0][i], sp)
    return tile_surf

def colliding(tilemap, grid: list, obj: pygame.Rect, get_index):
    tile_pos = set()
    for i in range(4):
        corners = [obj.topleft, obj.topright, obj.bottomleft, obj.bottomright]
        coord = list(corners[i])
        tile_pos.add(get_index(coord[0], coord[1]))
    for tile in tile_pos:
        tile = 
def colliding_with_tile(tile, obj: pygame.Rect):
    pass