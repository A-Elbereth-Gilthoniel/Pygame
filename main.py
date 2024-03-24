import pygame
from setting import *
from player import Player
import math
from map import world_map, text_map
from ray_casting2 import ray_casting
from drawing import Drawing

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
fps = 100
clock = pygame.time.Clock()
running = True
player = Player()
drawing = Drawing(screen)

while running: # Main game cycle
    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
    		running = False
    player.movement()
    screen.fill((0, 0, 0))
    drawing.background()
    drawing.fps(clock)

    drawing.world(player.pos, player.angle)

    # pygame.draw.circle(screen, (255, 0, 0), player.pos, 10)
    # pygame.draw.line(screen, (255, 0, 0), player.pos, (player.x + 15 * math.cos(player.angle),
    #                                                    player.y + 15 * math.sin(player.angle)))
    # for x, y in world_map:
    #     pygame.draw.rect(screen, (128, 128, 128), (x, y, TILE_WIDTH, TILE_HEIGHT), 2)

    # pygame.draw.circle(screen, (255, 0, 0), player.pos, 10 // 5)
    # pygame.draw.line(screen, (255, 0, 0), player.pos, ((player.x + 15 * math.cos(player.angle)),
    #                                                    (player.y + 15 * math.sin(player.angle))))
    # for x, y in world_map:
    #     pygame.draw.rect(screen, (128, 128, 128), (x, y, TILE_WIDTH, TILE_HEIGHT), 2)
    pygame.display.flip()
    clock.tick(fps)
