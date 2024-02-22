from settings import *
import pygame


class Object(pygame.sprite.Sprite):

    def __init__(self, image, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.name = name
        self.image = image
        self.animate_speed = 3
        self.animation_count = 0

    def display(self, screen, x_offset, y_offset):
        screen.blit(self.image, (self.rect.x - x_offset, self.rect.y - y_offset))


class Block(Object):
    def __init__(self, x, y, image=block_images["Plain grass"], name="block"):
        super().__init__(image, x, y, block_size, block_size, name)


class SpikedBall(Object):
    def __init__(self, x, y, name="trap"):
        image = spiked_ball["Spiked Ball"]
        width, height = image.get_width(), image.get_height()
        super().__init__(image, x, y, width, height, name)


class Spikes(Object):
    def __init__(self, x, y, name="trap"):
        image = spikes
        width, height = image.get_width(), image.get_height()
        super().__init__(image, x, y, width, height, name)


class Platform(Object):
    def __init__(self, x, y, sprite_sheet, start_point, end_point, speed=3,  name="platform"):
        image = spiked_ball["Spiked Ball"]
        width, height = image.get_width(), image.get_height()
        super().__init__(image, x, y, width, height, name)
        self.sprite_sheet = sprite_sheet
        self.start_point = start_point
        self.end_point = end_point
        self.direction = True
        self.speed = speed

    def display(self, screen, x_offset, y_offset):
        if self.direction:
            self.rect.x -= self.speed
        else:
            self.rect.right += self.speed
        if self.rect.x < self.start_point:
            self.direction = False
        elif self.rect.right > self.end_point:
            self.direction = True
        sprite_index = (self.animation_count // self.animate_speed) % len(
            self.sprite_sheet
        )
        self.image = self.sprite_sheet[sprite_index]
        self.animation_count += 1
        super().display(screen, x_offset, y_offset)

class Trophy(Object):
    def __init__(self, x, y, name="trophy"):
        self.sprite_sheets = end_check_point_images
        image = self.sprite_sheets["End (Idle)"][0]
        width, height = image.get_width(), image.get_height()
        super().__init__(image, x, y, width, height, name)
        self.state = "End (Pressed) (64x64)"

    def display(self, screen, x_offset, y_offset):
        sprite_index = (self.animation_count // self.animate_speed) % len(
            self.sprite_sheets[self.state]
        )
        self.image = self.sprite_sheets[self.state][sprite_index]
        self.animation_count += 1
        super().display(screen, x_offset, y_offset)
