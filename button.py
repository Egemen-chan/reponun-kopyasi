import pygame as pg

class Button():
  def __init__(self, x, y, image):
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y) #kullandığımız x ve y verilerini buttonun sol üst köşesi olarak belirledik. bu yüzden ismini böyle koyduk

  def draw(self, surface):
    #there are a few steps to working with buttons
    #get mouse position
    pos = pg.mouse.get_pos()
    
    #check mouseover and clicked conditions (he said that the button was a rectangle, so we could simply check for collision.)
    if self.rect.collidepoint(pos): #she was coding something :pp. bu, mouse'un buttonun üzerinde geziniyor olma durumunu kontrol ediyor.
      if pg.mouse.getpressed()[0] == 1: #mouse'umuzun tıklama durumuna bakıyoruz. [0]'ın olayı sadece sol tıklama kabul etmek
        pass #temporary. sonradan daha guzel seyler yazicaz buraya
    #draw button on screen. crazy i know
    surface.blit(self.image, self.rect) #ekrana çizdirecek metodu oluşturduk.
    
