import pygame
from pygame_tools import load_sprite_sheets, load_assets, load_sprite_sheet
from pygame.image import load

window_width, window_height = 900, 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Jumper Man")
pygame.display.set_icon(load("assets\Traps\Saw\off.png"))


main_characters = {
    "VirtualGuy": load_sprite_sheets("assets\MainCharacters\VirtualGuy", 32, 32),
    "PinkMan": load_sprite_sheets("assets\MainCharacters\PinkMan", 32, 32),
    "NinjaFrog": load_sprite_sheets("assets\MainCharacters/NinjaFrog", 32, 32),
    "MaskDude": load_sprite_sheets("assets\MainCharacters\MaskDude", 32, 32),
}

button_size = 64
menu_button_images = load_assets("assets\Menu\Buttons", (button_size, button_size))

block_size = 96
block_images = load_assets("assets\Terrain", (block_size, block_size))

fan_images = load_sprite_sheets("assets/Traps/Fan", 24, 8, False, (16, 48))
platform_images = load_sprite_sheets("assets/Traps/Platforms", 32, 8, False)
spiked_ball = load_assets("assets/Traps/Spiked Ball", (64, 64))
spikes = pygame.transform.scale(load("assets/Traps/Spikes/Idle.png"), (32, 32))
spike_size = 32
spiked_ball_size = 64
platform_size = 32, 8

background_tile_size = 64
current_background_tile = "Blue"
background_images = load_assets("assets/Background")

appearing_sprites = load_sprite_sheet("MainCharacters/Appearing (96x96).png", 96, 96, (64, 64), False)

start_check_point_images = load_sprite_sheets("assets/Items/Checkpoints/Start", 64, 64, False)
end_check_point_images = load_sprite_sheets("assets/Items/Checkpoints/End", 64, 64, False)
check_point_size = 64
