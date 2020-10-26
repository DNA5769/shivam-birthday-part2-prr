import os
import random
from pygame import mixer
import pygame
pygame.init()

from player import Player
from powerup import Powerup
from enemy import Enemy

WIDTH = 800
HEIGHT = 450

CS_FONT = pygame.font.Font(os.path.join('fonts', 'cs.ttf'), 25)

collect_sound = pygame.mixer.Sound(os.path.join('sounds', 'collect.wav'))
MUSIC_END = pygame.USEREVENT + 0
playlist = os.listdir('music')
random.shuffle(playlist)
curr_music = 0
mixer.music.load(os.path.join('music', playlist[curr_music]))
mixer.music.play()
mixer.music.set_endevent(MUSIC_END)
MUSIC_TEXT = CS_FONT.render('Now Playing - ' + playlist[curr_music][:-4], False, (255,255,0))

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
score = 0
health_decay_counter = -1
score_counter = -1
items = []

running = True
while running:
	screen.blit(BG, (0,0))

	next_spawn += 1
	if next_spawn == spawn_time:
		next_spawn = 0
		if not random.choice([0,1]):
			items.append(Enemy(WIDTH, HEIGHT))
		else:
			items.append(Powerup(WIDTH, HEIGHT))

	for x in items:
		x.draw(screen)
	player.draw(screen)
	screen.blit(MUSIC_TEXT, (WIDTH//2 - MUSIC_TEXT.get_width()//2, 3))
	HEALTH_TEXT = CS_FONT.render(f'Health: {player.health}/{player.max_health}', False, (255,0,0))
	screen.blit(HEALTH_TEXT, (1, 35))
	pygame.draw.rect(screen, (255,0,0), (HEALTH_TEXT.get_width()+3, 35, player.health*2,HEALTH_TEXT.get_height()), False)
	SCORE_TEXT = CS_FONT.render(f'Score: {score}km', False, (0,255,0))
	screen.blit(SCORE_TEXT, (1, 35+HEALTH_TEXT.get_height()+3))

	for x in items:
		player_col_pos = (player.x+player.WIDTH/2, player.y+player.HEIGHT)
		if player_col_pos[0] >= x.x and player_col_pos[0] <= x.x+x.WIDTH and player_col_pos[1] >= x.y and player_col_pos[1] <= x.y+x.HEIGHT:
			pygame.mixer.Sound.play(collect_sound)
			if isinstance(x, Powerup):
				player.health = min(player.max_health, player.health+10)
			else:
				player.health = max(0, player.health-10)
			items.remove(x)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == MUSIC_END:
			curr_music = (curr_music+1)%len(playlist)

			mixer.music.load(os.path.join('music', playlist[curr_music]))
			MUSIC_TEXT = CS_FONT.render('Now Playing - ' + playlist[curr_music][:-4], False, (255,255,0))
			mixer.music.play()

	keys = pygame.key.get_pressed()
	player.move(keys)
	for x in items:
		x.move()

	for x in items:
		if x.x + x.img.get_width() < -5:
			items.remove(x)

	health_decay_counter += 1
	if health_decay_counter == player.health_decay:
		health_decay_counter = -1
		player.health = max(0, player.health-1)
	score_counter += 1
	if score_counter == player.score_mult:
		score_counter = -1
		score += 1
	clock.tick(60)
	pygame.display.update()