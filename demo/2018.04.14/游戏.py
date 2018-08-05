#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/7/13 0013 9:47
# @author  : zza
# @Email   : 740713651@qq.com

import sys
from random import choice, random
from time import sleep

import pygame as pg
from pygame.locals import QUIT

gg = 255, 165, 0
green = 0, 255, 0
red = 255, 0, 0

pg.init()
scr = pg.display.set_mode((600, 600))
pg.display.set_caption('接球大战')
ft = pg.font.SysFont('stkaiti', 24)
zt3 = zt1 = pg.font.SysFont('stkaiti', 40)

kais = pg.image.load("./游戏图片/kais.jpg").convert()

beij = pg.image.load('./游戏图片/QQ.jpg').convert()
biaoq = []
for i in range(1, 41):
    biaoq.append(pg.image.load('./游戏图片/表情/' + str(i) + '.png').convert_alpha())

x = 231
y = 30
vx = 1
vy = 1
jf = 2
zf = 0
lv = 3
s = False
bq = biaoq[-1]
sudu = [1, 2, 3]
while True:
    scr.blit(kais, (0, 0))
    for eve in pg.event.get():
        if eve.type == QUIT:
            exit()
    mx, my = pg.mouse.get_pos()
    but1, but2, but3 = pg.mouse.get_pressed()
    x = x + vx
    y = y + vy
    scr.blit(bq, (x - 25, y - 25))
    if x < 25 or x > 575:
        vx = -vx
    if y < 25 or y > 575:
        vy = -vy
    if but1:
        if abs(mx - 284) < 84 and abs(my - 478) < 36:
            break
    pg.display.update()


def nextqiu():
    x = int(random() * 500 + 50)
    y = 30
    vx = choice([-3, -2, -1, 0, 1, 2, 3])
    vy = choice([1, 2, 3])
    jf = vx + vy


def prt(font, text, x, y, color=(255, 255, 255)):
    img = font.render(text, True, color)
    scr.blit(img, (x, y))


x = 231
y = 30
vx = 1
vy = 1

while True:
    scr.blit(beij, (0, 0))
    for eve in pg.event.get():
        if eve.type == QUIT:
            sys.exit()
    mx, my = pg.mouse.get_pos()
    pg.draw.rect(scr, green, (mx, 570, 100, 30), 0)
    # 画球
    scr.blit(bq, (x - 25, y - 25))
    x = x + vx
    y = y + vy
    if x > 575 or x < 25:
        vx = -vx
    if y > 550 and abs(mx + 50 - x) < 50:
        zf = zf + jf
        x = int(random() * 500 + 50)
        y = 30
        vx = choice([-3, -2, -1, 0, 1, 2, 3])
        vy = choice([1, 2, 3])
        jf = vx + vy
        sleep(0.25)
        bq = choice(biaoq)
    elif y > 550 and abs(mx + 50 - x) > 50:
        lv = lv - 1
        prt(zt3, '没接到', x, y - 40, color=(255, 0, 0))
        x = int(random() * 500 + 50)
        y = 30
        vx = choice([-3, -2, -1, 0, 1, 2, 3])
        vy = choice([1, 2, 3])
        bq = choice(biaoq)
        jf = vx + vy
        s = True
    if lv < 0:
        break
    sleep(0.005)
    prt(ft, '生命值 :' + str(lv), 452, 20, color=(255, 0, 0))
    prt(ft, '分数 :' + str(zf), 452, 50, color=green)
    pg.display.update()
    if s:
        sleep(1)
        s = False

hua = pg.image.load('./游戏图片/画.jpg').convert()
scr.blit(hua, (0, 0))
zt1 = pg.font.SysFont('stkaiti', 100)
zt2 = pg.font.SysFont('stkaiti', 50)
prt(zt1, '游戏结束', 70, 150, color=red)
prt(zt2, '得分 :' + str(zf), 80, 310, color=red)
pg.display.update()

# 作者：未尽之业
# 链接：https://www.zhihu.com/question/266742251/answer/387397296
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



