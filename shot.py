from circleshape import *
from constants import *

class Shot(CircleShape):

    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x,y,SHOT_RADIUS)
        self.radius = SHOT_RADIUS
    
    def draw(self, surface):
        pygame.draw.circle(surface, WHITE,(self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
