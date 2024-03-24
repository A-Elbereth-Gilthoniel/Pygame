import pygame
from setting import *
from map import world_map

# def ray_casting(screen, player_pos, player_angle):
#     half_fov = FOV / 2
#     cur_angle = (player_angle - half_fov)
#     xo, yo = player_pos
#     for ray in range(NUM_RAYS):
#         sin_a = math.sin(cur_angle)
#         cos_a = math.cos(cur_angle)
#         for depth in range(MAX_DEPTH):
#             x = xo + depth * cos_a
#             y = yo + depth * sin_a
#            # pygame.draw.line(screen, (128, 128, 128), player_pos, (x, y), 2)
#             if (x // TILE_WIDTH * TILE_WIDTH, y // TILE_HEIGHT * TILE_HEIGHT) in world_map:
#                 print((x // TILE_WIDTH * TILE_WIDTH, y // TILE_HEIGHT * TILE_HEIGHT))
#                 depth *= math.cos(player_angle - cur_angle)
#                 proj_height = PROJ_COEFF / depth
#                 c = 255 / (1 + depth * depth * 0.00001)
#                 color = (c, c // 2, c // 3)
#                 cur_height = (TILE_HEIGHT*2 / depth) * 100
#                 pygame.draw.rect(screen, color, (ray * (WIDTH // NUM_RAYS), (HEIGHT // 2 - cur_height // 2) - cur_height, WIDTH // NUM_RAYS, cur_height * 2))
#                 break
#         cur_angle += DELTA_ANGLE


# def ray_casting(screen, player_pos, player_angle):
#     half_fov = FOV / 2
#     cur_angle = (player_angle - half_fov)
#     xo, yo = player_pos
#     xm, ym = (xo // TILE_WIDTH) * TILE_WIDTH, (yo // TILE_WIDTH) * TILE_WIDTH
#     for ray in range(NUM_RAYS):
#         sin_a = math.sin(cur_angle)
#         cos_a = math.cos(cur_angle)
#         fx, fy = ((xo + MAX_DEPTH * cos_a) // TILE_WIDTH) * TILE_WIDTH, ((yo + MAX_DEPTH * sin_a) // TILE_WIDTH) * TILE_WIDTH
#         print(fx, fy, xm, ym, xo, yo, sin_a, cos_a)
#         variants = []
#         for x in range(int(min(xm, fx)), int(max(xm + 1, fx + 1)), 100):
#             depth = (x - xo) / cos_a
#             y = yo + depth * sin_a
#             print((x // TILE_WIDTH * TILE_WIDTH, y // TILE_HEIGHT * TILE_HEIGHT))
#             if (x // TILE_WIDTH * TILE_WIDTH, y // TILE_HEIGHT * TILE_HEIGHT) in world_map:
#                 print((x // TILE_WIDTH * TILE_WIDTH, y // TILE_HEIGHT * TILE_HEIGHT))
#                 variants.append(depth)
#
#
#         for y in range(int(min(ym, fy)), int(max(ym + 1, fy + 1)), 100):
#             depth = (y - yo) / sin_a
#             x = xo + depth * cos_a
#             print((x // TILE_WIDTH * TILE_WIDTH, y // TILE_HEIGHT * TILE_HEIGHT))
#             if (x // TILE_WIDTH * TILE_WIDTH, y // TILE_HEIGHT * TILE_HEIGHT) in world_map:
#                 print((x // TILE_WIDTH * TILE_WIDTH, y // TILE_HEIGHT * TILE_HEIGHT))
#                 variants.append(depth)
#
#         depth = min(variants)
#         depth *= math.cos(player_angle - cur_angle)
#         c = 255 / (1 + depth * depth * 0.00001)
#         color = (c, c // 2, c // 3)
#         cur_height = (TILE_HEIGHT*2 / depth) * 100
#         pygame.draw.rect(screen, color, (ray * (WIDTH // NUM_RAYS), (HEIGHT // 2 - cur_height // 2) - cur_height, WIDTH // NUM_RAYS, cur_height * 2))
#         pygame.draw.line(screen, (128, 128, 128), player_pos, (x, y), 2)
#         cur_angle += DELTA_ANGLE




def mapping(a, b):
    return (a // TILE_WIDTH) * TILE_WIDTH, (b // TILE_HEIGHT) * TILE_HEIGHT


def ray_casting(screen, player_pos, player_angle):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - (FOV / 2)
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        if cos_a >= 0:
            x = xm + TILE_WIDTH
            dx = 1
        else:
            x = xm
            dx = -1

        for i in range(0, WIDTH, TILE_WIDTH):
            depth_v = (x - ox) / cos_a
            y = oy + depth_v * sin_a
            if mapping(x + dx, y) in world_map:
                break
            x += dx * TILE_WIDTH

        y, dy = (ym + TILE_WIDTH, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, HEIGHT, TILE_HEIGHT):
            depth_h = (y - oy) / sin_a
            x = ox + depth_h * cos_a
            if mapping(x, y + dy) in world_map:
                break
            y += dy * TILE_HEIGHT


        depth = depth_h if depth_h < depth_v else depth_v
        depth *= math.cos(player_angle - cur_angle)
        proj_height = PROJ_COEFF / depth
        c = 255 / (1 + depth * depth * 0.00001)
        color = (c, c // 2, c // 3)
        cur_height = (TILE_HEIGHT*2 / depth) * 100
        pygame.draw.rect(screen, color, (ray * (WIDTH // NUM_RAYS), (HEIGHT // 2 - cur_height // 2) - cur_height, WIDTH // NUM_RAYS, cur_height * 2))
        cur_angle += DELTA_ANGLE