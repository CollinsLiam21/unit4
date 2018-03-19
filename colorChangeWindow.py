#Liam Collins
#3/9/18
#colorChangeWindow.py

from random import randint
from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)

def mouseClick(event):
    num = randint(1,3)
    if num == 1:
        Sprite(RectangleAsset(1200,800,LineStyle(1,red),red))
    elif num == 2:
        Sprite(RectangleAsset(1200,800,LineStyle(1,green),green))
    else:
        Sprite(RectangleAsset(1200,800,LineStyle(1,blue),blue))

App().listenMouseEvent('click',mouseClick)
App().run()
