from settings import *
import pygame
from player import Player
from pygame_tools import Button, blit_text, blit_surfaces_horizontal


def change_player_menu():
    run = True
    clock = pygame.time.Clock()
    fps = 60

    back_button = Button(menu_button_images["Back"], (0, 0))
    images = [main_characters[image]["idle_left"][0] for image in main_characters]
    for i, image in enumerate(images):
        images[i] = pygame.transform.scale2x(pygame.transform.scale2x(image))

    current_selected = 1

    previous_button = Button(
        menu_button_images["Previous"],
        (button_size * 4 - button_size / 2, images[0].get_height() + button_size * 2.5),
    )
    next_button = Button(
        menu_button_images["Next"],
        (
            (window_width - (button_size * 4)) - button_size / 2,
            images[0].get_height() + button_size * 2.5,
        ),
    )
    image_width = images[0].get_width()

    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.clicked():
                    name = list(main_characters.keys())
                    return name[current_selected]
                if previous_button.clicked():
                    current_selected -= 1
                if next_button.clicked():
                    current_selected += 1
                if current_selected < 0 or current_selected > len(images):
                    current_selected = 0

        window.fill((255, 255, 255))
        back_button.display(window)
        next_button.display(window)
        previous_button.display(window)
        blit_surfaces_horizontal(
            window,
            [image_width + 32 - image_width * current_selected, button_size * 2],
            *images
        )
        pygame.display.update()

    pygame.quit()
    quit()


def settings_menu():
    run = True
    clock = pygame.time.Clock()
    fps = 60

    back_button = Button(menu_button_images["Back"], (0, 0))
    player_change_button = Button(
        menu_button_images["Settings"], (button_size, button_size)
    )
    name = None

    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.clicked():
                    return name
                if player_change_button.clicked():
                    name = change_player_menu()

        window.fill((255, 255, 255))
        back_button.display(window)
        player_change_button.display(window)
        blit_text(
            window,
            "Character Customization",
            (player_change_button.rect.right, player_change_button.y),
        )
        pygame.display.update()

    pygame.quit()
    quit()


def main_menu():
    run = True
    clock = pygame.time.Clock()
    fps = 60

    play_button = Button(
        menu_button_images["Play"],
        (window_width / 2 - button_size / 2, window_height / 2 - button_size / 2),
    )
    settings_button = Button(
        menu_button_images["Settings"], (0, window_height - button_size)
    )

    character = "VirtualGuy"

    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if play_button.clicked():
                    player = Player(100, 100, main_characters[character])
                    return player
                if settings_button.clicked():
                    name = settings_menu()
                    if name is not None:
                        character = name

        window.fill((255, 255, 255))
        play_button.display(window)
        settings_button.display(window)
        pygame.display.update()

    pygame.quit()
    quit()
