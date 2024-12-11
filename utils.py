import pygame


def draw_text(screen, text, x, y, color):
    font = pygame.font.SysFont("Arial", 30)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))
