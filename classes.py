import pygame
import json

class Pymon:
    def __init__(self, name, level, health, type1, type2, moves):
        self.name = name
        self.level = level
        self.type1 = type1
        self.type2 = type2
        self.health = health
        self.moves = moves
    def lvlUp(self):
        self.level +=1
        print(self.name,"leveled up to level",str(self.level)+"!")
    def fight_intro(self):
        print("You sent out",str(self.name)+"!")
    def retreat(self):
        print("You brought back",str(self.name)+"!")
    def to_dict(self):
        return {
            "name": self.name,
            "level": self.level,
            "health": self.health,
            "type1": self.type1,
            "type2": self.type2,
            "moves": [m.to_dict() for m in self.moves]
        }
    @staticmethod
    def from_dict(data):
        return Pymon(
            name=data["name"],
            level=data["level"],
            health=data["health"],
            type1=data["type1"],
            type2=data["type2"],
            moves=[move.from_dict(m) for m in data["moves"]]
        )


class move:
    def __init__(self, name, type, damage, pp, effects):
        self.name = name
        self.type = type
        self.damage = damage
        self.pp = pp
        self.effects = effects
    def use(self,enemy):
        print("You used",str(self.name)+"!")
        if self.damage>0:
            print("It dealt",str(self.damage)+" damage to",str(enemy.name)+"!")
            enemy.health -= self.damage
    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "damage": self.damage,
            "pp": self.pp,
            "effects": self.effects
        }

    @staticmethod
    def from_dict(data):
        return move(
            name=data["name"],
            type=data["type"],
            damage=data["damage"],
            pp=data["pp"],
            effects=data["effects"]
        )


class sprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, scale):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * scale), int(self.rect.height * scale)))
    def draw(self, surface):
        surface.blit(self.image, self.rect)  # Draw the sprite on the surface
    def update(self):
        self.rect.x +=20

class textBox(pygame.sprite.Sprite):
    def __init__(self, text, x, y, scale=1.7):
        super().__init__()
        self.text = text
        base_font_size = 36
        font_size = int(base_font_size * scale)
        self.font = pygame.font.Font(None, font_size)

        # Load and scale background
        original_bg = pygame.image.load("textBox.png").convert_alpha()
        base_bg_width, base_bg_height = 500, 150
        scaled_width = int(base_bg_width * scale)
        scaled_height = int(base_bg_height * scale)
        self.background = pygame.transform.scale(original_bg, (scaled_width, scaled_height))
        self.rect = self.background.get_rect()
        self.rect.topleft = (x, y - int(40 * scale))  # Offset based on scale

        # Render the text
        self.text_image = self.font.render(self.text, True, (0, 0, 0))

        # Position text relative to the scaled background
        self.text_pos = (
            x + int(20 * scale),  # left padding
            y + int(30 * scale)   # top padding
        )

    def draw(self, surface):
        surface.blit(self.background, self.rect)
        surface.blit(self.text_image, self.text_pos)


class Button:
    def __init__(self, image_path, pos, scale=1.0, hover_scale=1.1):
        # Load the image
        original = pygame.image.load(image_path).convert_alpha()

        # Scale the image right away if needed
        if scale != 1.0:
            width, height = original.get_size()
            original = pygame.transform.scale(original, (int(width * scale), int(height * scale)))

        self.original_image = original
        self.image = self.original_image
        self.original_size = self.original_image.get_size()

        self.rect = self.image.get_rect(topleft=pos)
        self.pos = pos
        self.hovered = False
        self.hover_scale = hover_scale

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if not self.hovered:
                self.hovered = True
                width, height = self.original_size
                scaled_image = pygame.transform.scale(
                    self.original_image,
                    (int(width * self.hover_scale), int(height * self.hover_scale))
                )
                center = self.rect.center
                self.image = scaled_image
                self.rect = self.image.get_rect(center=center)
        else:
            if self.hovered:
                self.hovered = False
                self.image = self.original_image
                self.rect = self.image.get_rect(topleft=self.pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

class Player(pygame.sprite.Sprite):
    def __init__(self, name, north_images, south_images, east_images, west_images, x, y, scale, speed):
        super().__init__()
        self.name = name
        self.speed=speed
        self.north_images = north_images
        self.south_images = south_images
        self.east_images = east_images
        self.west_images = west_images

        self.direction = "south"
        self.current_frame = 0
        self.frame_timer = 0
        self.frame_delay = 5  # Frames before advancing animation

        # Scale first frame image
        self.image = self.south_images[0]
        width, height = self.image.get_size()
        self.scale = scale
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.pymon_list = []

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def catch_pymon(self, new_pymon):
        self.pymon_list.append(new_pymon)
        print(f"{self.name} acquired a new Pymon: {new_pymon.name}!")

    def update(self):
        keystate = pygame.key.get_pressed()
        moved = False

        if keystate[pygame.K_UP]:
            self.rect.y -= self.speed
            self.direction = "north"
            moved = True
        elif keystate[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.direction = "south"
            moved = True
        elif keystate[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.direction = "west"
            moved = True
        elif keystate[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.direction = "east"
            moved = True
        
        #On screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1500:
            self.rect.right = 1500
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 1000:
            self.rect.bottom = 1000

        if moved:
            self.frame_timer += 1
            if self.frame_timer >= self.frame_delay:
                self.current_frame = (self.current_frame + 1) % 4
                self.update_image()
                self.frame_timer = 0
        else:
            self.current_frame = 0
            self.update_image()

    def update_image(self):
        if self.direction == "north":
            img = self.north_images[self.current_frame]
        elif self.direction == "south":
            img = self.south_images[self.current_frame]
        elif self.direction == "east":
            img = self.east_images[self.current_frame]
        elif self.direction == "west":
            img = self.west_images[self.current_frame]
        else:
            img = self.south_images[0]

        original_width, original_height = img.get_size()
        scaled_width = int(original_width * self.scale)
        scaled_height = int(original_height * self.scale)

        self.image = pygame.transform.scale(img, (scaled_width, scaled_height))

        center=self.rect.center
        self.rect=self.image.get_rect(center=center)

    def to_dict(self):
        return {
            "name": self.name,
            "x": self.rect.x,
            "y": self.rect.y,
            "scale": self.scale,
            "speed": self.speed,  # add this line
            "pymon_list": [p.to_dict() for p in self.pymon_list]
        }

    @classmethod
    def from_dict(cls, data, north_images, south_images, east_images, west_images):
        name = data.get("name", "DefaultName")
        x = data.get("x", 750)
        y = data.get("y", 700)
        scale = data.get("scale", 0.4)
        speed = data.get("speed", 5)  # Default if missing

        player = cls(name, north_images, south_images, east_images, west_images, x, y, scale, speed)
        player.pymon_list = [Pymon.from_dict(p) for p in data.get("pymon_list", [])]
        return player
