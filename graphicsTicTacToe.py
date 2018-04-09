#Liam Collins
#4/4/18
#graphicsTicTacToe.py

from ggame import *
from random import randint


def mouseClick(event):
    if event.x < 150 and event.y < 150:
        Sprite(x, (25,10))
        square1 = 'x'
    elif event.x < 350 and event.y < 150:
        Sprite(x, (215,10))
        square2 = 'x'
    elif event.x < 550 and event.y < 150:
        Sprite(x, (400,10))
        square3 = 'x'
    elif event.x < 150 and event.y < 350:
        Sprite(x, (25,180))
        square4 = 'x'
    elif event.x < 350 and event.y < 350:
        Sprite(x, (215,180))
        square5 = 'x'
    elif event.x < 550 and event.y < 350:
        Sprite(x, (400,180))
        square6 = 'x'
    elif event.x < 150 and event.y < 550:
        Sprite(x, (25,380))
        square7 = 'x'
    elif event.x < 350 and event.y < 550:
        Sprite(x, (215,380))
        square8 = 'x'
    elif event.x < 550 and event.y < 550:
        Sprite(x, (400,380))
        square9 = 'x'
    computerTurn()
    

def computerTurn():
    n = randint(1,9)
    if n == 1:
        Sprite(o, (25,10))
    elif n == 2:
        Sprite(o, (215,10))
    elif n == 3:
        Sprite(o, (400,10))
    elif n == 4:
        Sprite(o, (25,180))
    elif n == 5:
        Sprite(o, (215,180))
    elif n == 6:
        Sprite(o, (400,180))
    elif n == 7:
        Sprite(o, (25,380))
    elif n == 8:
        Sprite(o, (215,380))
    elif n == 9:
        Sprite(o, (400,380))



def isEmpty(numSquare):
    if numSquare == 1:
        if square1 == 'x' or square1 == 'o':
            return False
        else:
            return True
    

if __name__=='__main__':
    
    data = {}
    data['isEmpty'] = True
    
    data[square1] = 0
    square2 = 0
    square3 = 0
    square4 = 0
    square5 = 0
    square6 = 0
    square7 = 0
    square8 = 0
    square9 = 0
    
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
    
