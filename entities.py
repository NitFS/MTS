import pygame
import random
from settings import *
from assets import *

pygame.init()


class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.width = 50
        self.height = 50
        self.velocity = 0
        self.shield = False
        self.shield_timer = 0

    def draw(self, screen):
        rotated_bird = pygame.transform.rotate(assets["bird_img"], -self.velocity * 2)
        screen.blit(rotated_bird, (self.x, self.y))
        if self.shield:
            pygame.draw.circle(
                screen,
                BLUE,
                (self.x + self.width // 2, self.y + self.height // 2),
                35,
                2,
            )

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        self.y = max(0, min(SCREEN_HEIGHT - self.height, self.y))
        if self.shield:
            self.shield_timer -= 1
            if self.shield_timer <= 0:
                self.shield = False

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def activate_shield(self, duration):
        self.shield = True
        self.shield_timer = duration


class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = 70
        self.top_height = random.randint(50, SCREEN_HEIGHT - PIPE_GAP - 200)
        self.bottom_height = SCREEN_HEIGHT - self.top_height - PIPE_GAP

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.x, 0, self.width, self.top_height))
        pygame.draw.rect(
            screen,
            GREEN,
            (
                self.x,
                SCREEN_HEIGHT - self.bottom_height,
                self.width,
                self.bottom_height,
            ),
        )

    def update(self):
        self.x -= PIPE_SPEED

    def is_off_screen(self):
        return self.x + self.width < 0


class Bonus:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30

    def draw(self, screen):
        screen.blit(assets["bonus_img"], (self.x, self.y))

    def update(self):
        self.x -= PIPE_SPEED

    def is_collected(self, bird):
        return (
            bird.x < self.x + self.width
            and bird.x + bird.width > self.x
            and bird.y < self.y + self.height
            and bird.y + bird.height > self.y
        )
