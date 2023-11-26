import pickle
import pygame
import scenes.main_scene as main_scene


def get_score_text(font: pygame.font.Font) -> pygame.surface.Surface:
    with open("data.pickle", "rb") as f:
        data = pickle.load(f)
        if main_scene.score > data["highscore"]:
            data["highscore"] = main_scene.score
            with open("data.pickle", "wb") as f:
                pickle.dump(data, f)
    return font.render(
        "Score: " + str(main_scene.score) + "\nHighscore: " + str(data["highscore"]),
        True,
        (255, 255, 255),
    )


def get_highscore() -> int:
    with open("data.pickle", "rb") as f:
        data = pickle.load(f)
        return data["highscore"]
