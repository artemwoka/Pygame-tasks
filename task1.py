import pygame as pg

pg.init()
clock = pg.time.Clock()


screen = pg.display.set_mode(
(700, 700)
         )
while True:
    screen.fill((0,0,255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    
    pg.display.flip()