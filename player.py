import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, sprites):
        super().__init__()
        self.sprites = sprites
        self.jump_count = 0
        self.animation_count = 0
        self.sprite = self.sprites["idle_left"][0]
        self.rect = self.sprite.get_rect(topleft=(x, y))
        self.direction = "left"
        self.x_vel = 0
        self.y_vel = 0
        self.hit = False
        self.hit_count = 0
        self.animate_speed = 3
        self.sprite_sheet = "idle"
        self.gravity = 1
        self.fall_count = 0
        self.speed = 5

    def display(self, screen, x_offset, y_offset):
        if self.hit:
            x_offset, y_offset = 0, 0
        self.update_sprite()
        screen.blit(self.sprite, (self.rect.x - x_offset, self.rect.y - y_offset))
        return x_offset, y_offset

    def update_sprite(self):
        self.sprite_sheet = "idle"
        if self.hit:
            self.sprite_sheet = "hit"
        elif self.y_vel < 0:
            if self.jump_count == 1:
                self.sprite_sheet = "jump"
            elif self.jump_count == 2:
                self.sprite_sheet = "double_jump"
        elif self.y_vel > self.gravity * 2:
            self.sprite_sheet = "fall"
        elif self.x_vel != 0:
            self.sprite_sheet = "run"
        sprite_sheet_name = self.sprite_sheet + "_" + self.direction
        sprites = self.sprites[sprite_sheet_name]
        sprite_index = (self.animation_count // self.animate_speed) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))

    def landed(self, obj):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0
        self.rect.bottom = obj.rect.top

    def hit_head(self, obj):
        self.y_vel = 0
        self.rect.top = obj.rect.bottom

    def is_hit(self):
        self.hit = True
        self.hit_count = 0
        self.rect.x, self.rect.y = 100, 100

    def move(self, dx, dy, objects):
        self.rect.y += dy
        for obj in objects:
            if self.rect.colliderect(obj.rect):
                if dy > 0:
                    self.landed(obj)
                else:
                    self.hit_head(obj)
                if obj.name == "trap":
                    self.is_hit()
                elif obj.name == "trophy":
                    return True
        self.rect.x += dx
        for obj in objects:
            if self.rect.colliderect(obj.rect):
                if dx > 0:
                    self.rect.right = obj.rect.left
                else:
                    self.rect.left = obj.rect.right
                if obj.name == "trap":
                    self.is_hit()
                elif obj.name == "trophy":
                    return True

    def move_left(self, vel):
        self.x_vel += -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def jump(self):
        if self.jump_count < 2:
            self.y_vel = -self.gravity * 8
            self.jump_count += 1
            self.animation_count = 0
        if self.jump_count == 1:
            self.fall_count = 0

    def controls(self):
        keys = pygame.key.get_pressed()
        self.x_vel = 0
        if keys[pygame.K_d]:
            self.move_right(self.speed)
        if keys[pygame.K_a]:
            self.move_left(self.speed)

    def event_controls(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.jump()

    def script(self, fps, objects):
        if self.hit:
            self.hit_count += 1
        if self.hit_count >= fps // 2:
            self.hit = False

        self.y_vel += min(1, (self.fall_count / fps) * self.gravity)
        if self.move(self.x_vel, self.y_vel, objects):
            return True
        if self.rect.y > 1000:
            self.is_hit()
        self.fall_count += 1
        self.controls()
