import pygame
class pokemon:
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
        self.x +=20

class textBox(pygame.sprite.Sprite):
    def __init__(self, text, x, y):
        super().__init__()
        self.text = text
        self.font = pygame.font.Font(None, 36)

        # Load and scale background
        original_bg = pygame.image.load("textBox.png").convert_alpha()
        self.background = pygame.transform.scale(original_bg, (500, 150))  # Resize to manageable size
        self.rect = self.background.get_rect()
        self.rect.topleft = (x, y-40)

        # Render the text
        self.text_image = self.font.render(self.text, True, (0, 0, 0))

        # Position text relative to the background (padding)
        self.text_pos = (
            x + 20,  # 20 pixels from left of box
            y + 30  # 20 pixels from top of box
        )

    def draw(self, surface):
        surface.blit(self.background, self.rect)         # Draw background first
        surface.blit(self.text_image, self.text_pos)     # Then draw text on top

class Button:
    def __init__(self, image_path, pos):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * 0.4), int(self.rect.height * 0.4)))
    def is_clicked(self, screen, event):
        # Draw the button
        screen.blit(self.image, self.rect)

        # Handle click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

class Player:
    def __init__(self, name, pokemon_list):
        self.name = name
        self.pokemon_list = pokemon_list
        self.current_pokemon = pokemon_list[0] if pokemon_list else None