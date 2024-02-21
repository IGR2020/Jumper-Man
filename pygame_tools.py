import pygame
from os.path import join, isfile
from os import listdir

pygame.font.init()


def blit_text(
    win, text, pos=(0, 0), colour=(0, 0, 0), size=30, font="arialblack", blit=True
):
    font_style = pygame.font.SysFont(font, size)
    text_surface = font_style.render(text, False, colour)
    if blit:
        win.blit(text_surface, pos)
    return text_surface


class Button:
    def __init__(self, image, pos, scale=1):
        self.x, self.y = pos
        self.width, self.height = image.get_width() * scale, image.get_height() * scale
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.transform.scale(image, (self.width, self.height))

    def clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True

    def display(self, win):
        win.blit(self.image, self.rect)


def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(path, width, height, direction=True, resize=None):
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()
        sprites = []

        for i in range(sprite_sheet.get_width() // width):
            for j in range(sprite_sheet.get_height() // height):
                surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
                rect = pygame.Rect(i * width, j * height, width, height)
                surface.blit(sprite_sheet, (0, 0), rect)
                sprites.append(pygame.transform.scale2x(surface))

        if resize is not None:
            sprites = [pygame.transform.scale(surface, resize) for surface in sprites]

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


def load_sprite_sheet(path, width, height, resize, direction=True):
    if not isinstance(path, pygame.Surface):
        path = join("assets", path)
        sprite_sheet = pygame.image.load(path).convert_alpha()
    sprites = []
    resize_sprites = []

    for i in range(sprite_sheet.get_width() // width):
        surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        rect = pygame.Rect(i * width, 0, width, height)
        surface.blit(sprite_sheet, (0, 0), rect)
        sprites.append(pygame.transform.scale2x(surface))
        if direction:
            sprites.append(flip(pygame.transform.scale2x(surface)))
    if resize is None:
        return sprites
    for sprite in sprites:
        resize_sprites.append(pygame.transform.scale(sprite, resize))

    return resize_sprites


def load_assets(path, size: list[int, int] | tuple[int, int] | None = None) -> dict:
    files = {}
    for file in listdir(path):
        if size is None:
            files[file.replace(".png", "")] = pygame.image.load(join(path, file))
        else:
            files[file.replace(".png", "")] = pygame.transform.scale(
                pygame.image.load(join(path, file)), size
            )
    return files


def load_assets_list(path, size) -> list:
    files = []
    for file in listdir(path):
        if size is None:
            files.append(pygame.image.load(join(path, file)))
        else:
            files.append(
                pygame.transform.scale(pygame.image.load(join(path, file)), size)
            )
    return files


def add_dict(dict1: dict, dict2: dict) -> dict:
    new_dict = {k: dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1 | dict2)}
    return new_dict


def set_to_grid(
    grid_size: int, coordinates: tuple[int, int]
) -> tuple[int, int]:  # sets a coordinate to align with a grid #
    x_offset = coordinates[0] % grid_size
    y_offset = coordinates[1] % grid_size
    new_coordinates = (coordinates[0] - x_offset, coordinates[1] - y_offset)
    return new_coordinates


def blit_surfaces_horizontal(window : pygame.Surface, start_location : list[int, int], *args):
    for surface in args:
        window.blit(surface, start_location)
        start_location[0] += surface.get_width()
    return window
