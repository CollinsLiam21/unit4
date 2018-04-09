#Liam Collins
#4/4/18
#graphicsTicTacToe.py

from ggame import *
from random import randint


def mouseClick(event):
    if event.x < 150 and event.y < 150:
        Sprite(x, (25,10))
        data['square1'] = 'x'
    elif event.x < 350 and event.y < 150:
        Sprite(x, (215,10))
        data['square2'] = 'x'
    elif event.x < 550 and event.y < 150:
        Sprite(x, (400,10))
        data['square3'] = 'x'
    elif event.x < 150 and event.y < 350:
        Sprite(x, (25,180))
        data['square4'] = 'x'
    elif event.x < 350 and event.y < 350:
        Sprite(x, (215,180))
        data['square5'] = 'x'
    elif event.x < 550 and event.y < 350:
        Sprite(x, (400,180))
        data['square6'] = 'x'
    elif event.x < 150 and event.y < 550:
        Sprite(x, (25,380))
        data['square7'] = 'x'
    elif event.x < 350 and event.y < 550:
        Sprite(x, (215,380))
        data['square8'] = 'x'
    elif event.x < 550 and event.y < 550:
        Sprite(x, (400,380))
        data['square9'] = 'x'
    computerTurn()
    

def computerTurn():
    n = randint(1,9)
    if n == 1:
        Sprite(o, (25,10))
        data['square1'] = 'o'
    elif n == 2:
        Sprite(o, (215,10))
        data['square2'] = 'o'
    elif n == 3:
        Sprite(o, (400,10))
        data['square3'] = 'o'
    elif n == 4:
        Sprite(o, (25,180))
        data['square4'] = 'o'
    elif n == 5:
        Sprite(o, (215,180))
        data['square5'] = 'o'
    elif n == 6:
        Sprite(o, (400,180))
        data['square6'] = 'o'
    elif n == 7:
        Sprite(o, (25,380))
        data['square7'] = 'o'
    elif n == 8:
        Sprite(o, (215,380))
        data['square8'] = 'o'
    elif n == 9:
        Sprite(o, (400,380))
        data['square9'] = 'o'
    else:
        computerTurn()


def isEmpty(numSquare):
    if numSquare == 1:
        if data['square1'] == 'x' or data['square1'] == 'o':
            return False
        else:
            return True
    if numSquare == 2:
        if data['square2'] == 'x' or data['square2'] == 'o':
            return False
        else:
            return True
    if numSquare == 3:
        if data['square3'] == 'x' or data['square3'] == 'o':
            return False
        else:
            return True
    if numSquare == 4:
        if data['square4'] == 'x' or data['square4'] == 'o':
            return False
        else:
            return True
    if numSquare == 5:
        if data['square5'] == 'x' or data['square5'] == 'o':
            return False
        else:
            return True
    if numSquare == 6:
        if data['square6'] == 'x' or data['square6'] == 'o':
            return False
        else:
            return True
    if numSquare == 7:
        if data['square7'] == 'x' or data['square7'] == 'o':
            return False
        else:
            return True
    if numSquare == 8:
        if data['square8'] == 'x' or data['square8'] == 'o':
            return False
        else:
            return True
    if numSquare == 9:
        if data['square9'] == 'x' or data['square9'] == 'o':
            return False
        else:
            return True
    

if __name__=='__main__':
    
    data = {}
    data['square1'] = 0
    data['square2'] = 0
    data['square3'] = 0
    data['square4'] = 0
    data['square5'] = 0
    data['square6'] = 0
    data['square7'] = 0
    data['square8'] = 0
    data['square9'] = 0
    
    
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
    
