import pygame
from setting import *
from ray_casting2 import ray_casting

class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 36, bold=True)

    def background(self):
        pygame.draw.rect(self.screen, (150, 75, 0), (0, HEIGHT // 2, WIDTH, HEIGHT // 2))
        pygame.draw.rect(self.screen, (127, 199, 255), (0, 0, WIDTH, HEIGHT // 2))

    def world(self, player_pos, player_angle):
        ray_casting(self.screen, player_pos, player_angle)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, True, (255, 0, 0))
        self.screen.blit(render, (WIDTH - 65, 5))