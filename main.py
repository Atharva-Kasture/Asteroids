import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
	
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")		
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	# Create groups for handling objects that need updating or drawing
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	
	# Set player groups and initialize player at the center of the screen
	Player.containers = (updatable, drawable)
	player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )
	
	# Set asteroid groups
	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)

	# Set shot groups
	shots = pygame.sprite.Group()
	Shot.containers = (shots, updatable, drawable)

	# Initialize asteroid field which generates asteroids
	AsteroidField.containers = (updatable,)
	asteroid_field = AsteroidField()



	while True:
		
		# Exit the game loop if the quit event is triggered
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		# Update all updatable objects
		for obj in updatable:
			obj.update(dt)


		# Check collisions between player and asteroids
		for obj in asteroids:
			value = obj.check_collisions(player)
			if value == True:
				print("Game over!")
				sys.exit()

		#Check collisions between asteroids and shots
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.check_collisions(shot):
					asteroid.split()
					shot.kill()

		# Clear the screen
		screen.fill(BLACK)
		
		# Draw all drawable objects
		for obj in drawable:
			obj.draw(screen)
		
		
		dt = clock.tick(60)/1000
		pygame.display.flip()

if __name__ == "__main__":
		main()
