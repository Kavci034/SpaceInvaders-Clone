import scenes.scene_manager


class Scene:
    def __init__(self, sprite_groups, screen) -> None:
        self.spriteGroups = sprite_groups
        self.screen = screen
        self.switch_scene = scenes.scene_manager.switch_scene

    def update(self):
        for group in self.spriteGroups:
            group.update()

    def draw(self):
        for group in self.spriteGroups:
            group.draw(self.screen)
