import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


def load_assets():
    bird_img = pygame.image.load("яйцо.png")
    bird_img = pygame.transform.scale(bird_img, (50, 50))
    pipe_img = pygame.image.load("труба.png")
    pipe_img = pygame.transform.scale(pipe_img, (70, SCREEN_HEIGHT))
    background_day = pygame.image.load("фон.png")
    background_night = pygame.image.load("фон_ночь.png")
    background_day = pygame.transform.scale(
        background_day,background_night (SCREEN_WIDTH, SCREEN_HEIGHT)
    
    )

    bonus_img = pygame.image.load("бонус.png")
    bonus_img = pygame.transform.scale(bonus_img, (30, 30))
    pygame.init()

    assets = {
        "bird_img": bird_img,
        "pipe_img": pipe_img,
        "background_day": background_day,
        "bonus_img": bonus_img,
        "flap_sound": pygame.mixer.Sound("nfg.wav"),
        "point_sound": pygame.mixer.Sound("накопление баллов.wav"),
        "collision_sound": pygame.mixer.Sound("удар.wav"),
        "bonus_sound": pygame.mixer.Sound("звук бонуса.wav"),
        "background_music": pygame.mixer.Sound("фон.wav"),
    }
    return assets


assets = load_assets()
