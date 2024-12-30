import pygame
import sys

class Platform:
	def __init__(self, x, y, w, h, color):
		self.rect = pygame.Rect(x, y, w, h)
		self.color = color

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)
