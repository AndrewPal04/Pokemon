import pygame
from classes import sprite, textBox, Button, Player, Pymon, move
import json
import time

screenWidth, screenHeight = 1500, 1000
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

prof_img = pygame.image.load("professor.png")
professor = sprite(prof_img, 50, 100, 0.7)

textBoxes = [
    textBox("Hello, welcome to the world of Pymon!", 500, 500, scale=1.7),
    textBox("I am your guide, Professor Cirus.", 500, 500, scale=1.7),
    textBox("Let's begin your journey!", 500, 500, scale=1.7)
]
current_box = 0

def obstacle(user, obstacle):
    a = user.rect
    b = obstacle
    overlap_left = a.right - b.left
    overlap_right = b.right - a.left
    overlap_top = a.bottom - b.top
    overlap_bottom = b.bottom - a.top
    min_x = overlap_left if overlap_left < overlap_right else overlap_right
    min_y = overlap_top if overlap_top < overlap_bottom else overlap_bottom
    if min_x < min_y:
        if overlap_left < overlap_right:
            a.right = b.left
        else:
            a.left = b.right
    else:
        if overlap_top < overlap_bottom:
            a.bottom = b.top
        else:
            a.top = b.bottom

running = True
while running:
    screen.fill((0, 150, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if current_box < len(textBoxes) - 1:
                current_box += 1
            else:
                running = False
    professor.draw(screen)
    textBoxes[current_box].draw(screen)
    pygame.display.update()
    clock.tick(60)

save_slot1 = Button("save1_img.png", (450, -150), scale=0.6)
save_slot2 = Button("save2_img.png", (450, 200), scale=0.6)
save_slot3 = Button("save3_img.png", (450, 550), scale=0.6)

save_buttons = [save_slot1, save_slot2, save_slot3]
save_files = ["saveSlot1.json", "saveSlot2.json", "saveSlot3.json"]

userNorthIMG = [pygame.image.load(f"userNorth{i}.png") for i in range(1, 5)]
userSouthIMG = [pygame.image.load(f"userSouth{i}.png") for i in range(1, 5)]
userEastIMG = [pygame.image.load(f"userEast{i}.png") for i in range(1, 5)]
userWestIMG = [pygame.image.load(f"userWest{i}.png") for i in range(1, 5)]

newPlayer = False
selected_slot_index = None

running = True
while running:
    screen.fill((50, 50, 50))
    for b in save_buttons:
        b.update()
        b.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        for i, b in enumerate(save_buttons):
            if b.is_clicked(event):
                selected_slot_index = i
                try:
                    with open(save_files[i]) as f:
                        data = json.load(f)
                except:
                    data = {}
                if data == {}:
                    newPlayer = True
                    user = Player("Ryott", userNorthIMG, userSouthIMG, userEastIMG, userWestIMG, 250, 250, 4, 5)
                else:
                    user = Player.from_dict(data, userNorthIMG, userSouthIMG, userEastIMG, userWestIMG)
                running = False
    pygame.display.update()
    clock.tick(60)

def home():
    room = sprite(pygame.image.load("home_room.png"), 0, 0, 1)
    user.scale = 4
    user.speed = 5
    user.update_image()
    user.location = "home"

    obstacles = [
        pygame.Rect(0, 100, 150, 250),
        pygame.Rect(200, 150, 200, 100),
        pygame.Rect(500, 150, 100, 100),
        pygame.Rect(1000, 150, 150, 100),
        pygame.Rect(0, 0, 1500, 100),
        pygame.Rect(0, 900, 700, 100),
        pygame.Rect(700, 900, 800, 100)
    ]

    exit_rect = pygame.Rect(580, 900, 150, 100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill((0, 0, 0))
        room.draw(screen)
        user.update()
        user.draw(screen)
        for o in obstacles:
            if user.rect.colliderect(o):
                obstacle(user, o)
        if user.rect.colliderect(exit_rect):
            pygame.display.update()
            pygame.time.delay(500)
            home_city("home")
            break
        pygame.display.update()
        clock.tick(60)

def home_city(from_location):
    city = sprite(pygame.image.load("home_city.png"), 0, 0, 1)
    user.scale = 2
    user.speed = 5
    user.update_image()
    user.location = "home_city"

    if from_location == "home":
        user.rect.topleft = (390, 780)
    elif from_location == "route_1":
        user.rect.topleft = (100, 450)

    obstacles = [
        pygame.Rect(350, 550, 250, 150),
        pygame.Rect(660, 370, 250, 150),
        pygame.Rect(650, 50, 250, 150),
        pygame.Rect(0, 0, 1500, 100),
        pygame.Rect(0, 0, 200, 350),
        pygame.Rect(1300, 0, 200, 350),
        pygame.Rect(0, 650, 100, 350),
        pygame.Rect(0, 900, 300, 100),
        pygame.Rect(1400, 600, 100, 400)
    ]

    exit_route1 = pygame.Rect(0, 350, 20, 200)
    exit_home = pygame.Rect(355, 550, 65, 150)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        city.draw(screen)
        user.update()
        user.draw(screen)

        keystate = pygame.key.get_pressed()

        if user.rect.colliderect(exit_route1) and (keystate[pygame.K_LEFT] or keystate[pygame.K_a]):
            pygame.display.update()
            pygame.time.delay(300)
            route_1("home_city")
            return

        if user.rect.colliderect(exit_home) and (keystate[pygame.K_UP] or keystate[pygame.K_w]):
            pygame.display.update()
            pygame.time.delay(300)
            home()
            return

        for o in obstacles:
            if user.rect.colliderect(o):
                obstacle(user, o)

        
        pygame.display.update()
        clock.tick(60)

def route_1(from_location):
    route = sprite(pygame.image.load("route_1.png"), 0, 0, 1)
    user.scale = 2
    user.speed = 5
    user.update_image()
    user.location = "route_1"

    if from_location == "home_city":
        user.rect.topleft = (1300, 700)

    obstacles = [
        pygame.Rect(0, 0, 1500, 150),
        pygame.Rect(0, 830, 1500, 170),
        pygame.Rect(0, 0, 50, 1000),
        pygame.Rect(1450, 0, 50, 1000)
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        route.draw(screen)
        user.update()
        user.draw(screen)
        for o in obstacles:
            if user.rect.colliderect(o):
                obstacle(user, o)
        
        if user.rect.right > 1440 and 700 < user.rect.centery < 800:
            home_city("route_1")
            break

        #For debugging purposes
        for i in range(len(obstacles)):
            pygame.draw.rect(screen, (255, 0, 0), obstacles[i], 2)
        #Remove later
         
        pygame.display.update()
        clock.tick(60)

pygame.mixer.init()
if user.location is None:
    user.location = "home"

if user.location == "home":
    home()
elif user.location == "home_city":
    home_city("none")
elif user.location == "route_1":
    route_1("none")
