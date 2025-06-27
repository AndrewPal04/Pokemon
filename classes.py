import pygame
import json

class Pymon:
    def __init__(self, name, level, health, type1, type2, move1, move2, move3, move4):
        self.name = name
        self.level = level
        self.type1 = type1
        self.type2 = type2
        self.health = health
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
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
            "move1": self.move1.to_dict(),
            "move2": self.move2.to_dict(),
            "move3": self.move3.to_dict(),
            "move4": self.move4.to_dict()
        }

    @staticmethod
    def from_dict(data):
        return Pymon(
            name=data["name"],
            level=data["level"],
            health=data["health"],
            type1=data["type1"],
            type2=data["type2"],
            move1=move.from_dict(data["move1"]),
            move2=move.from_dict(data["move2"]),
            move3=move.from_dict(data["move3"]),
            move4=move.from_dict(data["move4"])
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

class Player:
    def __init__(self, name):
        self.name = name
        self.pymon_list = []
    def catch_pymon(self, new_pymon):
        self.pymon_list.append(new_pymon)
        print(f"{self.name} aquired a new Pymon: {new_pymon.name}!")
    def to_dict(self):
        return {
            "name":self.name,
            "pymon_list":[p.to_dict() for p in self.pymon_list]
        }
    @staticmethod
    def from_dict(data):
        player=Player(data["name"])
        for p in data["pymon_list"]:
            player.catch_pymon(Pymon.from_dict(p))
        return player