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
	game_over = False
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	font = pygame.font.Font(None, 36)
	game_over_text = font.render("GAME OVER !!!", True, BLACK)
	play_again_text = font.render("Press SPACE to play again!", True, BLACK)
	


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
		if not game_over:
			for obj in updatable:
				obj.update(dt)


		# Check collisions between player and asteroids
		for obj in asteroids:
			value = obj.check_collisions(player)
			if value == True:
				game_over = True

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

		# Draw score
		score_text = font.render(f"Score: {Asteroid.get_score()}", True, GRAY)
		screen.blit(score_text, (10, 10))
    
		if game_over:
			screen.fill(GRAY)

			center_x = SCREEN_WIDTH // 2
			center_y = SCREEN_HEIGHT // 2
	
			final_score_text = font.render(f"Final Score: {Asteroid.get_score()}", True, BLACK)
			
			game_over_pos = (center_x - game_over_text.get_width()//2, center_y - 50)
			final_score_pos = (center_x - final_score_text.get_width()//2, center_y)
			play_again_pos = (center_x - play_again_text.get_width()//2, center_y + 50)

			screen.blit(game_over_text, game_over_pos)
			screen.blit(final_score_text, final_score_pos)
			screen.blit(play_again_text, play_again_pos)

			keys = pygame.key.get_pressed()
			if keys[pygame.K_SPACE]:
				
				# Reset game state
				player.position = pygame.math.Vector2(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
				player.velocity = pygame.math.Vector2(0, 0)
				Asteroid.score = 0  
				asteroids.empty()  
				shots.empty() 
				game_over = False
		
		dt = clock.tick(60)/1000
		pygame.display.flip()

if __name__ == "__main__":
		main()
