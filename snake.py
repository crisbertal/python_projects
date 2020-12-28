import pygame

'''
GAME SETUP 
''' 
# colors
black = (0,0,0)
red = (255,0,0)

# screen
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# game vars
x, y = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
x_lead, y_lead = 0, 0

# functions setup
pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

'''
GAME LOOP
''' 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_lead = -10 
                y_lead = 0
            elif event.key == pygame.K_RIGHT:
                x_lead = 10 
                y_lead = 0
            elif event.key == pygame.K_UP:
                x_lead = 0
                y_lead = -10
            elif event.key == pygame.K_DOWN:
                x_lead = 0 
                y_lead = 10

    # tickrate
    clock = pygame.time.Clock()
    clock.tick(30)

    # movement
    x += x_lead
    y += y_lead
    
    # drawing
    display.fill(black)
    pygame.draw.rect(display, red, (x, y, 20, 20))
    pygame.display.update()
