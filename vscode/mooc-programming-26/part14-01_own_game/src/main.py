# Complete your game here
#Create the player. DONE
#Add keyboard movement. DONE
#Create the game window and boundaries. DONE
#Add one treasure object. DONE
#Detect collision with treasure. DONE
#Add the score. DONE
#Add the game-over state. DONE
#Add restart functionality. DONE
#Add treasure randomization. DONE
#Add enemies. DONE
#Add health and enemy collisions. DONE
#Add increasing difficulty: number of enemies and enemies speed. DONE
#Add health appearance, restart appearance, menus, pause, sound, visual polish.

import pygame
from random import randint
from dataclasses import dataclass

WIDTH = 640
HEIGHT = 480
PLAYER_SPEED = 2
FPS = 60

@dataclass
class Enemy:
    x: float
    y: float
    speed: float

class Enemies:
    def __init__(self):
        self.monster = pygame.image.load("monster.png")
        self.enemies = []

    def create_enemy(self):
        x = randint(0, WIDTH - self.monster.get_width())
        y = randint(0, HEIGHT - self.monster.get_height())
        speed = 0.5 + len(self.enemies)/10
        enemy = Enemy(x, y, speed)
        self.enemies.append(enemy)

    def draw(self, window):
        for e in self.enemies:
            window.blit(self.monster, (e.x, e.y))

    def update_position(self, player):
        for e in self.enemies:
            if player.x > e.x:
                e.x += e.speed
            elif player.x < e.x:
                e.x -= e.speed
            if player.y > e.y:
                e.y += e.speed
            elif player.y < e.y:
                e.y -= e.speed

class Treasure:
    def __init__(self):
        self.treasure = pygame.image.load("coin.png")
        self.x = 0
        self.y = 0

    def create_treasure(self):
        self.y = randint(0, HEIGHT - self.treasure.get_height())
        self.x = randint(0, WIDTH - self.treasure.get_width())

    def draw(self, window):
        window.blit(self.treasure, (self.x, self.y))

    def update_position(self):
        self.y = randint(0, HEIGHT - self.treasure.get_height())
        self.x = randint(0, WIDTH - self.treasure.get_width())

class Player:
    def __init__(self):
        self.robot = pygame.image.load("robot.png")
        self.to_left = False
        self.to_right = False
        self.to_up = False
        self.to_down = False
        self.x = 0
        self.y = 0

    def create_player(self):
        self.x = 0
        self.y = HEIGHT - self.robot.get_height()
        self.health = 3

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
        self.treasure = Treasure()
        self.enemies = Enemies()

        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.game_font = pygame.font.SysFont("Arial", 24)
        self.new_game()
        pygame.display.set_caption("Gold Hunter")
        self.clock = pygame.time.Clock()

        self.main_loop()

    def new_game(self):
        self.change = 5
        self.player.create_player()
        self.treasure.create_treasure()
        self.enemies.enemies.clear()
        self.enemies.create_enemy()
        self.create_hud()

    def main_loop(self):
        while True:
            self.check_events()
            if self.player.health == 0:
                self.new_game()
            self.player.update_position()
            self.next_difficulty()
            self.enemies.update_position(self.player)
            self.draw_window()
            self.clock.tick(FPS)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F9:
                    self.new_game()
            self.player.move_player(event)

        self.field_boundaries()
        self.check_colision()

    def create_hud(self):
        self.score = 0
        self.score_text = self.game_font.render(f"Score: {self.score}", True, (255, 0, 0))
        self.health_text = self.game_font.render(f"Health: {self.player.health}", True, (255, 0, 0))
        self.text_restart = self.game_font.render(f"Restart: F9", True, (255, 0, 0))

    def update_score(self):
        self.score += 1
        self.score_text = self.game_font.render(f"Score: {self.score}", True, (255, 0, 0))

    def update_health(self):
        self.player.health -=1
        self.health_text = self.game_font.render(f"Health: {self.player.health}", True, (255, 0, 0))

    def next_difficulty(self):
        if self.score == self.change:
            self.enemies.create_enemy()
            self.change += 5

    def field_boundaries(self):
        if self.player.x + self.player.robot.get_width() >= WIDTH:
            self.player.to_right = False
        if self.player.x < 0:
            self.player.to_left = False
        if self.player.y + self.player.robot.get_height() >= HEIGHT:
            self.player.to_down = False
        if self.player.y <= 0:
            self.player.to_up = False

    def check_colision(self):
        player_rect = self.player.robot.get_rect(topleft=(self.player.x, self.player.y))
        treasure_rect = self.treasure.treasure.get_rect(topleft=(self.treasure.x, self.treasure.y))

        #monster collision
        for e in self.enemies.enemies:
            enemy_rect = (self.enemies.monster.get_rect(topleft=(e.x, e.y)))
            if player_rect.colliderect(enemy_rect):
                self.enemies.enemies.remove(e)
                self.update_health()
                self.enemies.create_enemy()
                break

        if player_rect.colliderect(treasure_rect):
            self.update_score()
            self.treasure.update_position()  

    def draw_window(self):
        self.window.fill((255, 255, 255))
        self.player.draw(self.window)
        self.treasure.draw(self.window)
        self.enemies.draw(self.window)
        self.window.blit(self.score_text, (530, 0))
        self.window.blit(self.health_text, (0, 0))
        self.window.blit(self.text_restart, (530, 450))
        pygame.display.flip()



if __name__ == "__main__":
    Game()