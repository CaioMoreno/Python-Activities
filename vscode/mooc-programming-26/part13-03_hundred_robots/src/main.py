# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

x = 0
y = 0

for i in range(10):
    y = 0 
    c = 0
    for j in range(10):
        window.blit(robot, (x + c, y))
        y += 30 
        c += 10
    x += 40

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()