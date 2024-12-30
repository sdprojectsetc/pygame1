from screen import Screen
from player import Player
from platform import Platform
import pygame
import sys

if __name__ == "__main__":
	screen = Screen(800, 600)
	player = Player("player", 'player_image.png', 6, -0.7)
	player.set_pos(screen)

	platforms = [
		Platform(100, 500, 200, 5, pygame.Color("brown")), 
		Platform(400, 400, 250, 5, pygame.Color("brown")), 
		Platform(200, 300, 150, 5, pygame.Color("brown")),
		Platform(300, 200, 300, 5, pygame.Color("brown")),
	]

	running = True
	clock = pygame.time.Clock()
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			player.move(-player.x_speed, 0, screen)
		if keys[pygame.K_RIGHT]:
			player.move(player.x_speed, 0, screen)
		if keys[pygame.K_UP]:
			player.jump(platforms)
		
		player.apply_grav_effect(screen, platforms)

		screen.set_bg()
		for platform in platforms:
			platform.draw(screen.window)
		
		screen.window.blit(player.image, player.rect)
		screen.update()
		clock.tick(60)

	screen.quit()
	sys.exit()
