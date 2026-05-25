import arcade

# --- KONSTANTA ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Varmintz Clone - Versi Arcade 3.0+"
GRID_SIZE = 40


class Player(arcade.SpriteSolidColor):
    def __init__(self):
        # Karakter Utama: Kotak Putih
        super().__init__(30, 30, arcade.color.WHITE)
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = GRID_SIZE // 2 + 5

    def move(self, dx, dy):
        new_x = self.center_x + (dx * GRID_SIZE)
        new_y = self.center_y + (dy * GRID_SIZE)
        # Batasi agar tidak keluar layar
        if 0 < new_x < SCREEN_WIDTH:
            self.center_x = new_x
        if 0 < new_y < SCREEN_HEIGHT:
            self.center_y = new_y


class MovingBox(arcade.SpriteSolidColor):
    def __init__(self, x, y, speed, width, height, color):
        super().__init__(width, height, color)
        self.center_x = x
        self.center_y = y
        self.change_x = speed

    def update(self, delta_time: float):
        # Gerakkan kotak
        self.center_x += self.change_x * delta_time

        # Looping posisi jika keluar layar
        if self.change_x > 0 and self.left > SCREEN_WIDTH:
            self.right = 0
        elif self.change_x < 0 and self.right < 0:
            self.left = SCREEN_WIDTH


class VarmintzGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AMAZON)

        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.log_list = arcade.SpriteList()
        self.food_list = arcade.SpriteList()

        self.player = None
        self.score = 0
        self.game_won = False

    def setup(self):
        # Reset semua list
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.log_list = arcade.SpriteList()
        self.food_list = arcade.SpriteList()

        self.score = 0
        self.game_won = False

        # Inisialisasi Player
        self.player = Player()
        self.player_list.append(self.player)

        # Musuh (Kotak Merah)
        for y in [GRID_SIZE * 2, GRID_SIZE * 4]:
            enemy = MovingBox(100, y, 3.5, 50, 30, arcade.color.RED)
            self.enemy_list.append(enemy)

        # Balok Kayu (Kotak Cokelat)
        for y in [GRID_SIZE * 7, GRID_SIZE * 8]:
            for x in range(0, SCREEN_WIDTH, 250):
                speed = 2.0 if y % 2 == 0 else -2.0
                log = MovingBox(x, y, speed, 80, 25, arcade.color.WOOD_BROWN)
                self.log_list.append(log)

        # Makanan (Lingkaran Kuning)
        for x in range(100, SCREEN_WIDTH, 200):
            food = arcade.SpriteCircle(10, arcade.color.YELLOW)
            food.center_x = x
            food.center_y = GRID_SIZE * 5
            self.food_list.append(food)

    def on_draw(self):
        self.clear()

        # 1. Gambar Zona Finish (Ganti draw_rectangle_filled dengan draw_lrtb_rectangle_filled)
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT - 40, SCREEN_HEIGHT, arcade.color.GOLD)

        # 2. Gambar Area Sungai (Biru)
        arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, GRID_SIZE * 6.5, GRID_SIZE * 8.5, arcade.color.BLUE_SAPPHIRE)

        # Draw semua sprite
        self.food_list.draw()
        self.log_list.draw()
        self.enemy_list.draw()
        self.player_list.draw()

        # Teks Skor
        arcade.draw_text(f"Score: {self.score}", 20, 20, arcade.color.WHITE, 16)

        if self.game_won:
            arcade.draw_text("MENANG! Tekan R untuk Reset", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                             arcade.color.WHITE, 30, anchor_x="center")

    def on_update(self, delta_time: float):
        if self.game_won:
            return

        self.enemy_list.update(delta_time)
        self.log_list.update(delta_time)

        # Cek tabrakan musuh
        if arcade.check_for_collision_with_list(self.player, self.enemy_list):
            self.setup()

        # Logika Sungai
        logs_hit = arcade.check_for_collision_with_list(self.player, self.log_list)
        in_river = (GRID_SIZE * 6.5) < self.player.center_y < (GRID_SIZE * 8.5)

        if in_river:
            if logs_hit:
                # Ikut arus balok pertama yang disentuh
                self.player.center_x += logs_hit[0].change_x
            else:
                self.setup()  # Tenggelam

        # Ambil Makanan
        foods_hit = arcade.check_for_collision_with_list(self.player, self.food_list)
        for food in foods_hit:
            food.remove_from_sprite_lists()
            self.score += 10

        # Cek Menang
        if self.player.center_y >= SCREEN_HEIGHT - 40:
            if len(self.food_list) == 0:
                self.game_won = True
            else:
                # Paksa ambil semua koin dulu
                self.player.center_y = GRID_SIZE // 2 + 5

    def on_key_press(self, key, modifiers):
        if self.game_won and key == arcade.key.R:
            self.setup()
            return

        if key == arcade.key.UP or key == arcade.key.W:
            self.player.move(0, 1)
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.move(0, -1)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.move(-1, 0)
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.move(1, 0)


if __name__ == "__main__":
    window = VarmintzGame()
    window.setup()
    arcade.run()