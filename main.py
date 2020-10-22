import pygame
pygame.init()

WIDTH = HEIGHT = 500

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shivam's Walk")

running = True
while running:
	screen.fill((0,0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	clock.tick(60)
	pygame.display.update()