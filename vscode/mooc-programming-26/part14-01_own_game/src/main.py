# Complete your game here
#Create the player. DONE
#Add keyboard movement. DONE
#Create the game window and boundaries. DONE
#Add one treasure object.
#Detect collision with treasure.
#Add the score.
#Add the timer.
#Add the game-over state.
#Add restart functionality.
#Add treasure randomization.
#Add enemies.
#Add health and enemy collisions.
#Add increasing difficulty.
#Add menus, pause, sound, and visual polish.

import pygame

WIDTH = 640
HEIGHT = 480
PLAYER_SPEED = 2
FPS = 60

class Player:
    def __init__(self):
        self.to_left = False
        self.to_right = False
        self.to_up = False
        self.to_down = False
        self.x = 0
        self.y = 0

    def create_player(self):
        self.robot = pygame.image.load("robot.png")
        self.y = HEIGHT - self.robot.get_height()

    def draw(self, window):
        window.blit(self.robot, (self.x, self.y))

    def move_player(self, movement):
        if movement.type == pygame.KEYDOWN:
            if movement.key == pygame.K_LEFT:
                self.to_left = True
            if movement.key == pygame.K_RIGHT:
                self.to_right = True
            if movement.key == pygame.K_UP:
                self.to_up = True
            if movement.key == pygame.K_DOWN:
                self.to_down = True

        if movement.type == pygame.KEYUP:
            if movement.key == pygame.K_LEFT:
                self.to_left = False
            if movement.key == pygame.K_RIGHT:
                self.to_right = False
            if movement.key == pygame.K_UP:
                self.to_up = False
            if movement.key == pygame.K_DOWN:
                self.to_down = False

    def update_position(self):
        if self.to_right:
            self.x += PLAYER_SPEED
        if self.to_left:
            self.x -= PLAYER_SPEED
        if self.to_up:
            self.y -= PLAYER_SPEED
        if self.to_down:
            self.y += PLAYER_SPEED


class Game:
    def __init__(self):
        pygame.init()
        self.player = Player()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))

        self.new_game()

        pygame.display.set_caption("Gold Hunter")
        self.clock = pygame.time.Clock()

        self.main_loop()

    def new_game(self):
        #load the images for the game
        self.player.create_player()

    def main_loop(self):
        while True:
            self.check_events()
            self.player.update_position()
            self.draw_window()
            self.clock.tick(FPS)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            self.player.move_player(event)

        self.field_boundaries()

    def field_boundaries(self):
        if self.player.x + self.player.robot.get_width() >= WIDTH:
            self.player.to_right = False
        if self.player.x < 0:
            self.player.to_left = False
        if self.player.y + self.player.robot.get_height() >= HEIGHT:
            self.player.to_down = False
        if self.player.y <= 0:
            self.player.to_up = False
        

    def draw_window(self):
        self.window.fill((0, 0, 0))
        self.player.draw(self.window)
        pygame.display.flip()



if __name__ == "__main__":
    Game()