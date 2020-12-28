import pygame
import random

'''
GAME SETUP 
''' 
# colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

# screen
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# game vars
x, y = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
x_lead, y_lead = 0, 0
block_size = 20 

x_food = random.randint(0, (SCREEN_WIDTH - block_size)/20) * 20 
y_food = random.randrange(0, SCREEN_HEIGHT - block_size, 20)

def new_snake_position():
    # x, y, x_lead, y_lead
    return SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 0, 0

def new_food_position():
    x = random.randint(0, (SCREEN_WIDTH - block_size)/20) * 20 
    y = random.randrange(0, SCREEN_HEIGHT - block_size, 20)
    return x, y



# functions setup
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# tickrate
clock = pygame.time.Clock()

'''
FUNCTIONS
'''
def draw_grid():
    for x in range(SCREEN_WIDTH):
        for y in range(SCREEN_HEIGHT):
            rect = pygame.Rect(x*block_size, y*block_size,
                               block_size, block_size)
            pygame.draw.rect(display, white, rect, 1)



'''
GAME LOOP
''' 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_lead = -20 
                y_lead = 0
            elif event.key == pygame.K_RIGHT:
                x_lead = 20 
                y_lead = 0
            elif event.key == pygame.K_UP:
                x_lead = 0
                y_lead = -20
            elif event.key == pygame.K_DOWN:
                x_lead = 0 
                y_lead = 20
    
    # set framerate
    clock.tick(24)

    # go out of bounds
    if x > SCREEN_WIDTH - block_size or x < 0 or y > SCREEN_HEIGHT - block_size or y < 0:
        x, y, x_lead, y_lead = new_snake_position()
    
    # TO EAT
    if x == x_food and y == y_food:
        x_food, y_food = new_food_position()

    # movement
    x += x_lead
    y += y_lead

    
    # drawing
    display.fill(black)
    # draw_grid()
    pygame.draw.rect(display, red, (x, y, block_size, block_size))
    pygame.draw.rect(display, blue, (x_food, y_food, block_size, block_size))
    pygame.display.update()
