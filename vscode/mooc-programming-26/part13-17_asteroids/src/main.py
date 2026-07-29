# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))
game_font = pygame.font.SysFont("Arial", 24)
pygame.display.set_caption("Asteroids")


robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")

x = 0
y = 480 - robot.get_height()

to_right = False
to_left = False
points = 0
comets = []
time = 0

clock = pygame.time.Clock()

while True:
    window.fill((0, 0, 0))
    text = game_font.render(f"Points: {points}", True, (255, 0, 0))
    window.blit(text, (530, 0))
    window.blit(robot, (x, y))

    time += 1

    if time > 150:
        time = 0
        j = -50
        i = random.randint(0, 640 - rock.get_width()) 
        comets.append({"x": i, "y": j})
    
    for r in comets:
        window.blit(rock, (r["x"], r["y"]))
        if r["y"] < 480 - rock.get_height():
            r["y"] += 1

        if r["y"] >= 480 - rock.get_height():
            points = 0
            x = 0
            y = 480 - robot.get_height()
            comets.clear()
            break 
        if abs(x - r["x"]) < 50 and abs(y - r["y"]) < 46:
            comets.remove({"x": r["x"], "y": r["y"]})
            points += 1
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False                            

        if event.type == pygame.QUIT:
            exit()

    if x + robot.get_width() >= 640:
        to_right = False
    if x <= 0:
        to_left = False

    if to_right:
        x += 2
    if to_left:
        x -= 2

    pygame.display.flip()

    clock.tick(60)