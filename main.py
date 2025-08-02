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
    user.location = "home"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if selected_slot_index is not None:
                    user.location= "home"
                    data=user.to_dict()
                    data['x'] = user.rect.x
                    data['y'] = user.rect.y
                    with open(save_files[selected_slot_index], 'w') as f:
                        json.dump(data, f, indent=4)
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
    pygame.mixer.music.load("home_city.mp3")
    pygame.mixer.music.play(-1)
    home_cityIMG=pygame.image.load("home_city.png")
    home_city=sprite(home_cityIMG, 0, 0, 1)
    user.scale=2
    user.update_image()
    user.speed=5
    user.location = "home_city"
    if from_location=="home":
        user.rect.x=390
        user.rect.y=780
    elif from_location=="route_1":
        user.rect.x=100
        user.rect.y=450
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if selected_slot_index is not None:
                    user.location= "home_city"
                    data=user.to_dict()
                    data['x'] = user.rect.x
                    data['y'] = user.rect.y
                    with open(save_files[selected_slot_index], 'w') as f:
                        json.dump(data, f, indent=4)
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

        tree_rect1=pygame.Rect(0, 0, 1500, 100)#Top trees
        if user.rect.colliderect(tree_rect1):
            if user.rect.left < tree_rect1.right and user.rect.right > tree_rect1.right:
                user.rect.left = tree_rect1.right
            if user.rect.top < tree_rect1.bottom and user.rect.bottom > tree_rect1.bottom:
                user.rect.top = tree_rect1.bottom
            if user.rect.right > tree_rect1.left and user.rect.left < tree_rect1.left:
                user.rect.right = tree_rect1.left
            if user.rect.bottom > tree_rect1.top and user.rect.top < tree_rect1.top:
                user.rect.bottom = tree_rect1.top
        
        tree_rect2=pygame.Rect(0, 0, 200, 350)#Top left tree
        if user.rect.colliderect(tree_rect2):
            if user.rect.top  < tree_rect2.bottom and user.rect.bottom > tree_rect2.bottom:
                user.rect.top = tree_rect2.bottom
            if user.rect.left < tree_rect2.right and user.rect.right > tree_rect2.right:
                user.rect.left = tree_rect2.right
            if user.rect.right > tree_rect2.left and user.rect.left < tree_rect2.left:
                user.rect.right = tree_rect2.left

        tree_rect3=pygame.Rect(1300, 0, 200, 350)#Top right tree
        if user.rect.colliderect(tree_rect3):
            if user.rect.top < tree_rect3.bottom and user.rect.bottom > tree_rect3.bottom:
                user.rect.top = tree_rect3.bottom 
            if user.rect.left < tree_rect3.right and user.rect.right > tree_rect3.right:
                user.rect.left = tree_rect3.right
            if user.rect.right > tree_rect3.left and user.rect.left < tree_rect3.left:
                user.rect.right = tree_rect3.left

        tree_rect4=pygame.Rect(0, 650, 100, 350)#Bottom left trees vertical
        if user.rect.colliderect(tree_rect4):
            if user.rect.top < tree_rect4.bottom and user.rect.bottom > tree_rect4.bottom:
                user.rect.top = tree_rect4.bottom
            if user.rect.left < tree_rect4.right and user.rect.right > tree_rect4.right:
                user.rect.left = tree_rect4.right
            if user.rect.right > tree_rect4.left and user.rect.left < tree_rect4.left:
                user.rect.right = tree_rect4.left
            if user.rect.bottom > tree_rect4.top and user.rect.top < tree_rect4.top:
                user.rect.bottom = tree_rect4.top

        tree_rect5=pygame.Rect(0, 900, 300, 100)#Bottom left trees horizontal
        if user.rect.colliderect(tree_rect5):
            if user.rect.top < tree_rect5.bottom and user.rect.bottom > tree_rect5.bottom:
                user.rect.top = tree_rect5.bottom
            if user.rect.left < tree_rect5.right and user.rect.right > tree_rect5.right:
                user.rect.left = tree_rect5.right
            if user.rect.right > tree_rect5.left and user.rect.left < tree_rect5.left:
                user.rect.right = tree_rect5.left
            if user.rect.bottom > tree_rect5.top and user.rect.top < tree_rect5.top:
                user.rect.bottom = tree_rect5.top
        tree_rect6=pygame.Rect(1400, 600, 100, 400)#Bottom right trees
        if user.rect.colliderect(tree_rect6):
            if user.rect.top < tree_rect6.bottom and user.rect.bottom > tree_rect6.bottom:
                user.rect.top = tree_rect6.bottom
            if user.rect.left < tree_rect6.right and user.rect.right > tree_rect6.right:
                user.rect.left = tree_rect6.right
            if user.rect.right > tree_rect6.left and user.rect.left < tree_rect6.left:
                user.rect.right = tree_rect6.left
            if user.rect.bottom > tree_rect6.top and user.rect.top < tree_rect6.top:
                user.rect.bottom = tree_rect6.top
        
        if user.rect.left <20 and user.rect.top > 350 and user.rect.bottom < 550:
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                pygame.mixer.music.stop()
                screen.fill((255,255,255))
                pygame.display.update()
                pygame.time.delay(500)
                route_1("home_city")

        if user.rect.x > 355 and user.rect.x < 420 and user.rect.y < 701 and user.rect.y >550:
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_UP]:
                pygame.mixer.music.stop()
                screen.fill((255,255,255))
                pygame.display.update()
                pygame.time.delay(500)
                home()

        pygame.display.update()
        clock.tick(60)
    
   
    
def route_1(from_location):#Left of home city
    route_1IMG=pygame.image.load("route_1.png")
    route_1=sprite(route_1IMG, 0, 0, 1)
    user.scale=2
    user.update_image()
    user.speed=5
    user.location = "route_1"
    if from_location=="home_city":
        user.rect.x=1300
        user.rect.y=700
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if selected_slot_index is not None:
                    user.location= "route_1"
                    data=user.to_dict()
                    data['x'] = user.rect.x
                    data['y'] = user.rect.y
                    with open(save_files[selected_slot_index], 'w') as f:
                        json.dump(data, f, indent=4)
                pygame.quit()
                quit()
        route_1.draw(screen)
        user.draw(screen)
        user.update()
        print(user.rect.x, user.rect.y)
        #Player Boundaries


        if user.rect.right > 1470 and user.rect.top > 650 and user.rect.bottom < 800:
            screen.fill((255,255,255))
            pygame.display.update()
            pygame.time.delay(500)
            home_city("route_1")

        pygame.display.update()
        clock.tick(60)
pygame.mixer.init()
if newPlayer and user.location is None:
    user.location = "home"
if user.location == "home":
    home()
elif user.location == "home_city":
    home_city("none")
elif user.location == "route_1":
    route_1("none")