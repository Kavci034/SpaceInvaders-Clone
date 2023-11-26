import pygame

import scenes.scene
import scenes.scene_manager
import math
import score_manager


class title_scene(scenes.scene.Scene):
    def __init__(
        self,
        screen,
    ):
        super().__init__([], screen)
        self.background = pygame.image.load("assets/background.png").convert()

        self.font = pygame.font.Font("assets/Quicksand-Regular.ttf", 20)
        self.title_font = pygame.font.Font("assets/Quicksand-Regular.ttf", 50)

        self.starttext = self.font.render("Press space to start", True, (255, 255, 255))
        self.starttext_rect = self.starttext.get_rect()
        self.starttext_rect.center = (300, 500)

        self.titletext = self.title_font.render("Space Invaders", True, (255, 255, 255))
        self.titletext_rect = self.titletext.get_rect()
        self.titletext_rect.center = (280, 300)

        self.highscore_text = self.font.render(
            "Highscore: " + str(score_manager.get_highscore()), True, (255, 255, 255)
        )
        self.highscore_text_rect = self.highscore_text.get_rect()
        self.highscore_text_rect.center = (300, 400)

        self.time = 0

    def update(self):
        super().update()
        self.time += 0.07
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.next_scene = "main"
        self.titletext_rect.center = (300, 280 + math.sin(self.time) * 10)
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.switch_scene(1)

    def draw(self):
        for i in range(3):
            for j in range(4):
                self.screen.blit(self.background, (i * 256, j * 256))
        self.screen.blit(self.titletext, self.titletext_rect)
        self.screen.blit(self.starttext, self.starttext_rect)
        self.screen.blit(self.highscore_text, self.highscore_text_rect)
        super().draw()
