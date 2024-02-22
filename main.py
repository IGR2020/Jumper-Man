from settings import *
import pygame
from main_menu import main_menu
from objects import Block, Spikes, SpikedBall, Platform, Trophy

run = True
clock = pygame.time.Clock()
fps = 60

x_offset, y_offset = 0, 0
scroll_width_area = 200

objects = [
    [
        Block(100, 200),
        Block(196, 200),
        Block(292, 200),
        Spikes(312, 200 - spike_size),
        Block(388, 200),
        SpikedBall(484, 200 - spiked_ball_size / 2),
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
        SpikedBall(772, -88 - spiked_ball_size / 2),
        Block(772, -88),
        Block(676, -88),
        Block(292, -184),
        Trophy(288, -184 - check_point_size * 2),
    ],
    [
        Block(100, 200),
        Block(196, 200),
        Platform(388, 200, platform_images["Brown On (32x8)"], 292, 1060),
        SpikedBall(580, 200 - spiked_ball_size / 2),
        Block(1060, 200),
    ],
    [
        Block(100, 200),
        Block(196, 200),
    ],
    [
        Block(100, 200),
        Block(196, 200),
    ],
    [
        Block(100, 200),
        Block(196, 200),
    ],
    [
        Block(100, 200),
        Block(196, 200),
    ],
    [
        Block(100, 200),
        Block(196, 200),
    ],
]


def display():
    global x_offset, y_offset
    window.fill((255, 255, 255))
    for i in range(window_width // background_tile_size + 1):
        for j in range(window_height // background_tile_size + 1):
            window.blit(
                background_images[current_background_tile],
                (i * background_tile_size, j * background_tile_size),
            )
    for obj in objects[current_level]:
        obj.display(window, x_offset, y_offset)
    x_offset, y_offset = player.display(window, x_offset, y_offset)
    pygame.display.update()


if __name__ == "__main__":
    player, current_background_tile, current_level = main_menu(current_level)
    current_level = current_level[0]
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
        if player.script(fps, objects[current_level]):
            current_level += 1
            x_offset, y_offset = 0, 0
            player, current_background_tile, current_level = main_menu(current_level)
            current_level = current_level[0]
        display()
    pygame.quit()
    quit()
