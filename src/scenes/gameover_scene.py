import scenes.scene
import scenes.scene_manager
import pygame
import score_manager


class gameover_scene(scenes.scene.Scene):
    def __init__(self, screen):
        super().__init__([], screen)
        self.background = pygame.image.load("assets/background.png").convert()
        self.font = pygame.font.Font("assets/Quicksand-Regular.ttf", 20)
        self.title_font = pygame.font.Font("assets/Quicksand-Regular.ttf", 50)
        self.starttext = self.font.render(
            "Press space to restart\nPress esc to return to title",
            True,
            (255, 255, 255),
        )
        self.scoretext = score_manager.get_score_text(self.font)
        self.scoretext_rect = self.scoretext.get_rect()
        self.scoretext_rect.center = (300, 400)
        self.starttext_rect = self.starttext.get_rect()
        self.starttext_rect.center = (300, 500)
        self.titletext = self.title_font.render("Game Over", True, (255, 255, 255))
        self.titletext_rect = self.titletext.get_rect()
        self.titletext_rect.center = (300, 300)

    def update(self):
        super().update()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.switch_scene(1)
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.switch_scene(0)

    def draw(self):
        for i in range(3):
            for j in range(4):
                self.screen.blit(self.background, (i * 256, j * 256))
        self.screen.blit(self.titletext, self.titletext_rect)
        self.screen.blit(self.starttext, self.starttext_rect)
        self.screen.blit(self.scoretext, self.scoretext_rect)
        super().draw()
