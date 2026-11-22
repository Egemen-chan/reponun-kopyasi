import pygame as pg # wrote as pg so that whenever we need to call a pygame func., we can js write pg
from enemies import Enemy
from world import World
import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))

pg.init() # we are initializing the module here

#let's create our clock
clock = pg.time.Clock() #now we put this under the main loop of our game.

#now we need to open a window, so we assign it to a variable
screen = pg.display.set_mode((500,500))
#unless we tell the code to keep the window open, running this code will only cause a momentary pop-up of our window.
#so we create a loop in order to keep our window open.
#then we change the name of our window
pg.display.set_caption("Tower Defense")

#load images
map_image =   pg.image.load("levels/level_map.png").convert_alpha() 
enemy_image = pg.image.load('assets/enemies/enemy_1.png').convert_alpha() #bunun amacı enemy oluşturduğumuz zaman ekrana vereceğimiz image'ı koda tanıtmak

#create world ^-^
world = World(map_image)
#burada group üretiyoruz enemyler için
enemy_group = pg.sprite.Group()

#şimdi waypointler için bir liste oluşturuyoruz. içerisinde koordinat tuple'ları olan bir liste oluyor bu.
waypoints = [
    (100,100),
    (400,200),
    (400,100),
    (200,300),
] #waypoint'leri visualiselamak için ekrana çizeceğiz sanırım.

#ilk enemy'i yaptık ve onu enemy_group grubuna ekledik

#şimdi artık enemy'lerimizin oluşturduğumuz waypoint'leri takip etmelerini sağlamamız lazım.
enemy = Enemy(waypoints, enemy_image) #manuel olarak yazdığımız koordinatı waypoint'le değiştiriyoruz bunun için.
enemy_group.add(enemy)

print(enemy)

run = True
while run:  #as long as the run variable is true, the code will keep executing itself in a loop. brief moment --> forever
    clock.tick(60)
    
    #burada arkaplan rengi ekledim, bir de bu olmazsa karakter hareket ettikçe eski halleri ekranı kaplıyor >~<
    screen.fill("goldenrod4")

    #draw level
    world.draw(screen)

    #draw enemy path
    pg.draw.lines(screen, "grey0", False, waypoints) #nereye çizdiğimiz, rengi, son argüman waypoints listesini çiziyor oluşumuz.
    # (üçüncü argüman da içi kapalı bir şekil olup olmadığını soruyor.  çizgi olduğu için False.)
    
    #artık bütün düşmanları hareket ettirecek method ile hareketi sağlayabiliriz ^_^
    enemy_group.update()
    
    #enemyleri ekrana yansıtıyoruz burada artık :3
    enemy_group.draw(screen)
    
    # to keep the loop from being stuck in forever, we use an event handler.
    for event in pg.event.get():
        #quit program
        if event.type == pg.QUIT:
            run = False #now, whenever we press x the window can be closed. it won't stay open forever and ever. 
            
    pg.display.flip() #güncellemeleri ekranda gösteriyoruz  
    
pg.quit() #bunu neden yaptığımızı anlamadım, bu satırı yazmadan önce de pencere açılıyordu ve kapat deyince kapanıyordu? :PP

#next thing we need to do is limiting the framerate, meaning it should run at 
#the same speed no matter how powerful the computer is. so we go under the first init to create a clock.

