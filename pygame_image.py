import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    bird_img = pg.image.load("ex01/fig/3.png")
    bird_img = pg.transform.flip(bird_img, True, False)
    bird_img2 = pg.transform.rotozoom(bird_img, 10, 1.0)
    bird_list = [bird_img, bird_img2]

    tmr = 0
    bird_fly = 0
    bg_img_go = 0
    whe_i = 0
    x = 0
    y = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        bg_img_go = tmr % 1600
        whe_i = tmr % 3200

        if tmr % 100 == 0:
            bird_fly += 1

        screen.blit(bg_img, [-bg_img_go, 0])
        screen.blit(bg_img2, [1600 - whe_i, 0])
        screen.blit(bird_list[bird_fly % 2], (300, 200))


        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()