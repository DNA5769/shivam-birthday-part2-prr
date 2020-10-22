import os
import pygame
pygame.init()

from player import Player

WIDTH = 800
HEIGHT = 450

BG = pygame.image.load(os.path.join('images', 'BG.jpg'))
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))
icon = pygame.image.load(os.path.join('images', 'icon.png'))

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shivam's Run")
pygame.display.set_icon(icon)

p = Player(HEIGHT)

running = True
while running:
	screen.blit(BG, (0,0))

	p.draw(screen)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	p.move()

	clock.tick(60)
	pygame.display.update()