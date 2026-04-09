import pygame
import sys
import random

# Inisialisasi Pygame
pygame.init()

# Konstanta
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
FPS = 60
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
RED = (200, 50, 50)


# --- 1. Parent Class ---
class GameObject:
    def __init__(self, x, y, width, height, image_path):
        try:
            self.raw_image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.raw_image, (width, height))
            self.rect = self.image.get_rect(topleft=(x, y))
        except pygame.error as e:
            print(f"Gagal memuat gambar {image_path}: {e}")
            pygame.quit()
            sys.exit()

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# --- 2. Subclasses (Player, Enemy, Coin) ---
class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 40, 40, 'player.png')
        self.speed = 5
        self.lives = 3

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH: self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0: self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT: self.rect.y += self.speed


class Enemy(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 35, 35, 'enemy.png')
        self.speed_x = random.choice([-3, 3])
        self.speed_y = random.choice([-3, 3])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH: self.speed_x *= -1
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT: self.speed_y *= -1


class Coin(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 25, 25, 'coin.png')
        self.is_collected = False


# --- 3. Game Engine ---
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Sprite Adventure")
        self.clock = pygame.time.Clock()

        # --- PERUBAHAN DISINI: Memuat Background ---
        try:
            bg_raw = pygame.image.load('background.png').convert()
            self.bg_image = pygame.transform.scale(bg_raw, (SCREEN_WIDTH, SCREEN_HEIGHT))
        except pygame.error:
            print("Peringatan: background.png tidak ditemukan, menggunakan warna solid.")
            self.bg_image = None

        self.font_main = pygame.font.SysFont("Arial", 32, bold=True)
        self.font_hud = pygame.font.SysFont("Arial", 20)
        self.state = "START"
        self.reset_game()

    def reset_game(self):
        self.player = Player(50, SCREEN_HEIGHT // 2)
        self.coins = [Coin(random.randint(50, 550), random.randint(50, 350)) for _ in range(8)]
        self.enemies = [Enemy(400, 100), Enemy(400, 300)]
        self.score = 0

    def draw_text_centered(self, text, font, color, y_offset=0):
        surf = font.render(text, True, color)
        rect = surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset))
        self.screen.blit(surf, rect)

    def update_logic(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys)
        for enemy in self.enemies:
            enemy.update()
            if self.player.rect.colliderect(enemy.rect):
                self.player.lives -= 1
                self.player.rect.topleft = (50, SCREEN_HEIGHT // 2)
                if self.player.lives <= 0: self.state = "GAMEOVER"
        for coin in self.coins:
            if not coin.is_collected and self.player.rect.colliderect(coin.rect):
                coin.is_collected = True
                self.score += 1
        if self.score == len(self.coins): self.state = "WON"

    def draw_screen(self):
        # --- PERUBAHAN DISINI: Render Background ---
        if self.bg_image:
            self.screen.blit(self.bg_image, (0, 0))
        else:
            self.screen.fill(WHITE)

        if self.state == "START":
            self.draw_text_centered("ADVENTURE GAME", self.font_main, BLACK, -40)
            self.draw_text_centered("Tekan Apapun untuk Mulai", self.font_hud, BLACK, 20)

        elif self.state == "PLAYING":
            for c in self.coins:
                if not c.is_collected: c.draw(self.screen)
            for e in self.enemies: e.draw(self.screen)
            self.player.draw(self.screen)

            # HUD
            score_txt = self.font_hud.render(f"Coins: {self.score}", True, WHITE if self.bg_image else BLACK)
            self.screen.blit(score_txt, (15, 15))

        elif self.state == "WON":
            self.draw_text_centered("YOU WIN!", self.font_main, BLACK, -20)
        elif self.state == "GAMEOVER":
            self.draw_text_centered("GAME OVER", self.font_main, RED, -20)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN and self.state != "PLAYING":
                    self.reset_game()
                    self.state = "PLAYING"

            if self.state == "PLAYING": self.update_logic()
            self.draw_screen()
            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == "__main__":
    Game().run()