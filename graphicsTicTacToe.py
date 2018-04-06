#Liam Collins
#4/4/18
#graphicsTicTacToe.py

from ggame import *
from random import randint

'''def isEmpty(numSquare):
    if numSquare == 1:'''

def mouseClick(event):
    i=0
    while i<=9:
        if event.x < 150 and event.y < 150:
            Sprite(x, (25,10))
            i += 1
        elif event.x < 350 and event.y < 150:
            Sprite(x, (215,10))
            i += 1
        elif event.x < 550 and event.y < 150:
            Sprite(x, (400,10))
            i += 1
        elif event.x < 150 and event.y < 350:
            Sprite(x, (25,180))
            i += 1
        elif event.x < 350 and event.y < 350:
            Sprite(x, (215,180))
            i += 1
        elif event.x < 550 and event.y < 350:
            Sprite(x, (400,180))
            i += 1
        elif event.x < 150 and event.y < 550:
            Sprite(x, (25,380))
            i += 1
        elif event.x < 350 and event.y < 550:
            Sprite(x, (215,380))
            i += 1
        elif event.x < 550 and event.y < 550:
            Sprite(x, (400,380))
            i += 1
    

def computerTurn():
    if event.x < 1000 and event.y < 1000:
        n = randint(1,9)
        if n == 1:
            Sprite(o, (25,10))
            i += 1
        elif n == 2:
            Sprite(x, (215,10))
            i += 1
        elif n == 3:
            Sprite(x, (400,10))
            i += 1
        elif n == 4:
            Sprite(x, (25,180))
            i += 1
        elif n == 5:
            Sprite(x, (215,180))
            i += 1
        elif n == 6:
            Sprite(x, (400,180))
            i += 1
        elif n == 7:
            Sprite(x, (25,380))
            i += 1
        elif n == 8:
            Sprite(x, (215,380))
            i += 1
        elif n == 9:
            Sprite(x, (400,380))
            i += 1
    

if __name__=='__main__':
    
    
    
    #color codes
    black = Color(0x000000,1)
    blue = Color(0x0000FF,1)
    
    #graphics
    boxLeft = RectangleAsset(25,525,LineStyle(1,black),black)
    boxRight = RectangleAsset(25,525,LineStyle(1,black),black)
    boxTop = RectangleAsset(525,25,LineStyle(1,black))
    boxBottom = RectangleAsset(525,25,LineStyle(1,black))
    x = TextAsset('X',fill=black,style='bold 100pt Times')
    o = TextAsset('O',fill=black,style='bold 100pt Times')
    
    Sprite(boxRight, (150,0))
    Sprite(boxRight, (350,0))
    Sprite(boxTop, (0,150))
    Sprite(boxBottom, (0,350))
    '''Sprite(o, (200,0))'''
    
    App().listenMouseEvent('click',mouseClick)
    App().run()
    
