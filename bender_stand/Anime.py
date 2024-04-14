# import pprint
# from random import randrange, choice
import os
import shutil

import pygame as pg
import time
import Audio
# from Vosk_trunc import start as st
# READY = True
import DATAS as dat
tex = ""

import shutil
import os


def copy_and_replace(source_path, destination_path):
    if os.path.exists(destination_path):
        os.remove(destination_path)
    shutil.copy2(source_path, destination_path)

# def timing():
#     global START_TIME
#     # print("--- %s seconds ---" % (time.time() - START_TIME))
#     tim = (float(time.time()) - float(START_TIME))
#     # print(tim)
#     return tim


dat.STATUS = True
START_TIME = 0.0
FPS = 60
WIDTHH = 480*2.5
WIDTH = 480
HEIGHT = 640
HEIGHTT = HEIGHT + (HEIGHT // 8)
FRAME = 0
# SHAG = 0


def set_image_size(img, height=-1, width=-1):
    import pygame as pg
    if width < 0 and height < 0:
        return img
    if height < 0:
        k = img.get_size()
        return pg.transform.scale(img, (width, round(k[1] / (k[0] / width))))
    elif width < 0:
        k = img.get_size()
        return pg.transform.scale(img, (round(k[0] / (k[1] / height)), height))
    else:
        return pg.transform.scale(img, (width, height))


def start(imgi, bender='voice', voice=True, anal=True):

    global FPS, WIDTH, HEIGHT, FRAME, START_TIME
    FRAME = 0

    if not dat.window:
        pg.init()
        window = pg.display.set_mode((WIDTHH, HEIGHT + (HEIGHT // 8)))
        dat.window = window
    else:
        window = dat.window
    if not dat.clock:
        clock = pg.time.Clock()
        dat.clock = clock
    else:
        clock = dat.clock

    logo = pg.image.load('datas/backgrounds/ico.ico')  # directory of logo
    pg.display.set_icon(logo)
    pg.display.set_caption("BENDER")


    play = True
    CHAR = '_'
    START_TIME = time.time()
    time.sleep(0.2)
    if voice:
        Audio.PLAY_AUDIO()


    body = pg.image.load('datas/'+bender+'.png')
    img = pg.image.load('datas/' + imgi + '.png')
    while play:
        window.fill((255, 255, 255))

        body = set_image_size(body, height=HEIGHT)
        body_rect = body.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        window.blit(body, body_rect)


        img = set_image_size(img, height=HEIGHTT - ((HEIGHTT // 18)*2))
        window.blit(img, (WIDTHH - int(img.get_width()) - (HEIGHTT // 18), HEIGHTT // 18))



        # print((time.time() - START_TIME) , Audio.get_length())
        if (time.time() - START_TIME) >= Audio.get_length():
            if anal:
                img = pg.image.load('datas/begin.png')
                img = set_image_size(img, height=HEIGHTT - ((HEIGHTT // 18) * 2))
                window.blit(img, (WIDTHH - int(img.get_width()) - (HEIGHTT // 18), HEIGHTT // 18))
            # body = pg.image.load('datas/stop.png')
            # body = set_image_size(body, height=HEIGHT)
            # body_rect = body.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            # window.blit(body, body_rect)
            print("ok")
            copy_and_replace('pysto.wav', 'test.wav')
            dat.STATUS = True
            return


        FRAME += 1

        # print(clock.get_fps())
        pg.display.update()
        clock.tick(FPS)
    # pg.quit()
# try:
#     start(st())
# except:
#     pass
