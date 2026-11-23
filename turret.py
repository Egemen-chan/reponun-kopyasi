import pygame as pg

class Turret(pg.sprite.Sprite):
    def __init__(self, image, tile_x, tile_y):
        pg.sprite.Sprite.__init__(self)
        self.tile_x = tile_x
        self.tile_y = tile_y
        #calculates the center coordinates
        self.x = self.tile_x * 64
        self.y = self.tile_y * 64
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
