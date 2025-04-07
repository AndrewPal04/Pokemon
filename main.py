import pygame
from classes import sprite
from classes import textBox
from classes import Button
import json

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
running=True
while running:
    screen.fill((0, 150, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            pygame.quit()

        # Detect left mouse button click to move to next text
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if current_box < len(textBoxes) - 1:
                current_box += 1
            else:
                current_box = None
                running=False
    # Draw professor
    professor.draw(screen)

    # Draw current text box
    if current_box is not None:
        textBoxes[current_box].draw(screen)

    pygame.display.update()
    clock.tick(60)

#Save slot buttons
save_slot1 = Button("save1_img.png", 500, 100)
save_slot2 = Button("save2_img.png", 500, 200)
save_slot3 = Button("save3_img.png", 500, 300)
# Loop for save slots
running = True
while running:
    screen.fill((50, 50, 50))
    save_slot1.draw(screen)
    save_slot2.draw(screen)
    save_slot3.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if save_slot1.is_clicked(screen, event):
        f=open("saveSlot1.json")
        data=json.load(f)
        if not data:
            pass
        else:
            player=json.load(f)
            running=False
    if save_slot2.is_clicked(screen, event):
        f=open("saveSlot2.json")
        data=json.load(f)
        if not data:
            pass
        else:
            player=json.load(f)
            running=False
    if save_slot3.is_clicked(screen, event):
        f=open("saveSlot3.json")
        data=json.load(f)
        if not data:
            pass
        else:
            player=json.load(f)
            running=False
    pygame.display.update()
    clock.tick(60)

print(player)
pygame.quit()
