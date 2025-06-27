import pygame
from classes import sprite, textBox, Button, Player, Pymon, move
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

newPlayer = False
selected_slot_index = None

save_buttons = [save_slot1, save_slot2, save_slot3]
save_files = ["saveSlot1.json", "saveSlot2.json", "saveSlot3.json"]
player = None

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
                selected_slot_index = i
                try:
                    with open(save_files[i]) as f:
                        data = json.load(f)
                except (FileNotFoundError, json.JSONDecodeError):
                    data = {}

                if data == {}:
                    newPlayer = True
                    user = Player("Ryott")
                else:
                    user = Player.from_dict(data)

                running = False

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

pymon=[]
starter=None
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
            starter="Pyrazzle"
        if starter2.is_clicked(event):
            starter="Aquabble"
        if starter3.is_clicked(event):
            starter="Sproutuft"

    pygame.display.update()
    clock.tick(60)

#Starter Pymon
Tackle= move("Tackle", "Normal", 40, 100, 0)
Flame_Shot= move("Flame Shot", "Fire", 50, 100, 0)
Water_Pierce= move("Water Pierce", "Water", 45, 100, 0)
Leaf_Slash= move("Leaf Slash", "Grass", 55, 100, 0)

# Create starter Pymon

Pyrazzle=Pymon("Pyrazzle", 5, "Fire", 39, 52, 43, 65, 50, 60, [Tackle, Flame_Shot])
Aquabble=Pymon("Aquabble", 5, "Water", 44, 48, 65, 43, 50, 64, [Tackle, Water_Pierce])
Sproutuft=Pymon("Sproutuft", 5, "Grass", 45, 49, 49, 65, 65, 45, [Tackle, Leaf_Slash])

#Assign Starter
if starter=="Pyrazzle":
    user.catch_pymon(Pyrazzle)
elif starter=="Aquabble":
    user.catch_pymon(Aquabble)
elif starter=="Sproutuft":
    user.catch_pymon(Sproutuft)

# Save the player data to the selected slot
if selected_slot_index is not None:
    with open(save_files[selected_slot_index], 'w') as f:
        json.dump(user.to_dict(), f, indent=4)

def home():
    roomIMG=pygame.image.load("home_room.png")
    room=sprite(roomIMG, 0, 0, 1.0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        room.draw(screen)
        #Add player update/sprite here


        pygame.display.update()
        clock.tick(60)
def home_city():
    pass
def route_1():
    pass
