from circleshape import *
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE,(self.x, self.y), self.radius, 2)
    
    def update(self, dt):
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt
    



