import pygame as pg # wrote as pg so that whenever we need to call a pygame func., we can js write pg
import json
from turret import Turret
from enemies import Enemy
from world import World
import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))

pg.init() # we are initializing the module here

#let's create our clock
clock = pg.time.Clock() #now we put this under the main loop of our game.

#now we need to open a window, so we assign it to a variable
screen = pg.display.set_mode((300+960,960)) #butonları ekleyebilmek için oyun ekranını büyüttük. 1260 yazmaya usendim
#unless we tell the code to keep the window open, running this code will only cause a momentary pop-up of our window.
#so we create a loop in order to keep our window open.
#then we change the name of our window
pg.display.set_caption("Tower Defense")

#load images
map_image =   pg.image.load("levels/level_map.png").convert_alpha() 
enemy_image = pg.image.load('assets/enemies/enemy_1.png').convert_alpha() #bunun amacı enemy oluşturduğumuz zaman ekrana vereceğimiz image'ı koda tanıtmak
cursor_turret = pg.image.load("assets/turrets/cursor_turret.png").convert_alpha() #bu kodla turret koyacağımız zamanki cursor image'ı programa ekledik
#düğmelerin görsellerini ekliyorum :3
buy_turret_image = pg.image.load("assets/buttons/buy_turret.png").convert_alpha()
cancel_image = pg.image.load("asstes/buttons/cancel.png").convert_alpha()


#load json data for level UwU
with open("levels/level.tmj") as file:
    world_data = json.load(file)

#create world ^-^
world = World(world_data , map_image)
world.process_data()

#esasında bu fonksiyon ile oyunumuzun tile game olmasını sağlıyoruz
#Turret class'ının özelliklerini de kullanarak turret'ların istediğimiz her yere değil her 64 pixele bir koyulmasını sağlıyoruz
#önce 64'e bölüp sonra da kalanını alıp 64'le çarpınca küsuratları gidiyor bu sayede her 64 pixelde bir oluyor
def create_turret(mouse_pos):
    mouse_tile_x = mouse_pos[0] // 64
    mouse_tile_y = mouse_pos[1] // 64
    mouse_tile_num = (mouse_tile_y * 15) + mouse_tile_x #burada böyle bir şekilde yazmamızın sebebi JSON formatı böyle koordinat kaydediyormuş
    if world.map_tiles[mouse_tile_num] == 25: #eğer kullanacağımız tile sadece çimenin olduğu bir tile'sa bir sonraki check'e geçeriz
        #burada turret koyduğumuz yer boş mu onu kontrol ediyor boşsa koyuyor
        space_is_free = True
        for turret in turret_group:
             if (mouse_tile_x, mouse_tile_y) == (turret.tile_x, turret.tile_y):
                  space_is_free = False
        if space_is_free == True:
            new_turret = Turret(cursor_turret, mouse_tile_x, mouse_tile_y) #burada new_turret dedim çok fazla turret'lı değişken vardı çünkü
            turret_group.add(new_turret)

#burada group üretiyoruz enemyler ve turretler için
enemy_group = pg.sprite.Group()
turret_group = pg.sprite.Group()

#ilk enemy'i yaptık ve onu enemy_group grubuna ekledik

#şimdi artık enemy'lerimizin oluşturduğumuz waypoint'leri takip etmelerini sağlamamız lazım.
enemy = Enemy(world.waypoints, enemy_image) #manuel olarak yazdığımız koordinatı waypoint'le değiştiriyoruz bunun için.
enemy_group.add(enemy)

print(enemy)

run = True
while run:  #as long as the run variable is true, the code will keep executing itself in a loop. brief moment --> forever
    clock.tick(60)
    
    #burada arkaplan rengi ekledim, bir de bu olmazsa karakter hareket ettikçe eski halleri ekranı kaplıyor >~<
    screen.fill("goldenrod4")

    #draw level
    world.draw(screen)

    #enemy'nin takip edeceği yolu artık ekrana çizmemiz gerekmediği için sildim :pp

    #artık bütün düşmanları hareket ettirecek method ile hareketi sağlayabiliriz ^_^
    enemy_group.update()
    
    #enemyleri ekrana yansıtıyoruz burada artık :3
    enemy_group.draw(screen)
    turret_group.draw(screen)
    
    # to keep the loop from being stuck in forever, we use an event handler.
    for event in pg.event.get():
        #quit program
        if event.type == pg.QUIT:
            run = False #now, whenever we press x the window can be closed. it won't stay open forever and ever. 

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pg.mouse.get_pos()
            #turret koyduğumuz yer oyun ekranının içinde mi onu kontrol ediyor, içindeyse turret yerleştiriyor ^w^
            if mouse_pos[0]<960 and mouse_pos[1]<960:
                    create_turret(mouse_pos)
            

    pg.display.flip() #güncellemeleri ekranda gösteriyoruz  
    
pg.quit() #bunu neden yaptığımızı anlamadım, bu satırı yazmadan önce de pencere açılıyordu ve kapat deyince kapanıyordu? :PP

#next thing we need to do is limiting the framerate, meaning it should run at 
#the same speed no matter how powerful the computer is. so we go under the first init to create a clock.
