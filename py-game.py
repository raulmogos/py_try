import pygame as pg

pg.init()

win = pg.display.set_mode((500, 500))

pg.display.set_caption('first game')


x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

while run:

    pg.time.delay(100)

    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            run = False

    pg.draw.rect(win, (255,155,0), (x,y,width,height))
    pg.display.update()

pygame.quit()
