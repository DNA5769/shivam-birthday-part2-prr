import os
import pygame

class Player:
	def __init__(self, SCREEN_HEIGHT):
		self.WIDTH = 92
		self.HEIGHT = 100
		self.HEAD_WIDTH = 48
		self.HEAD_HEIGHT = 48
		self.x = 20
		self.y = 3*SCREEN_HEIGHT//4
		self.jump = False
		self.jump_ind = -1
		self.jump_path = list(range(-2,-31,-2)) + abs(sum(list(range(-2,-31,-2))))//2*[2] + ([1] if abs(sum(list(range(-2,-31,-2))))%2!=0 else [])
		self.jump_len = len(self.jump_path)
		self.health = self.max_health = 100
		self.health_decay = 20
		self.score_mult = 30


		self.src = [pygame.image.load(os.path.join('images', 'sprites', f'walk{i}.png')) for i in range(8)]
		self.src = [pygame.transform.scale(img, (self.WIDTH, self.HEIGHT)) for img in self.src]
		self.head = pygame.image.load(os.path.join('images', 'player_head.png'))
		self.head = pygame.transform.scale(self.head, (self.HEAD_WIDTH, self.HEAD_HEIGHT))

		self.ind = -1
		self.speed = 10
		self.dist = -1

	def draw(self, screen):
		screen.blit(self.src[self.ind], (self.x, self.y))
		screen.blit(self.head, (self.x+self.head.get_width()/2+5, self.y - 7.5))

	def move(self, keys):
		self.dist += 1
		if self.dist == self.speed:
			self.dist = -1
			self.ind = (self.ind+1)%8

		if keys[pygame.K_SPACE] and not self.jump:
			self.jump = True

		if self.jump:
			self.jump_ind += 1

			if self.jump_ind == self.jump_len:
				self.jump_ind = -1
				self.jump = False
			else:
				self.y += self.jump_path[self.jump_ind]


