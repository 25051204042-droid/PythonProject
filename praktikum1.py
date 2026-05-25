import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game PBO Aisy")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Player:
    def __init__(self,x,y):
        self.x = x
        self.y = y

        self.width = 50
        self.height = 50

        self.speed = 0.5

        self.color = BLUE

    def move(self):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:self.y += self.speed

    def limit(self):
        if self.x < 0:
            self.x = 0
        if self.x + self.width > WIDTH:
            self.x = WIDTH - self.width

        if self.y < 0:
            self.y = 0
        if self.y + self.height > HEIGHT:
            self.x = HEIGHT - self.height

    def change1(self):
        if keys[pygame.K_1]:
            self.color = (RED)
        if keys[pygame.K_2]:
            self.color = (BLUE)

    def draw(self, surface):
        pygame.draw.rect(surface,self.color,
                         (self.x, self.y,self.width,self.height))

    def change2(self):
        if keys[pygame.K_p]:
            self.width += 0.2
            self.height += 0.2
        if keys[pygame.K_o]:
            self.width -= 0.2
            self.height -= 0.2

player = Player(375, 375)
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player.move()
    player.limit()
    player.change1()
    player.change2()

    screen.fill(WHITE)
    player.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()