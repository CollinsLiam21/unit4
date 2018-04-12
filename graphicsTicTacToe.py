#Liam Collins
#4/4/18
#graphicsTicTacToe.py

from ggame import *
from random import randint


def mouseClick(event):
    if data['gameOver'] == False:
        if (event.x < 150 and event.y < 150) and isEmpty(1) == True:
            Sprite(x, (25,10))
            data['square1'] = 'x'
        elif (event.x < 350 and event.y < 150) and isEmpty(2) == True:
            Sprite(x, (215,10))
            data['square2'] = 'x'
        elif (event.x < 550 and event.y < 150) and isEmpty(3) == True:
            Sprite(x, (400,10))
            data['square3'] = 'x'
        elif (event.x < 150 and event.y < 350) and isEmpty(4) == True:
            Sprite(x, (25,180))
            data['square4'] = 'x'
        elif (event.x < 350 and event.y < 350) and isEmpty(5) == True:
            Sprite(x, (215,180))
            data['square5'] = 'x'
        elif (event.x < 550 and event.y < 350) and isEmpty(6) == True:
            Sprite(x, (400,180))
            data['square6'] = 'x'
        elif (event.x < 150 and event.y < 550) and isEmpty(7) == True:
            Sprite(x, (25,380))
            data['square7'] = 'x'
        elif (event.x < 350 and event.y < 550) and isEmpty(8) == True:
            Sprite(x, (215,380))
            data['square8'] = 'x'
        elif (event.x < 550 and event.y < 550) and isEmpty(9) == True:
            Sprite(x, (400,380))
            data['square9'] = 'x'
        if winner() == True:
            print('We have a winner!')
            data['gameOver'] == True
        else:
            computerTurn()
            if winner() == True:
                print('We have a winner!')
                data['gameOver'] = True
        if fullBoard() == True and winner() == False:
            print('We have a tie!')
        

def computerTurn():
    n = randint(1,9)
    if n == 1 and isEmpty(1) == True:
        Sprite(o, (25,10))
        data['square1'] = 'o'
    elif n == 2 and isEmpty(2) == True:
        Sprite(o, (215,10))
        data['square2'] = 'o'
    elif n == 3 and isEmpty(3) == True:
        Sprite(o, (400,10))
        data['square3'] = 'o'
    elif n == 4 and isEmpty(4) == True:
        Sprite(o, (25,180))
        data['square4'] = 'o'
    elif n == 5 and isEmpty(5) == True:
        Sprite(o, (215,180))
        data['square5'] = 'o'
    elif n == 6 and isEmpty(6) == True:
        Sprite(o, (400,180))
        data['square6'] = 'o'
    elif n == 7 and isEmpty(7) == True:
        Sprite(o, (25,380))
        data['square7'] = 'o'
    elif n == 8 and isEmpty(8) == True:
        Sprite(o, (215,380))
        data['square8'] = 'o'
    elif n == 9 and isEmpty(9) == True:
        Sprite(o, (400,380))
        data['square9'] = 'o'
    elif fullBoard() == False:
        computerTurn()
    


def isEmpty(numSquare):
    if numSquare == 1:
        if data['square1'] == 'x' or data['square1'] == 'o':
            return False
        else:
            return True
    elif numSquare == 2:
        if data['square2'] == 'x' or data['square2'] == 'o':
            return False
        else:
            return True
    elif numSquare == 3:
        if data['square3'] == 'x' or data['square3'] == 'o':
            return False
        else:
            return True
    elif numSquare == 4:
        if data['square4'] == 'x' or data['square4'] == 'o':
            return False
        else:
            return True
    elif numSquare == 5:
        if data['square5'] == 'x' or data['square5'] == 'o':
            return False
        else:
            return True
    elif numSquare == 6:
        if data['square6'] == 'x' or data['square6'] == 'o':
            return False
        else:
            return True
    elif numSquare == 7:
        if data['square7'] == 'x' or data['square7'] == 'o':
            return False
        else:
            return True
    elif numSquare == 8:
        if data['square8'] == 'x' or data['square8'] == 'o':
            return False
        else:
            return True
    elif numSquare == 9:
        if data['square9'] == 'x' or data['square9'] == 'o':
            return False
        else:
            return True

def fullBoard():
    if isEmpty(1) == False and isEmpty(2) == False and isEmpty(3) == False and isEmpty(4) == False and isEmpty(5) == False and isEmpty(6) == False and isEmpty(7) == False and isEmpty(8) == False and isEmpty(9) == False:
        return True
        data['gameOver'] = True
    else:
        return False

def winner():
    if data['square1'] == 'x' and data['square2'] == 'x' and data['square3'] == 'x':
        return True
    elif data['square4'] == 'x' and data['square5'] == 'x' and data['square6'] == 'x':
        return True
    elif data['square7'] == 'x' and data['square8'] == 'x' and data['square9'] == 'x':
        return True
    elif data['square1'] == 'x' and data['square4'] == 'x' and data['square7'] == 'x':
        return True
    elif data['square2'] == 'x' and data['square5'] == 'x' and data['square8'] == 'x':
        return True
    elif data['square3'] == 'x' and data['square6'] == 'x' and data['square9'] == 'x':
        return True
    elif data['square1'] == 'x' and data['square5'] == 'x' and data['square9'] == 'x':
        return True
    elif data['square3'] == 'x' and data['square5'] == 'x' and data['square7'] == 'x':
        return True
    elif data['square1'] == 'o' and data['square2'] == 'o' and data['square3'] == 'o':
        return True
    elif data['square4'] == 'o' and data['square5'] == 'o' and data['square6'] == 'o':
        return True
    elif data['square7'] == 'o' and data['square8'] == 'o' and data['square9'] == 'o':
        return True
    elif data['square1'] == 'o' and data['square4'] == 'o' and data['square7'] == 'o':
        return True
    elif data['square2'] == 'o' and data['square5'] == 'o' and data['square8'] == 'o':
        return True
    elif data['square3'] == 'o' and data['square6'] == 'o' and data['square9'] == 'o':
        return True
    elif data['square1'] == 'o' and data['square5'] == 'o' and data['square9'] == 'o':
        return True
    elif data['square3'] == 'o' and data['square5'] == 'o' and data['square7'] == 'o':
        return True
    else:
        return False
    

if __name__=='__main__':
    
    
    
    #dictionary
    data = {}
    data['square1'] = ''
    data['square2'] = ''
    data['square3'] = ''
    data['square4'] = ''
    data['square5'] = ''
    data['square6'] = ''
    data['square7'] = ''
    data['square8'] = ''
    data['square9'] = ''
    data['gameOver'] = False
    
    
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
    
