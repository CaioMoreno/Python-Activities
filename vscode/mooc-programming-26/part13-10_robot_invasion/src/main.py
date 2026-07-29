# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame, random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

clock = pygame.time.Clock()

window.fill((0, 0, 0))
robots = []
time = 0
#I have to resolve the random robots in the animation
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    time += 1
    if time > 50:
        y = random.randint(-200, -30)
        x = random.randint(0, 640 - robot.get_width())   
        robots.append({"x": x , "y": y})
        time = 0

    for r in robots:
        window.blit(robot, (r["x"], r["y"]))

        pygame.display.flip()
        if r["y"] + robot.get_height() < 480:
            r["y"] += 1
        elif r["y"] + robot.get_height() >= 480 and r["x"] <= 320:
            r["x"] -= 1
        elif r["y"] + robot.get_height() >= 480 and r["x"] > 320:
            r["x"] += 1

    clock.tick(60)