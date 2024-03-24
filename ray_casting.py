import pygame
from setting import *
from map import world_map

def ray_casting(screen, player_pos, player_angle):
    half_fov = FOV / 2
    cur_angle = (player_angle - half_fov)
    xo, yo = player_pos
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
           # pygame.draw.line(screen, (128, 128, 128), player_pos, (x, y), 2)
            if (x // TILE_WIDTH * TILE_WIDTH, y // TILE_HEIGHT * TILE_HEIGHT) in world_map:
                depth *= math.cos(player_angle - cur_angle)
                proj_height = PROJ_COEFF / depth
                c = 255 / (1 + depth * depth * 0.0001)
                color = (c, c, c)
                pygame.draw.rect(screen, color, (ray * SCALE, HEIGHT // 2 - proj_height // 2, SCALE, proj_height))
                break
        cur_angle += DELTA_ANGLE