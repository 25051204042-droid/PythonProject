#utils.py : menyediakan alat-alat bantu agar file lain bisa bekerja dengan mudah.

import os
import pygame

BASE_IMG_PATH = 'data/images/'

#load_image & load_images:
#Tugasnya mengambil gambar balok, trs hpus latar belakang supaya siap dipakai di dalam game.
def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images

#Tugasnya mengatur pergantian gambar dari frame ke frame
class Animation:
    #construktor
    def __init__(self, images, img_dur=5, loop=True):
        self.images = images #enkapsulasi
        self.loop = loop
        self.img_duration = img_dur #enkapsulasi
        self.done = False
        self.frame = 0

    def copy(self):
        return Animation(self.images, self.img_duration, self.loop)

    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True

    def img(self):
        return self.images[int(self.frame / self.img_duration)]