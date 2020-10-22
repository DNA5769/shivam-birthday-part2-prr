import os
import pygame

class Player:
	def __init__(self, SCREEN_HEIGHT):
		self.WIDTH = 92
		self.HEIGHT = 100
		self.x = 20
		self.y = 3*SCREEN_HEIGHT//4 - self.HEIGHT//2

		self.src = [pygame.image.load(os.path.join('images', 'sprites', f'walk{i}.png')) for i in range(8)]
		self.src = [pygame.transform.scale(img, (self.WIDTH, self.HEIGHT)) for img in self.src]
		
		self.ind = 0
		self.speed = 10
		self.dist = 0

	def draw(self, screen):
		screen.blit(self.src[self.ind], (self.x, self.y))

	def move(self):
		self.dist += 1
		if self.dist == self.speed:
			self.dist = 0
			self.ind += 1
			if self.ind == 8:
				self.ind = 0