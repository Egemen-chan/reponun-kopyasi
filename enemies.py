import pygame as pg
from pygame.math import Vector2 #bu modülü, enemy'mizin çizgileri takip etmesini yazmayı kolaylaştırmak için importladık.
import math # bu modülü enemy'mizin yüzü gittiği yöne dönük olarak ilerlemesin sağlamak için importladık. 
class Enemy(pg.sprite.Sprite): #burada enemy class'ımızı tanımlıyoruz, ayrıca enemy'lerin sprite sayılması için pygame'in sprite class'ından inheritance da aldık
    def __init__(self, waypoints, image): #normalde pos variable'ı bekliyordu bu class, waypoints kullanabilmek için içini güncelledik.
        pg.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0]) #burada waypoints'i baştaki pos variable'ımızı extractlemek için kullandığımızı söyledi.
        #en baştaki initial position'umuzu waypoints listesinin ilk elemanı yaptık ki hareketine çizginin başından başlasın.
        self.target_waypoint = 1 #bir sonraki waypoint'imizin waypoints listesi içerisindeki indexi olacak bu sayı :D
        self.speed = 2 #ileride farklı enemy türleri için farklı farklı hızlar yapacağımız bir speed variable'ı ekledik.
        self.angle = 0 
        self.original_image = image #şimdi angle ve og image'ı, self.image variable'ını güncellemek için kullanabiliriz.
        self.image = pg.transform.rotate(self.original_image , self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos 

    def move(self): #burada enemy'nin hareket etmesini sağlayan method var, x ekseninde tick başına 1 piksel ilerliyor bu sayede #ARTIK YOK DFJKGNLSKDJFNLSD
        if self.target_waypoint < len(self.waypoints): #burada diyoruz ki gidilebilecek waypoint kaldığı sürece gideriz. (zaten öyle yapmıyor muyduk a)
            self.target = Vector2(self.waypoints[self.target_waypoint])  
            self.movement = self.target - self.pos 
        else: #tamam anladım özür dilerim russ.
            #enemy has reached the end of the path
            self.kill() #sprite'ı silmeye yarayan bir method bu da. yolun sonuna gelince artık oyunun kendisi error verip kapanmıyor, enemy yok oluyor sadece.
        dist = self.movement.length()
        #check if remaining distance is greater than enemy speed
        if dist >= self.speed: #bu normalde olması gereken koşulumuz. dolayısıyla normal hareketimizi bunun içine attık.
            self.pos += self.movement.normalize() * self.speed #adım büyüklüğünü speed'le çarptık ki o hızda gitsin.
        else:
            if dist != 0:
                #eğer bu if satırını eklemeseydik bu sefer de ikinci kez yolun sonuna geldiğimizde valueerror yiyecektik.
                self.pos += self.movement.normalize() * dist #eğer adımdan az kaldıysa direkt distance'ın kendisi kadar gideceği şekilde kodladık.
            self.target_waypoint += 1 #çizgi sonuna gelmiş enemy'mizin targetini diğer waypoint yapıyoruz.
        #artık enemy ekranın bir ucundan diğerine gitmeyeceği için x += 1 kısmını sildik. sorry Egemen :D 
    def update(self): #burada update diye bir method ekledim, hareket methodunu çağırmak için kullanılıyor
        self.move()
        self.rotate() #artık updat'İ çağırdığımızda rotate'İ de çağırmış olacağız.
    def rotate(self):
        #calculate the distance to next waypoint
        #ama bu sefer vektörel bir şekilde yapmayacağız bunu. daha doğrusu bulduğumuz değerleri vektör methodlarıyla işlemeyeceğiz. neyse.
        dist = self.target - self.pos
        #use the distance to calculate angle. TRİGONOMETRİK BİR ŞEYLER YAPACAĞIZ ŞİMDİ BURADA, GEBERMELİK.
        self.angle = math.degrees(math.atan2(-dist[1], dist[0])) #sırasıyla y ve x mesafe değerlerini verip açı hesaplattık, radyanı dereceye çevirdik
        #rotate image and update rectangle
        self.image = pg.transform.rotate(self.original_image , self.angle) #og image'imizi angle'a göre rotatelenmiş halini self.image'e eşitledik.
        self.rect = self.image.get_rect()
        self.rect.center = self.pos #rotate methoduna koyduğumuz için bu satırı move methodundan sildik.
        #yeni methodumuzu tanımladık, bunu bir yerlerde çağırmamız lazım.
    #dedi ki artık açımızı elde ettik, görselimizi rotateleyebiliriz.
    #ama aynı görseli tekrar tekrar rotatelersek görsel kalitesi düşermiş. bu yüzden sanırım bir image daha tanımlıyoruz yukarıda.
    
        
        
        
        
   

