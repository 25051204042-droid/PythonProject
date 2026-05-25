import pygame
import sys

pygame.init()


WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game Kejar Maling")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

class Character:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 0.5
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface,self.color,
                            (self.x,self.y,self.width,self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Police(Character):
    def move(self):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

class Thief(Character):
    def move(self):
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.x += self.speed


police = Police(100,200, BLUE)
thief = Thief(400, 200, RED)


running = True
game_over = False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_over:
        police.move()
        thief.move()

        if police.get_rect().colliderect(thief.get_rect()):
            print("Polisi Menang!")
            game_over = True

    screen.fill(WHITE)

    if game_over:
        font = pygame.font.SysFont("Times New Roman", 50)
        text = font.render("POLISI MENANG",
                           True, (0, 0, 0))
        screen.blit(text,(200,180))

    police.draw(screen)
    thief.draw(screen)

    pygame.display.update()

pygame.quit()
sys.exit()

