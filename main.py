import pygame
from classes import sprite
from classes import textBox
from classes import Button
import json
import time

# Pygame setup
screenWidth, screenHeight = 1500, 1000
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

# Professor Sprite
prof_img = pygame.image.load("professor.png")
professor = sprite(prof_img, 50, 100, 0.7)

# Text Boxes
textBoxes = [
    textBox("Hello, welcome to the world of Pymon!", 500, 500, scale = 1.7),
    textBox("I am your guide, Professor Cirus.", 500, 500, scale = 1.7),
    textBox("Let's begin your journey!", 500, 500, scale = 1.7)
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
# Save slot buttons
save_slot1 = Button("save1_img.png", (450, -150),scale=0.6)
save_slot2 = Button("save2_img.png", (450, 200), scale=0.6)
save_slot3 = Button("save3_img.png", (450, 550), scale=0.6)
player = {}
newPlayer = False

save_buttons = [save_slot1, save_slot2, save_slot3]
save_files = ["saveSlot1.json", "saveSlot2.json", "saveSlot3.json"]

# Loop for save slots
running = True
while running:
    screen.fill((50, 50, 50))
    # Update & draw buttons
    for button in save_buttons:
        button.update()
        button.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        for i, button in enumerate(save_buttons):
            if button.is_clicked(event):
                with open(save_files[i]) as f:
                    data = json.load(f)
                if data == {}:
                    newPlayer = True
                else:
                    player = data
                running = False  # Exit after selection

    pygame.display.update()
    clock.tick(60)

textBoxes = [
    textBox("Oh, you haven't been given a Pymon?",500, 500, scale = 1.7),
    textBox("...Well lucky for you I have a suprise.",500, 500, scale = 1.7),
    textBox("Your first Pymon!",500, 500, scale = 1.7)
]
current_box = 0
running=True
if newPlayer:  # Finish of introduction
    while running:
        screen.fill((50, 50, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_box < len(textBoxes) - 1:
                    current_box += 1
                else:
                    current_box = None
                    running = False

        # Draw professor
        professor.draw(screen)

        # Draw current text box
        if current_box is not None:
            textBoxes[current_box].draw(screen)

        pygame.display.update()
        clock.tick(60)

#Starters
# Create individual buttons
starter1 = Button("pyrazzle.png", (150, 200), scale=0.4)
starter2 = Button("aquabble.png", (550, 200), scale=0.4)
starter3 = Button("sproutuft.png", (950, 200), scale=0.4)

running = True
while running:
    screen.fill((50, 50, 50))

    # Update and draw each button
    starter1.update()
    starter1.draw(screen)

    starter2.update()
    starter2.draw(screen)

    starter3.update()
    starter3.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if starter1.is_clicked(event):
            print("Starter 1 (Pyrazzle) clicked!")
        if starter2.is_clicked(event):
            print("Starter 2 (Aquabble) clicked!")
        if starter3.is_clicked(event):
            print("Starter 3 (Sproutuft) clicked!")

    pygame.display.update()
    clock.tick(60)

