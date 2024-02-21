from settings import *
import pygame
from main_menu import main_menu
from objects import Block, Spikes, SpikedBall, Platform

run = True
clock = pygame.time.Clock()
fps = 60

x_offset, y_offset = 0, 0
scroll_width_area = 200

objects = [
    Block(100, 200),
    Block(196, 200),
    Block(292, 200),
    Spikes(312, 200 - spike_size),
    Block(388, 200),
    SpikedBall(484, 200 - spiked_ball_size/2),
    Block(484, 200),
    Block(580, 200),
    Block(676, 296),
    Spikes(676 + spike_size, 296 - spike_size),
    Block(772, 296),
    Spikes(772 + spike_size, 296 - spike_size),
    Block(868, 296),
    Spikes(868 + spike_size, 296 - spike_size),
    Block(964, 200),
    Block(1060, 104),
    Block(1060, 8),
    Block(868, -88),
    SpikedBall(772, -88 - spiked_ball_size/2),
    Block(772, -88),
    Block(676, -88),
    Block(292, -184)
]


def display():
    window.fill((255, 255, 255))
    for i in range(window_width // background_tile_size + 1):
        for j in range(window_height // background_tile_size + 1):
            window.blit(
                background_images["Blue"],
                (i * background_tile_size, j * background_tile_size),
            )
    for obj in objects:
        obj.display(window, x_offset, y_offset)
    player.display(window, x_offset, y_offset)
    pygame.display.update()


if __name__ == "__main__":
    player = main_menu()
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            player.event_controls(event)

        if (
            player.rect.right - x_offset >= window_width - scroll_width_area
            and player.x_vel > 0
        ) or (player.rect.left - x_offset <= scroll_width_area and player.x_vel < 0):
            x_offset += player.x_vel
        if (
            player.rect.bottom - y_offset >= window_height - scroll_width_area
            and player.y_vel > 0
        ) or (player.rect.top - y_offset <= scroll_width_area and player.y_vel < 0):
            y_offset += player.y_vel
        player.script(fps, objects)
        display()
    pygame.quit()
    quit()