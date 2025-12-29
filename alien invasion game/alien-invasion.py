import sys
import pygame
from setting import Setting
from ship import Ship
from bullet import Bullet

class AlienInvasion:

    def __init__(self): #1
        pygame.init()
        self.setting = Setting()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

        self.screen = pygame.display.set_mode(
        (self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self): # Start the main loop for the game
        while True:
            self.check_events()
            self.update_screens()
            self.ship.update()
            self.update_bullet()


    def update_bullet(self):
            self.bullets.update()  
            for bullet in self.bullets.sprites():
                if bullet.rect.bottom <= 0:
                    bullet.kill()

    def check_events(self): # Respond to keypresses and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                self.check_keyup_event(event)
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_event(event)
            elif event.type == pygame.K_LEFT:
                self.check_keyleft_event(event)
            elif event.type == pygame.K_RIGHT:
                self.check_keyright_event(event)

    def check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


    def check_keydown_event(self,event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

    def fire_bullet(self):
         if len(self.bullets) < self.setting.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_screens(self): # Update images on the screen, and flip to the new screen
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()                                                                                               
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()