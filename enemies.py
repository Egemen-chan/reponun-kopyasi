import pygame as pg
from pygame.math import Vector2 #bu modülü, enemy'mizin çizgileri takip etmesini yazmayı kolaylaştırmak için importladık.
class Enemy(pg.sprite.Sprite): #burada enemy class'ımızı tanımlıyoruz, ayrıca enemy'lerin sprite sayılması için pygame'in sprite class'ından inheritance da aldık
    def __init__(self, waypoints, image): #normalde pos variable'ı bekliyordu bu class, waypoints kullanabilmek için içini güncelledik.
        pg.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0]) #burada waypoints'i baştaki pos variable'ımızı extractlemek için kullandığımızı söyledi.
        #en baştaki initial position'umuzu waypoints listesinin ilk elemanı yaptık ki hareketine çizginin başından başlasın.
        #şimdi enemy'nin çizgimizi gerçekten takip etmesini sağlamamız lazım.
        self.target_waypoint = 1 #bir sonraki waypoint'imizin waypoints listesi içerisindeki indexi olacak bu sayı :D
        self.speed = 2 #ileride farklı enemy türleri için farklı farklı hızlar yapacağımız bir speed variable'ı ekledik.
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos 

    def move(self): #burada enemy'nin hareket etmesini sağlayan method var, x ekseninde tick başına 1 piksel ilerliyor bu sayede #ARTIK YOK DFJKGNLSKDJFNLSD
        if self.target_waypoint < len(self.waypoints): #burada diyoruz ki gidilebilecek waypoint kaldığı sürece gideriz. (zaten öyle yapmıyor muyduk a)
            self.target = Vector2(self.waypoints[self.target_waypoint])  
            self.movement = self.target - self.pos 
        else: #tamam anladım özür dilerim russ.
            #enemy has reached the end of the path
            self.kill() #sprite'ı silmeye yarayan bir method bu da.
        dist = self.movement.length()
        #check if remaining distance is greter than enemy speed
        if dist >= self.speed: #bu normalde olması gereken koşulumuz. dolayısıyla normal hareketimizi bunun içine attık.
            self.pos += self.movement.normalize() * self.speed #adım büyüklüğünü speed'le çarptık ki o hızda gitsin.
        else:
            if dist != 0:
                #eğer bu if satırını eklemeseydik bu sefer de ikinci kez yolun sonuna geldiğimizde valueerror yiyecektik.
                self.pos += self.movement.normalize() * dist #eğer adımdan az kaldıysa direkt distance'ın kendisi kadar gideceği şekilde kodladık.
            #şimdi çizgi sonuna gelmiş enemy'mizin targetini diğer waypoint yapıyoruz.
            self.target_waypoint += 1
        self.rect.center = self.pos #self.rect'i de güncellemiş olduk.
        #şimdi bu sefer de waypointleri bitirdiği zaman valueerror yiyoruz T-T hayat çok güzel
        #bunu önlemek için de yeterince waypoint'imizin mevcut olduğundan emin olmamız lazımmış.
        #artık enemy ekranın bir ucundan diğerine gitmeyeceği için x += 1 kısmını sildik. sorry Egemen :D 
   

    def update(self): #burada update diye bir method ekledim, hareket methodunu çağırmak için kullanılıyor
        self.move()
