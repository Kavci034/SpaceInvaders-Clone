import pygame
import laser


class enemy_laser(laser.Laser):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.transform.rotate(self.image, 180)
        self.speed = 10
        self.rect = self.image.get_rect()
        self.rect.center = pos
