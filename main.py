import os
import random
from pygame import mixer
import pygame
pygame.init()

from player import Player
from powerup import Powerup

WIDTH = 800
HEIGHT = 450

MUSIC_END = pygame.USEREVENT + 0
playlist = os.listdir('music')
random.shuffle(playlist)
curr_music = 0
mixer.music.load(os.path.join('music', playlist[curr_music]))
mixer.music.play()
mixer.music.set_endevent(MUSIC_END)

BG = pygame.image.load(os.path.join('images', 'BG.jpg'))
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))
icon = pygame.image.load(os.path.join('images', 'icon.png'))

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shivam's Run")
pygame.display.set_icon(icon)

spawn_time = 300
next_spawn = 0

player = Player(HEIGHT)
items = []

running = True
while running:
	screen.blit(BG, (0,0))

	next_spawn += 1
	if next_spawn == spawn_time:
		next_spawn = 0
		items.append(Powerup(WIDTH, HEIGHT))

	for x in items:
		x.draw(screen)
	player.draw(screen)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == MUSIC_END:
			curr_music = (curr_music+1)%len(playlist)

			mixer.music.load(os.path.join('music', playlist[curr_music]))
			mixer.music.play()

	keys = pygame.key.get_pressed()
	player.move(keys)
	for x in items:
		x.move()

	for x in items:
		if x.x + x.img.get_width() < -5:
			items.remove(x)

	clock.tick(60)
	pygame.display.update()