import pygame

# x - screen_x

class Player:
    def __init__(self, x: int, y: int, screen):
        self.x_vel = 0
        self.y_vel = 0
        self.world_x = 0
        self.world_y = 0
        self.screen = screen
        self.reconstruct()
        
    def update(self, keys, level, dt):
        if keys[pygame.K_d]:
            self.x_vel += 5
        if keys[pygame.K_a]:
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
        self.world_y += 1
        self.reconstruct()
        touching = level.colliding(self.playerrect)
        self.world_y -= 1
        return touching

    def trymove(self, x_vel, y_vel, level):
        if x_vel:
            self.world_x += x_vel
            self.reconstruct()
            if level.colliding(self.playerrect):
                self.world_x -= x_vel
                self.reconstruct()
                
        if y_vel:
            self.world_y += y_vel
            self.reconstruct()
            if level.colliding(self.playerrect):
                self.world_y -= y_vel
                self.reconstruct()
                self.y_vel = 0
                    
    def reconstruct(self):
        self.playerrect = pygame.Rect(self.world_x, self.world_y, 64, 100)

    def draw(self):
        self.playerrect.x = (self.world_x - self.camera.x, self.world_y -)
        pygame.draw.rect(self.screen, (0, 255, 0), 

if __name__ == "__main__":
    import entry