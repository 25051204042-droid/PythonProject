import random


#Mengatur 1 Awan
class Cloud:
    #konstruktor
    #cetakan sifat dasar 1 awan
    def __init__(self, pos, img, speed, depth):
        self.pos = list(pos)
        self.img = img
        self.speed = speed
        self.depth = depth

    #Mengubah posisi awan seiring berjalannya waktu
    def update(self):
        self.pos[0] += self.speed

    #menggambar fisik awan ke layar berdasarkan posisi kamera game
    def render(self, surf, offset=(0, 0)):
        render_pos = (self.pos[0] - offset[0] * self.depth, self.pos[1] - offset[1] * self.depth)
        surf.blit(self.img, (render_pos[0] % (surf.get_width() + self.img.get_width()) - self.img.get_width(),
                             render_pos[1] % (surf.get_height() + self.img.get_height()) - self.img.get_height()))


#mandor semua awan
class Clouds:
    #konstruktor
    #melahirkan dan mengacak 16 awan sekaligus
    def __init__(self, cloud_images, count=16):
        self.clouds = []

        for i in range(count):
            self.clouds.append(Cloud((random.random() * 99999, random.random() * 99999), random.choice(cloud_images),
                                     random.random() * 0.05 + 0.05, random.random() * 0.6 + 0.2))

        self.clouds.sort(key=lambda x: x.depth)

    #menyuruh semua awan jalan
    def update(self):
        for cloud in self.clouds:
            cloud.update()

    #seluruh awan untuk menggambar dirinya ke layar
    def render(self, surf, offset=(0, 0)):
        for cloud in self.clouds:
            cloud.render(surf, offset=offset)