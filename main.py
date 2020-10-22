import os
import pygame
pygame.init()

WIDTH = HEIGHT = 500

icon = pygame.image.load(os.path.join('images', 'icon.png'))

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shivam's Walk")
pygame.display.set_icon(icon)

running = True
while running:
	screen.fill((0,0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	clock.tick(60)
	pygame.display.update()