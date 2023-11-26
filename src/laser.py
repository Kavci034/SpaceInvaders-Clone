import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("assets/laser.png").convert_alpha()
        self.image = pygame.transform.smoothscale_by(self.image, 0.75)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()
