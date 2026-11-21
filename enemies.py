import pygame as pg
#normalde bu class pos variable'ı için x-y koordinatları bekliyor, biz ise waypoints listesini gönderdik.
#o yüzden güncellememiz lazım burayı.
class Enemy(pg.sprite.Sprite): #burada enemy class'ımızı tanımlıyoruz, ayrıca enemy'lerin sprite sayılması için pygame'in sprite class'ından inheritance da aldık
    def __init__(self, waypoints, image):
        pg.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = self.waypoints[0] #burada waypoints'i baştaki pos variable'ımızı extractlemek için kullandığımızı söyledi.
        #en baştaki initial position'umuzu waypoints listesinin ilk elemanı yaptık ki hareketine çizginin başından başlasın.
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos #rect'in center'ına self.pos atadık. 

    def move(self): #burada enemy'nin hareket etmesini sağlayan method var, x ekseninde tick başına 1 piksel ilerliyor bu sayede
        self.rect.x += 1

    def update(self): #burada update diye bir method ekledim, hareket methodunu çağırmak için kullanılıyor
        self.move()
