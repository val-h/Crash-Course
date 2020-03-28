import sys

import pygame

# Settings
screen_width = 1200
screen_height = 800
screen_bg_color = (177, 214, 57)

kb_up = pygame.K_w
kb_down = pygame.K_s
kb_fire = pygame.K_SPACE
kb_quit = pygame.K_q

# Init
pygame.init()
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sideways Shooter')

# Player
player_image = pygame.image.load('Sideways shooter\\ship_vertical.png')
player_rect = player_image.get_rect()
player_speed = 2

pl_move_up = False
pl_move_down = False
pl_y = float(player_rect.y)

player_rect.midleft = win.get_rect().midleft

# Main Functions

def player_draw():
    win.blit(player_image, player_rect)

    print(f'Player y - {pl_y}')

def player_update():
    if pl_move_up == True:
        pl_y -= player_speed
    elif pl_move_down == True:
        pl_y += player_speed

    player_rect.y = pl_y

def _keydown_events(event):
    if event.key == kb_up:
        pl_move_up = True
    elif event.key == kb_down:
        pl_move_down = True

    if event.key == kb_fire:
        # Fire bullet
        pass

    if event.key == kb_quit:
        sys.exit()

def _keyup_events(event):
    if event.key == kb_up:
        pl_move_up = False
    elif event.key == kb_down:
        pl_move_down = False

def _check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            _keydown_events(event)
        elif event.type == pygame.KEYUP:
            _keyup_events(event)

def update_win():
    win.fill(screen_bg_color)
    player_draw()
    pygame.display.update()
    pygame.time.delay(100)

# Main Loop
while True:
    _check_events()
    player_update()
    update_win()

