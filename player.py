from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0
        self.angle = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self,screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(),2)

    def rotate(self,dt, direction):
        self.rotation += direction*PLAYER_TURN_SPEED*dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt, -1)
            self.angle -= ROTATION_SPEED

        if keys[pygame.K_d]:
            self.rotate(dt, 1)
            self.angle += ROTATION_SPEED
        
        if keys[pygame.K_w]:
            self.move(dt)  
        
        if keys[pygame.K_s]:
            self.move(dt) 

        if keys[pygame.K_SPACE]:
            self.shoot()
        
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        velocity = pygame.Vector2(0, 1).rotate(self.angle) 
        velocity *= PLAYER_SHOT_SPEED
        new_shot.velocity = velocity
