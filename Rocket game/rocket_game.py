import sys

import pygame

class Rocket:
    """A Rocket with movement."""

    TRUST_SPEED = 1
    SIDE_SPEED = 0.5

    def __init__(self, rg):

        self.screen = rg.screen
        self.screen_rect = rg.screen.get_rect()

        # Rocket image and shape
        self.image = pygame.image.load('Rocket game\\rocket.png')
        self.rect = self.image.get_rect()

        # Possition
        self.rect.midbottom = self.screen_rect.midbottom

        # Current Possition
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.move_right = False
        self.move_left = False

        self.move_up = False
        self.move_down = False
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        # Trust the rocket up or down
        if self.move_up == True and self.rect.top > self.screen_rect.top:
            self.y -= self.TRUST_SPEED
        elif self.move_down == True and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.TRUST_SPEED

        # Move the rocket to the sides
        if self.move_right == True and self.rect.right < self.screen_rect.right:
            self.x += self.SIDE_SPEED
        elif self.move_left == True and self.rect.left > 0:
            self.x -= self.SIDE_SPEED
        
        self.rect.x = self.x
        self.rect.y = self.y

class RocketGame:
    """Creating the game instance"""

    def __init__(self):
        pygame.init()

        # Settings
        self.screen = pygame.display.set_mode((500, 800))
        self.bg_image = pygame.image.load('Rocket game\\rocket_game_bg.png')

        # Creating the rocket instance
        self.rocket = Rocket(self)

    def run(self):
        """A method for running the game"""
        print('Starting the game.')
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Quiting Alien Invasion...')
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    print('Quiting Alien Invasion...')
                    sys.exit()

                if event.key == pygame.K_UP:
                    self.rocket.move_up = True
                elif event.key == pygame.K_DOWN:
                    self.rocket.move_down = True

                if event.key == pygame.K_RIGHT:
                    self.rocket.move_right = True
                elif event.key == pygame.K_LEFT:
                    self.rocket.move_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.rocket.move_up = False
                elif event.key == pygame.K_DOWN:
                    self.rocket.move_down = False
                
                if event.key == pygame.K_RIGHT:
                    self.rocket.move_right = False
                elif event.key == pygame.K_LEFT:
                    self.rocket.move_left = False

    def _update_screen(self):
        self.screen.blit(self.bg_image, (0, 0))
        self.rocket.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    rg = RocketGame()
    rg.run()
