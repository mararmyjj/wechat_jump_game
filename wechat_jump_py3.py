# -*- coding: utf-8 -*-
import os
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image
import math


def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/autojump.png')
    os.system('adb pull /sdcard/autojump.png .')


def jump(x):
    #y=float(input("请输入系数="))
    y = (-0.0004*x)+1.7084
    press_time = x * y
    press_time = int(press_time)
    cmd = 'adb shell input swipe 320 410 320 410 ' + str(press_time)
    print("按压毫秒数为="+str(press_time))
    os.system(cmd)


fig = plt.figure()
pull_screenshot()
img = np.array(Image.open('autojump.png'))
im = plt.imshow(img, animated=True)

update = True
click_count = 0
cor = []


def update_data():
    return np.array(Image.open('autojump.png'))


def updatefig(*args):
    global update
    if update:
        time.sleep(0.8)
        pull_screenshot()
        im.set_array(update_data())
        update = False
    return im,

def on_click(event):
    global update
    global ix, iy
    global click_count
    global cor

    ix, iy = event.xdata, event.ydata
    coords = [(ix, iy)]
    #print('now = ', coords)
    cor.append(coords)

    click_count += 1
    if click_count > 1:
        click_count = 0
        cor1 = cor.pop()
        cor2 = cor.pop()

        distance = (cor1[0][0] - cor2[0][0])**2 + (cor1[0][1] - cor2[0][1])**2
        distance = math.sqrt(distance)
        print('distance = ', distance)
        jump(distance)
        update = True


fig.canvas.mpl_connect('button_press_event', on_click)
ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
plt.show()
