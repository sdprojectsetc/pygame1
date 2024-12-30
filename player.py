import pygame
import sys

class Player:
	def __init__(self, name, image, x_speed, bounce):
		self.name = name
		self.image = pygame.image.load(image) #will need to receive 'blah.png'
		self.image = pygame.transform.scale(self.image, (50, 50))

		self.x_speed = x_speed
		self.bounce = bounce
		self.on_ground = True

		self.grav_eff = 1.2
		self.y_speed = 0
		self.jump_force = -15
		self.max_vy = 10
		self.damp = 0.85  #loose energy with each bounce


		self.rect = self.image.get_rect()

	def move(self, dx, dy, screen):
		if 0 < self.rect.x + dx <= screen.width - self.rect.width:
			self.rect.x += dx
		if 0 < self.rect.y + dy <= screen.height - self.rect.height:
			self.rect.y += dy

	def apply_grav_effect(self, screen, platforms):
		#apply gravity and cap falling speed
		if not self.on_ground:
			self.y_speed = min(self.y_speed + self.grav_eff, self.max_vy)
		
		# save prev pos	
		prev_rect = self.rect.copy()
		self.rect.y += self.y_speed
		
		#platform collision
		self.on_ground = False  #reset for each platform
		for platform in platforms:
			if self.rect.colliderect(platform.rect) and self.y_speed > 0:
				# move player down inc
				for y_offset in range(int(prev_rect.bottom), int(self.rect.bottom) + 1):
					# move player incrementally downward
					test_rect = self.rect.copy()
					test_rect.y = y_offset
					if test_rect.colliderect(platform.rect):
						if self.y_speed > 3:
							self.y_speed *= self.bounce * self.damp
							self.on_ground = False
						else:
							self.rect.bottom = platform.rect.top
							self.y_speed = 0
							self.on_ground = True
						break

		#ground collision
		if self.rect.bottom >= screen.height:
			self.rect.bottom = screen.height
			if self.y_speed > 3:
				self.y_speed *= self.bounce * self.damp
				self.on_ground = False
			else:
				self.y_speed = 0
				self.on_ground = True

	def jump(self, platforms):
		if self.on_ground:
			self.y_speed = self.jump_force
			self.on_ground = False

		prev_rect = self.rect.copy()
		self.rect.y += self.y_speed
		
		for platform in platforms:
			if self.rect.colliderect(platform.rect) and self.y_speed < 0:

				for y_offset in range(int(prev_rect.top), int(self.rect.top) - 1, -1):
					test_rect = self.rect.copy()
					test_rect.y = y_offset
					if test_rect.colliderect(platform.rect):
						self.rect.top = platform.rect.bottom
						self.y_speed = 0
						self.on_ground = False
						return

	def set_pos(self, screen):
		self.rect.center = (screen.width // 2, screen.height - self.rect.height // 2)
