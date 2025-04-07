import pygame
from classes import sprite
from classes import textBox

# Pygame setup
screenWidth, screenHeight = 1000, 500
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

# Professor Sprite
prof_img = pygame.image.load("professor.png")
professor = sprite(prof_img, 50, 100, 0.3)

# Text Boxes
textBoxes = [
    textBox("Hello, welcome to the world of Pymon!", 350, 350),
    textBox("I am your guide, Professor Cirus.", 350, 350),
    textBox("Let's begin your journey!", 350, 350)
]
current_box = 0

# Introduction loop
running = True
while running:
    screen.fill((0, 150, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect left mouse button click to move to next text
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if current_box < len(textBoxes) - 1:
                current_box += 1
            else:
                current_box = None  # End of dialogue

    # Draw professor
    professor.draw(screen)

    # Draw current text box
    if current_box is not None:
        textBoxes[current_box].draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
