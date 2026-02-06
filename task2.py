import pygame as pg

class Mario:
    def __init__(self):
        self.screen = pg.display.set_mode((700, 700))
        self.image = pg.image.load('images/super-mario.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def blitme(self):        
        
        while True:           
            self.screen.fill('white')
            self.screen.blit(self.image, self.rect)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
            
            pg.display.flip()
if __name__ == '__main__':
    pg.init()
    mario = Mario()
    mario.blitme()