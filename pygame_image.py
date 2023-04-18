import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bird_img = pg.image.load("ex01/fig/3.png")
    bird_img = pg.transform.flip(bird_img, True, False)
    bird_img2 = pg.transform.rotozoom(bird_img, 10, 1.0)
    bird_list = [bird_img, bird_img2]

    tmr = 0
    bird_fly = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        if tmr % 100 == 0:
            bird_fly += 1
        screen.blit(bg_img, [0, 0])

        screen.blit(bird_list[bird_fly % 2], (300, 200))


        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()