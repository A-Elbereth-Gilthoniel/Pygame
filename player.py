from setting import *
import pygame
from math import sin, cos

class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property         # Превращение метода класса в атрибут (переменную)
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y += player_speed * sin(self.angle)
            self.x += player_speed * cos(self.angle)
        if keys[pygame.K_s]:
            self.y -= player_speed * sin(self.angle)
            self.x -= player_speed * cos(self.angle)
        if keys[pygame.K_a]:
            self.y += player_speed * sin(self.angle - RIGHT_ANGLE)
            self.x += player_speed * cos(self.angle - RIGHT_ANGLE)
        if keys[pygame.K_d]:
            self.y -= player_speed * sin(self.angle - RIGHT_ANGLE)
            self.x -= player_speed * cos(self.angle - RIGHT_ANGLE)
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02