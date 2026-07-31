# Complete your game here
import pygame

class Game:
    def __init__(self):
        pygame.init()

        self.load_images()
        self.new_game()

        self.window = pygame.display.set_mode((640, 480))

        pygame.display.set_caption("Gold Hunter")
        self.main_loop()

    def load_images(self):
        self.images = []
        for name in ["coin", "monster", "robot"]:
            self.images.append(pygame.image.load(name + ".png"))

    def new_game(self):
        print("ok")

    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def draw_window(self):
        self.window.fill((0, 0, 0))

        pygame.display.flip()

if __name__ == "__main__":
    Game()