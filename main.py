import pygame as pg # wrote as pg so that whenever we need to call a pygame func., we can js write pg
from enemies import Enemy
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

enemy_image = pg.image.load('assets/enemies/enemy_1.png').convert_alpha()

#burada group üretiyoruz enemyler için
enemy_group = pg.sprite.Group()

enemy = Enemy((200,300), enemy_image)
enemy_group.add(enemy)

print(enemy)

run = True
while run:  #as long as the run variable is true, the code will keep executing itself in a loop. brief moment --> forever
    clock.tick(60)

     #enemyleri ekrana veriyoruz burada
    enemy_group.draw(screen)
    
    # to keep the loop from being stuck in forever, we use an event handler.
    for event in pg.event.get():
        #quit program
        if event.type == pg.QUIT:
            run = False #now, whenever we press x the window can be closed. it won't stay open forever and ever.
            
    #güncellemeleri ekranda gösteriyoruz
    pg.display.flip()    
pg.quit() #bunu neden yaptığımızı anlamadım, bu satırı yazmadan önce de pencere açılıyordu ve kapat deyince kapanıyordu? :PP

#next thing we need to do is limiting the framerate, meaning it should run at 
#the same speed no matter how powerful the computer is. so we go under the first init to create a clock.

