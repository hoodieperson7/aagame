import pygame
from math import floor

class Player:
    def __init__(self, x: int, y: int, screen):
        self.x_vel = 0
        self.y_vel = 0
        self.x = x
        self.y = y
        self.screen = screen
        self.reconstruct()
        
    def update(self, keys, level, dt):
        if keys[pygame.K_d]:
            if self.x_vel < 0:
                self.x_vel *= 0.3
            self.x_vel += 5
        if keys[pygame.K_a]:
            if self.x_vel > 0:
                self.x_vel *= 0.3
            self.x_vel -= 5
        self.x_vel = max(self.x_vel, -12)
        self.x_vel = min(self.x_vel, 12)

        if self.touchingground(level):
            if keys[pygame.K_a] or keys[pygame.K_d]:
                self.x_vel *= 0.85
            else:
                self.x_vel *= 0.8
            
            if keys[pygame.K_w]:
                self.y_vel -= 12

        else:
            self.x_vel *= 0.95

        if keys[pygame.K_s]:
            self.x_vel *= 0.65
        
        self.y_vel += 1

        self.trymove(self.x_vel * dt * 60, self.y_vel * dt * 60, level)

    def touchingground(self, level):
        self.y += 1
        self.reconstruct()
        touching = level.colliding(self.playerrect)
        self.y -= 1
        self.reconstruct()
        return touching

    def trymove(self, x_vel, y_vel, level):
        if x_vel:
            self.x += x_vel
            self.reconstruct()
            if level.colliding(self.playerrect):
                self.x -= x_vel
                self.reconstruct()
                
        if y_vel:
            self.y += y_vel
            self.reconstruct()
            if level.colliding(self.playerrect):
                self.y -= y_vel
                self.reconstruct()
                self.y_vel = 0
                    
    def reconstruct(self):
        self.playerrect = pygame.Rect(self.x, self.y, 64, 100)

    def draw(self):
        pygame.draw.rect(self.screen, (0, 255, 0), self.playerrect)
    
    def resize(self, screen_w, screen_h):
        x_ratio = self.x / screen_w
        y_ratio = self.y / screen_h
        
        self.screen_w = screen_w
        self.screen_h = screen_h
        
        self.x = x_ratio * screen_w
        self.y = y_ratio * screen_h
        
        self.y_vel = 0
        self.reconstruct()

if __name__ == "__main__":
    import entry