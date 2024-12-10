import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
	
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")		
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	
	player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )
	
	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)

	AsteroidField.containers = (updatable,)
	asteroid_field = AsteroidField()

	while True:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		for obj in updatable:
			obj.update(dt)

		for obj in asteroids:
			value = obj.check_collisions(player)
			if value == True:
				print("Game over!")
				sys.exit()
			
		
			
		screen.fill(BLACK)
		
		for obj in drawable:
			obj.draw(screen)
		
		dt = clock.tick(60)/1000
		pygame.display.flip()

if __name__ == "__main__":
		main()
