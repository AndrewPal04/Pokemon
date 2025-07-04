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

#Player Sprites
userNorthIMG=[
    pygame.image.load("userNorth1.png"),
    pygame.image.load("userNorth2.png"),
    pygame.image.load("userNorth3.png"),
    pygame.image.load("userNorth4.png")
    ]
userEastIMG=[
    pygame.image.load("userEast1.png"),
    pygame.image.load("userEast2.png"),
    pygame.image.load("userEast3.png"),
    pygame.image.load("userEast4.png")
    ]
userSouthIMG=[
    pygame.image.load("userSouth1.png"),
    pygame.image.load("userSouth2.png"),
    pygame.image.load("userSouth3.png"),
    pygame.image.load("userSouth4.png")
    ]
userWestIMG=[
    pygame.image.load("userWest1.png"),
    pygame.image.load("userWest2.png"),
    pygame.image.load("userWest3.png"),
    pygame.image.load("userWest4.png")
    ]


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
                    user = Player("Ryott", userNorthIMG, userSouthIMG, userEastIMG, userWestIMG, 250, 250, 4, 5)
                else:
                    user = Player.from_dict(data, userNorthIMG, userSouthIMG, userEastIMG, userWestIMG)

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
if newPlayer:
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
                running=False
            if starter2.is_clicked(event):
                starter="Aquabble"
                running=False
            if starter3.is_clicked(event):
                starter="Sproutuft"
                running=False

        pygame.display.update()
        clock.tick(60)

#Starter Pymon
Tackle= move("Tackle", "Normal", 40, 100, 0)
Flame_Shot= move("Flame Shot", "Fire", 50, 100, 0)
Water_Pierce= move("Water Pierce", "Water", 45, 100, 0)
Leaf_Slash= move("Leaf Slash", "Grass", 55, 100, 0)

# Create starter Pymon

Pyrazzle=Pymon("Pyrazzle", 5, 39,"Fire",None, [Tackle, Flame_Shot])
Aquabble=Pymon("Aquabble", 5, 44, "Water",None, [Tackle, Water_Pierce])
Sproutuft=Pymon("Sproutuft", 5, 45, "Grass", None, [Tackle, Leaf_Slash])

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
    room=sprite(roomIMG, 0, 0, 1)
    user.speed=5
    user.scale=4
    user.update_image()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill((0,0,0))
        room.draw(screen)
        #Add player update/sprite here
        user.draw(screen)
        user.update()
        #Player Boundaries
        #Bed
        bed_rect=pygame.Rect(0, 100, 150, 250)
        if user.rect.colliderect(bed_rect):
            if user.rect.left < bed_rect.right and user.rect.right > bed_rect.right:
                user.rect.left = bed_rect.right
            if user.rect.top < bed_rect.bottom and user.rect.bottom > bed_rect.bottom:
                user.rect.top = bed_rect.bottom
        #Desk
        desk_rect=pygame.Rect(200, 150, 200, 100)
        if user.rect.colliderect(desk_rect):
            if user.rect.left < desk_rect.right and user.rect.right > desk_rect.right:
                user.rect.left = desk_rect.right
            if user.rect.top < desk_rect.bottom and user.rect.bottom > desk_rect.bottom:
                user.rect.top = desk_rect.bottom
        #Cabinet
        cabinet_rect=pygame.Rect(500, 150, 100, 100)
        if user.rect.colliderect(cabinet_rect):
            if user.rect.left < cabinet_rect.right and user.rect.right > cabinet_rect.right:
                user.rect.left = cabinet_rect.right
            if user.rect.top < cabinet_rect.bottom and user.rect.bottom > cabinet_rect.bottom:
                user.rect.top = cabinet_rect.bottom
        #Bookshelf
        bookshelf_rect=pygame.Rect(1000, 150, 150, 100)
        if user.rect.colliderect(bookshelf_rect):
            if user.rect.top < bookshelf_rect.bottom and user.rect.bottom > bookshelf_rect.bottom:
                user.rect.top = bookshelf_rect.bottom
            if user.rect.left < bookshelf_rect.right and user.rect.right > bookshelf_rect.right:
                user.rect.left = bookshelf_rect.right
            if user.rect.right > bookshelf_rect.left and user.rect.left < bookshelf_rect.left:
                user.rect.right = bookshelf_rect.left
        #Walls
        if user.rect.top < 100:
            user.rect.top = 100
        if user.rect.bottom > 900 and user.rect.left>700 or user.rect.bottom >900 and user.rect.right < 700:
            user.rect.bottom = 900
        #Exit
        exit_rect=pygame.Rect(580, 900, 150, 100)
        if user.rect.colliderect(exit_rect):
            screen.fill((255,255,255))
            pygame.display.update()
            pygame.time.delay(500)
            home_city("home")
            break
        pygame.display.update()
        clock.tick(60)
    
def home_city(from_location):
    home_cityIMG=pygame.image.load("home_city.png")
    home_city=sprite(home_cityIMG, 0, 0, 1)
    user.scale=2
    user.update_image()
    user.speed=5
    if from_location=="home":
        user.rect.x=390
        user.rect.y=750
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        home_city.draw(screen)
        user.draw(screen)
        user.update()
        
        house_rect=pygame.Rect(350, 550, 250, 150)
        if user.rect.colliderect(house_rect):
            if user.rect.left < house_rect.right and user.rect.right > house_rect.right:
                user.rect.left = house_rect.right
            if user.rect.top < house_rect.bottom and user.rect.bottom > house_rect.bottom:
                user.rect.top = house_rect.bottom
            if user.rect.right > house_rect.left and user.rect.left < house_rect.left:
                user.rect.right = house_rect.left
            if user.rect.bottom > house_rect.top and user.rect.top < house_rect.top:
                user.rect.bottom = house_rect.top
        
        house2=pygame.Rect(660,370,250,150)
        if user.rect.colliderect(house2):
            if user.rect.left < house2.right and user.rect.right > house2.right:
                user.rect.left = house2.right
            if user.rect.top < house2.bottom and user.rect.bottom > house2.bottom:
                user.rect.top = house2.bottom
            if user.rect.right > house2.left and user.rect.left < house2.left:
                user.rect.right = house2.left
            if user.rect.bottom > house2.top and user.rect.top < house2.top:
                user.rect.bottom = house2.top
        
        house3=pygame.Rect(650, 50, 250, 150)
        if user.rect.colliderect(house3):
            if user.rect.left < house3.right and user.rect.right > house3.right:
                user.rect.left = house3.right
            if user.rect.top < house3.bottom and user.rect.bottom > house3.bottom:
                user.rect.top = house3.bottom
            if user.rect.right > house3.left and user.rect.left < house3.left:
                user.rect.right = house3.left
            if user.rect.bottom > house3.top and user.rect.top < house3.top:
                user.rect.bottom = house3.top

        print(user.rect.x, user.rect.y)
        tree_polygon=pygame.polygon([(0, 0), (1500, 0), (1500, 100), (0, 100)])#Edit this to create polygon around trees

        pygame.display.update()
        clock.tick(60)
    
   
    
def route_1():#Left of home city
    pass

home()