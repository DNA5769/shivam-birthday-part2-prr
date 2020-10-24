import random
import pygame
import os

class Powerup:
	def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
		self.img = pygame.image.load(os.path.join('images','powerups',random.choice(os.listdir(os.path.join('images','powerups')))))

		self.x = SCREEN_WIDTH + 5
		self.y = SCREEN_HEIGHT - self.img.get_height()
		self.speed = 3

	def move(self):
		self.x -= self.speed

	def draw(self, screen):
		screen.blit(self.img, (self.x, self.y))