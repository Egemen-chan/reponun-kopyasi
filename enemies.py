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
        self.speed = 2 #ileride farklı enemy türleri için farklı farklı hızlar yapacağımız bir speed variable'ı ekledik.
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos #rect'in center'ına self.pos atadık. 

    def move(self): #burada enemy'nin hareket etmesini sağlayan method var, x ekseninde tick başına 1 piksel ilerliyor bu sayede #ARTIK YOK DFJKGNLSKDJFNLSD
        #şimdi bu methodun içine hedef waypoint tanımlayacağız.
        self.target = Vector2(self.waypoints[self.target_waypoint]) #hedefimiz = waypointsteki istediğimiz indexe sahip eleman demiş olduk :D 
        #şimdi bir current position, bir de target position diye iki variableımız var. 
        self.movement = self.target - self.pos #bu iki variableın arasındaki mesafeyi belirlemiş olduk.
        #calculate distance to target so that fazla büyük adımlar hareketin sonunda buga sokmasın.
        dist = self.movement.length() #movement aslında bir vektör, biz de onun uzunluğunu almış olduk.
        #check if remaining distance is greter than enemy speed
        if dist >= self.speed: #bu normalde olması gereken koşulumuz. dolayısıyla normal hareketimizi bunun içine attık.
            self.pos += self.movement.normalize() * self.speed #adım büyüklüğünü speed'le çarptık ki o hızda gitsin.
        else:
            self.pos += self.movement.normalize() * dist #eğer adımdan az kaldıysa direkt distance'ı gideceği şekilde kodladık.
        self.rect.center = self.pos #self.rect'i de güncellemiş olduk.
        #artık enemy ekranın bir ucundan diğerine gitmeyeceği için x += 1 kısmını sildik. sorry Egemen :D 

    def update(self): #burada update diye bir method ekledim, hareket methodunu çağırmak için kullanılıyor
        self.move()
