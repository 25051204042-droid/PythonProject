import math

import pygame


class Spark:
    #konstruktor
    def __init__(self, pos, angle, speed):
        self.pos = list(pos)
        self.angle = angle
        self.speed = speed

    #method untuk pergerakan dengan logika trigonometri
    def update(self):
        self.pos[0] += math.cos(self.angle) * self.speed
        self.pos[1] += math.sin(self.angle) * self.speed

        self.speed = max(0, self.speed - 0.1)
        return not self.speed

    #method untuk menggambar sebuah Poligon (Segi Empat Berbintang/Belah Ketupat Meruncing) menggunakan 4 titik koordinat
    def render(self, surf, offset=(0, 0)):
        render_points = [
            ## 1. TITIK DEPAN (Maju searah pergerakan, dikali speed * 3 agar makin cepat makin panjang)
            (self.pos[0] + math.cos(self.angle) * self.speed * 3 - offset[0],
             self.pos[1] + math.sin(self.angle) * self.speed * 3 - offset[1]),
            #2. TITIK KANAN (Diputar 90 derajat [+ math.pi * 0.5], dikali 0.5 agar tipis)
            (self.pos[0] + math.cos(self.angle + math.pi * 0.5) * self.speed * 0.5 - offset[0],
             self.pos[1] + math.sin(self.angle + math.pi * 0.5) * self.speed * 0.5 - offset[1]),
            #3. TITIK BELAKANG(Diputar 180 derajat[+ math.pi] menjadi ekornya)
            (self.pos[0] + math.cos(self.angle + math.pi) * self.speed * 3 - offset[0],
             self.pos[1] + math.sin(self.angle + math.pi) * self.speed * 3 - offset[1]),
            #4. TITIK KIRI(Diputar - 90 derajat[- math.pi * 0.5] untuk sisi sebelahnya)
            (self.pos[0] + math.cos(self.angle - math.pi * 0.5) * self.speed * 0.5 - offset[0],
             self.pos[1] + math.sin(self.angle - math.pi * 0.5) * self.speed * 0.5 - offset[1]),
        ]

        #titik berwarna putih
        pygame.draw.polygon(surf, (255, 255, 255), render_points)