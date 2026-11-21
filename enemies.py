import pygame as pg
#şimdi enemy'mizin çizgileri takip etmesi için belli bir açı da yapıyor olması lazım. 
#bu işi kolaylaştırmk için vector2 adında bir modül kullanacağız.
from pygame.math import Vector2 #modülü importladık. sonra self.pos'u bunu içerisine attık. 
#normalde bu class pos variable'ı için x-y koordinatları bekliyor, biz ise waypoints listesini gönderdik.
#o yüzden güncellememiz lazım burayı.
class Enemy(pg.sprite.Sprite): #burada enemy class'ımızı tanımlıyoruz, ayrıca enemy'lerin sprite sayılması için pygame'in sprite class'ından inheritance da aldık
    def __init__(self, waypoints, image):
        pg.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0]) #burada waypoints'i baştaki pos variable'ımızı extractlemek için kullandığımızı söyledi.
        #en baştaki initial position'umuzu waypoints listesinin ilk elemanı yaptık ki hareketine çizginin başından başlasın.
        #şimdi enemy'nin çizgimizi gerçekten takip etmesini sağlamamız lazım.
        self.target_waypoint = 1 #bir sonraki waypoint'imizin waypoints listesi içerisindeki indexi olacak bu sayı :D
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos #rect'in center'ına self.pos atadık. 

    def move(self): #burada enemy'nin hareket etmesini sağlayan method var, x ekseninde tick başına 1 piksel ilerliyor bu sayede #ARTIK YOK DFJKGNLSKDJFNLSD
        #şimdi bu methodun içine hedef waypoint tanımlayacağız.
        self.target = Vector2(self.waypoints[self.target_waypoint]) #hedefimiz = waypointsteki istediğimiz indexe sahip eleman demiş olduk :D 
        #şimdi bir current position, bir de target position diye iki variableımız var. 
        self.movement = self.target - self.pos #bu iki variableın arasındaki mesafeyi belirlemiş olduk.
        print(self.movement.normalize()) #Vector2'den gelen normalize methodunu ekledik. artık ekrana bastırılan variable'lar değişti. 
        #sanırım işin trigonometri kısmını halletmiş olduk.
        #artık enemy ekranın bir ucundan diğerine gitmeyeceği için x += 1 kısmını sildik. sorry Egemen :D 

    def update(self): #burada update diye bir method ekledim, hareket methodunu çağırmak için kullanılıyor
        self.move()
