from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):

    score = 0
    
    @classmethod
    def get_score(cls):
        return cls.score

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE,(self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
    
    def split(self):
        self.kill()
        
        if self.radius > ASTEROID_MIN_RADIUS * 2:  # Large asteroid
            Asteroid.score += 100
        elif self.radius > ASTEROID_MIN_RADIUS:    # Medium asteroid
            Asteroid.score += 50
        else:                                      # Small asteroid
            Asteroid.score += 25
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        small_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        small_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        small_asteroid1.velocity = velocity1 * 1.2
        small_asteroid2.velocity = velocity2 * 1.2
         




