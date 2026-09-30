import pygame
from pygame import *
import math
import time
import sys
import random
import spritesheet


pygame.init()

# Set up display
width, height = 1900, 1000
window = pygame.display.set_mode((width, height))

#Set up background image, list of backgrounds is the grid the user can traverse
background_wood = pygame.image.load("Wood.png").convert()
background_wood = pygame.transform.scale(background_wood, (width, height))
backgrounds = [[background_wood, background_wood, background_wood],

               [background_wood, background_wood, background_wood],

               [background_wood, background_wood, background_wood]]

current_row = 0
current_col = 0
current_background = backgrounds[current_row][current_col]
rooms = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]
current_room = 0

#We have to specify this, for some reason
black = (0, 0, 0)
#We need this to update the time program is running
last_update = pygame.time.get_ticks()
#We need this to define how fast the animations run
animation_cooldown = 500

#Player animations
leon_duck_spritesheet_left = pygame.image.load("Leon_Duck_Left.png").convert_alpha()
leon_duck_spritesheet_right = pygame.image.load("Leon_Duck_Right.png").convert_alpha()
leon_duck_spritesheet_front = pygame.image.load("Leon_Duck_Front.png").convert_alpha()
leon_duck_spritesheet_back = pygame.image.load("Leon_Duck_Back.png").convert_alpha()

sprite_sheet_left = spritesheet.SpriteSheet(leon_duck_spritesheet_left)
sprite_sheet_right = spritesheet.SpriteSheet(leon_duck_spritesheet_right)
sprite_sheet_front = spritesheet.SpriteSheet(leon_duck_spritesheet_front)
sprite_sheet_back = spritesheet.SpriteSheet(leon_duck_spritesheet_back)

animation_list_left = []
animation_list_right = []
animation_list_front = []
animation_list_back = []
animation_steps = 4
frame = 0

for x in range(animation_steps):
    animation_list_left.append(sprite_sheet_left.get_image(x, 256, 256, .5, black))
    animation_list_right.append(sprite_sheet_right.get_image(x, 256, 256, .5, black))
    animation_list_front.append(
        sprite_sheet_front.get_image(x, 256, 256, .5, black))  # Load frames from sprite_sheet_front
    animation_list_back.append(
        sprite_sheet_back.get_image(x, 256, 256, .5, black))  # Load frames from sprite_sheet_back

#Player sprites and stuff
duck_width = animation_list_right[0].get_width()
duck_height = animation_list_right[0].get_height()
duck_x = 100
duck_y = 100
duck_speed = 5
direction = 'left'
player_health = 3

#Time stuff
enemy_attack_delay = 2
last_attack_time = 0

#Star imgs
img = pygame.image.load("star_bullet.png").convert_alpha()
star = pygame.transform.scale(img, (50, 50))

img = pygame.image.load("soda.png").convert_alpha()
enemy_img = pygame.transform.scale(img, (100, 100))
#List of all the objects the player must sort across all grids
objects = []

def room():
    """This function creates a random amount of objects to collect and stores them
    in max_stars to return"""
    global rooms
    global current_room
    if current_room == 0:
        max_stars = random.randint(1, 2)
        max_enemies = 1
    if current_room == 1:
        max_stars = random.randint(2, 3)
        max_enemies = random.randint(1, 3)
    if current_room == 2:
        max_stars = random.randint(1, 4)
        max_enemies = random.randint(2, 5)
    if current_room == 3:
        max_stars = random.randint(1, 5)
        max_enemies = random.randint(3, 7)
    if current_room == 4:
        max_stars = random.randint(3, 3)
        max_enemies = random.randint(4, 8)
    if current_room == 5:
        max_stars = random.randint(1, 7)
        max_enemies = random.randint(5, 6)
    if current_room == 6:
        max_stars = random.randint(3, 4)
        max_enemies = random.randint(2, 6)
    if current_room == 7:
        max_stars = random.randint(2, 5)
        max_enemies = random.randint(3, 6)
    if current_room == 8:
        max_stars = random.randint(7, 9)
        max_enemies = random.randint(10, 15)
    return (max_stars,max_enemies)

def spawn_stars(room):
    """This function spawns the objects in a room and turns the object into a dictionary to be edited"""
    global current_room
    global max_stars
    stars_current_room = []
    for item in objects:
        if item['room'] == room:
            stars_current_room.append(item)
    if len(stars_current_room) < max_stars:
        star_x = random.randint(50, width - star.get_width() - 100)
        star_y = random.randint(height // 2, height - star.get_height() - 100)  # Adjusted spawn area
        item = {'x': star_x, 'y': star_y, 'star_direction': 'left',
                 'star_speed': 4.5, 'room': room, 'collected': False}
        objects.append(item)

enemies = []
def spawn_enemies(room):
    global max_enemies
    global enemies
    enemies_current_room = []
    for enemy in enemies:
        if enemy['room'] == room:
            enemies_current_room.append(enemy)
    if len(enemies_current_room) < max_enemies:
        enemy_x = random.randint(0, width - enemy_img.get_width())
        enemy_y = random.randint(height // 2, height - enemy_img.get_height())  # Adjusted spawn area
        # enemy dictionary
        enemy = {'x': enemy_x, 'y': enemy_y,'enemy_speed': random.randint(2,4), 'room': room}
        enemies.append(enemy)



running = True

while running:

    #Get mouse click events from pygame

    #We need this for some reason
    clock = pygame.time.Clock()
    window.fill((0, 0, 0))

    #define max amount of objects spawning'
    max_stars,max_enemies = room()
    #Track mouse operations
    mouse_x, mouse_y = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    #If anything happens where the user loses or wants to quit, then quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.blit(current_background, (0, 0))

    # Display health
    font = pygame.font.Font(None, 75)
    text_surface = font.render(f'Current Health: {player_health}', True, (255, 255, 255))
    player_health_rect = text_surface.get_rect(center=(250, 150))
    window.blit(text_surface, (200, 100))

    # Display instruction
    font = pygame.font.Font(None, 30)
    text_surface = font.render(f'Collect all the objects to win! Avoid the soda cans! Press P to quit', True, (255, 255, 255))
    instruction_rect = text_surface.get_rect(center=(250, 150))
    window.blit(text_surface, (200, 160))

    #Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        duck_x = duck_x - duck_speed
        if duck_x <= 0:  # Check if player reaches the left wall
            # Teleport to the previous room
            current_col = (current_col - 1) % 3
            current_background = backgrounds[current_row][current_col]  # Update current background
            duck_x = width - duck_height  # Teleport to the right side
            room_change = True
        else:
            duck_x = duck_x - duck_speed
        direction = 'left'

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        duck_x = duck_x + duck_speed
        if duck_x + duck_width >= width:  # Check if player reaches the right wall
            # Teleport to the next room
            current_col = (current_col + 1) % 3
            current_background = backgrounds[current_row][current_col]  # Update current background
            duck_x = 0  # Teleport to the left side
            room_change = True
        else:
            duck_x = duck_x + duck_speed

        direction = 'right'

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        if duck_y <= 0:  # Check if player reaches the top wall
            # Teleport to the previous room
            current_row = (current_row - 1) % 3
            current_background = backgrounds[current_row][current_col]  # Update current background
            duck_y = height - duck_height  # Teleport to the bottom side
            room_change = True
        else:
            duck_y = duck_y - duck_speed - 3

    # amy_y + amy_image.get_height() < HEIGHT old code if this doesn't work
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if duck_y + duck_height >= height:  # Check if player reaches the bottom wall
            # Teleport to the next room
            current_row = (current_row + 1) % 3
            current_background = backgrounds[current_row][current_col]  # Update current background
            duck_y = 0  # Teleport to the top side
            room_change = True
        else:
            duck_y = duck_y + duck_speed + 3
        direction = 'front'

    #Break if they press p
    if keys[pygame.K_p]:
        break

    #Direction duck sprite is facing
    if direction == 'left':
        window.blit(animation_list_left[frame], (duck_x, duck_y))
    elif direction == 'right':
        window.blit(animation_list_right[frame], (duck_x, duck_y))
    elif direction == 'back':
        window.blit(animation_list_back[frame], (duck_x, duck_y))  # Blit the back sprite
    elif direction == 'front':
        window.blit(animation_list_front[frame], (duck_x, duck_y))

    #Make hitbpxes for objects and players
    player_rect = pygame.Rect(duck_x, duck_y, 100, 100)



    #Collision checker if player gets an object
    dx = mouse_x - duck_x
    dy = mouse_y - duck_y
    for item in objects:
        item_rect = pygame.Rect(item['x'], item['y'], star.get_width(), star.get_height())
        if player_rect.colliderect(item_rect) and item['room'] == current_room and item["collected"] == False:
            item['collected'] = True
            duck_speed += 1
        for item1 in objects:
            item1_rect = pygame.Rect(item1['x'], item1['y'], star.get_width(), star.get_height())
            if item1_rect.colliderect(item_rect) and item1['room'] == current_room and item['room'] == current_room:
                #Knockback stars if they collide with each other
                item1['x'] += (item1['x'] - item['x']) * .15
                item1['y'] += (item1['y'] - item['y']) * .15

    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy['x'], enemy['y'], enemy_img.get_width()-75, enemy_img.get_height()-75)
        if player_rect.colliderect(enemy_rect) and time.time() - last_attack_time >= enemy_attack_delay and enemy['room'] == current_room:
            player_health -= 1
            duck_speed += 3
            last_attack_time = time.time()
            print("Player health:", player_health)
            enemy['x'] += (enemy['x'] - duck_x + 100)
            enemy['y'] += (enemy['y'] - duck_y + 100)



    #display stars
    for item in objects:
        if item['room'] == current_room and item['collected'] == False:
            window.blit(star, (item['x'], item['y']))
        if item['room'] == current_room and item['collected']:
            window.blit(star, (item['x'], item['y']))


    current_room = rooms[current_row][current_col]
    spawn_stars(current_room)
    spawn_enemies(current_room)

    # star pathfinding if collectedw
    for item in objects:
        if item['room'] == current_room and item['collected']:
            if duck_x < item['x']:
                item['x'] -= item['star_speed']
                item['star_direction'] = 'left'
            elif duck_x > item['x']:
                item['x'] += item['star_speed']
                item['star_direction'] = 'right'
            if duck_y < item['y']:
                item['y'] -= item['star_speed']
            elif duck_x > item['y']:
                item['y'] += item['star_speed']

    #Enemy pathfinding and blit
    for enemy in enemies:
        if enemy['room'] == current_room:
            window.blit(enemy_img, (enemy['x'], enemy['y']))
        if enemy['room'] == current_room:
            if duck_x < enemy['x']:
                enemy['x'] -= enemy['enemy_speed']
                enemy['enemy_direction'] = 'left'
            elif duck_x > enemy['x']:
                enemy['x'] += enemy['enemy_speed']
                enemy['enemy_direction'] = 'right'
            if duck_y < enemy['y']:
                enemy['y'] -= enemy['enemy_speed']
            elif duck_x > enemy['y']:
                enemy['y'] += enemy['enemy_speed']


    #Check if all stars are collected
    num_collected = 0
    to_collect = 0
    for item in objects:
        if item['collected']:
            num_collected += 1
        else:
            to_collect += 1
    if num_collected >= 20:
        print ("You win!")
        break
    #Display collected already
    font = pygame.font.Font(None, 30)
    text_surface = font.render(f'{num_collected} collected! Collect 20 objects to win! There is {to_collect} more to go from the rooms you visited!', True, (255, 255, 255))
    instruction_rect = text_surface.get_rect(center=(250, 150))
    window.blit(text_surface, (200, 180))

    #Check if player dies
    if player_health <= 0:
        print("Game Over")
        pygame.quit()
        sys.exit()


    #Get the time the program is running and make sure the duck decreases speed overtime if
    #they are above average speed
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame = (frame + 1) % animation_steps
        last_update = current_time
        if duck_speed > 5:
            duck_speed -= 1

    #Define player position and hitbox


    pygame.display.update()
    clock.tick(60)

pygame.quit()