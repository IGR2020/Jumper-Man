from settings import *
import pygame
from player import Player
from pygame_tools import Button, blit_text, blit_surfaces_horizontal


def change_background_menu():
    global current_background_tile

    run = True
    clock = pygame.time.Clock()
    fps = 60

    previous_button = Button(
        menu_button_images["Previous"],
        (button_size * 4 - button_size / 2, 250 + button_size * 2.5),
    )
    next_button = Button(
        menu_button_images["Next"],
        (
            (window_width - (button_size * 4)) - button_size / 2,
            250 + button_size * 2.5,
        ),
    )

    back_button = Button(menu_button_images["Back"], (0, 0))
    tiles_display_surface = pygame.Surface((900, 150))
    tiles_display_surface.fill((255, 255, 255))

    x_offset = 226
    current_choice = 3

    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.clicked():
                    return
                if previous_button.clicked():
                    x_offset += 64
                    current_choice -= 1
                if next_button.clicked():
                    current_choice += 1
                    x_offset -= 64
                if current_choice < 0 or current_choice >= len(
                    list(background_images.keys())
                ):
                    current_choice = 0
                current_background_tile = list(background_images.keys())[current_choice]

        window.fill((255, 255, 255))
        for i in range(window_width // background_tile_size + 1):
            for j in range(window_height // background_tile_size + 1):
                window.blit(
                    background_images[current_background_tile],
                    (i * background_tile_size, j * background_tile_size),
                )
        window.blit(tiles_display_surface, (0, 175))
        blit_surfaces_horizontal(
            tiles_display_surface,
            [x_offset, 43],
            *[surface for surface in background_images.values()]
        )
        back_button.display(window)
        previous_button.display(window)
        next_button.display(window)
        pygame.display.update()

    pygame.quit()
    quit()


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
                if current_selected < 0 or current_selected >= len(images):
                    current_selected = 0

        window.fill((255, 255, 255))
        for i in range(window_width // background_tile_size + 1):
            for j in range(window_height // background_tile_size + 1):
                window.blit(
                    background_images[current_background_tile],
                    (i * background_tile_size, j * background_tile_size),
                )
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
    background_tile_change_button = Button(
        menu_button_images["Settings"], (button_size, button_size * 2 + 16)
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
                if background_tile_change_button.clicked():
                    change_background_menu()

        window.fill((255, 255, 255))
        for i in range(window_width // background_tile_size + 1):
            for j in range(window_height // background_tile_size + 1):
                window.blit(
                    background_images[current_background_tile],
                    (i * background_tile_size, j * background_tile_size),
                )
        back_button.display(window)
        player_change_button.display(window)
        blit_text(
            window,
            "Character Customization",
            (player_change_button.rect.right, player_change_button.y),
            size=50,
        )
        background_tile_change_button.display(window)
        blit_text(
            window,
            "Background Customization",
            (
                background_tile_change_button.rect.right,
                background_tile_change_button.y,
            ),
            size=50,
        )
        pygame.display.update()

    pygame.quit()
    quit()


def main_menu(current_level):
    run = True
    clock = pygame.time.Clock()
    fps = 60

    play_button = Button(
        menu_button_images["Play"],
        (window_width / 2 - button_size / 2 - 10, window_height / 2 - button_size / 2),
    )
    settings_button = Button(
        menu_button_images["Settings"], (0, window_height - button_size)
    )

    level_buttons = []
    level = 0
    for i in range(main_menu_level_formatting[0]):
        for j in range(main_menu_level_formatting[1]):
            level_buttons.append(
                Button(
                    level_images[level],
                    (
                        level_blit_point[0] + i * level_image_size + i * 20,
                        level_blit_point[1] + j * level_image_size + j * 20,
                    ),
                    level,
                )
            )
            level += 1

    character = "VirtualGuy"

    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if play_button.clicked():
                    player = Player(100, 100, main_characters[character])
                    return player, current_background_tile, current_level
                if settings_button.clicked():
                    name = settings_menu()
                    if name is not None:
                        character = name
                for button in level_buttons:
                    if button.clicked():
                        current_level = button.information
                        player = Player(100, 100, main_characters[character])
                        return (player, current_background_tile, current_level)

        window.fill((255, 255, 255))
        for i in range(window_width // background_tile_size + 1):
            for j in range(window_height // background_tile_size + 1):
                window.blit(
                    background_images[current_background_tile],
                    (i * background_tile_size, j * background_tile_size),
                )
        for button in level_buttons:
            button.display(window)
        play_button.display(window)
        settings_button.display(window)
        pygame.display.update()

    pygame.quit()
    quit()
