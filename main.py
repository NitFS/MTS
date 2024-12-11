import pygame

from settings import *
from assets import *
from entities import Bird, Pipe, Bonus
from utils import draw_text
import random

pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Timekiller")
pygame.mixer.Sound.play(assets["background_music"], loops=-1)

bird = Bird()
pipes = [Pipe(400), Pipe(600), Pipe(900)]
bonuses = []

clock = pygame.time.Clock()
running = True
score = 0
frame_count = 0
background_toggle = True


def check_collision():
    if bird.shield:
        return False
    for pipe in pipes:
        if (
            bird.x + bird.width > pipe.x
            and bird.x < pipe.x + pipe.width
            and (
                bird.y < pipe.top_height
                or bird.y + bird.height > SCREEN_HEIGHT - pipe.bottom_height
            )
        ):
            assets["collision_sound"].play()
            return True
    return False


while running:
    background_toggle = frame_count // 1000 % 2 == 0
    screen.blit(
        assets["background_day" if background_toggle else "background_night"], (0, 0)
    )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.flap()
                assets["flap_sound"].play()

    bird.update()
    bird.draw(screen)

    for pipe in pipes:
        pipe.update()
        pipe.draw(screen)

    if pipes[0].is_off_screen():
        pipes.pop(0)
        pipes.append(Pipe(pipes[-1].x + 300))
        score += 1
        assets["point_sound"].play()

    for bonus in bonuses[:]:
        bonus.update()
        bonus.draw(screen)
        if bonus.is_collected(bird):
            bird.activate_shield(BONUS_DURATION)
            bonuses.remove(bonus)
            assets["bonus_sound"].play()

    if frame_count % 500 == 0:
        bonuses.append(Bonus(SCREEN_WIDTH, random.randint(50, SCREEN_HEIGHT - 100)))

    if check_collision():
        draw_text(screen, "Game Over!", SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2, RED)
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    draw_text(screen, f"Score: {score}", 10, 10, WHITE)
    pygame.display.flip()
    clock.tick(FPS)
    frame_count += 1

pygame.quit()
