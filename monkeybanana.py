#Liam Collins
#3/22/18
#monkeybanana.py - Best game ever

from ggame import *

#constants
ROWS = 20
COLS = 40
CELL_SIZE = 25

def moveRight(event):
    monkey.x += CELL_SIZE
    if monkey.x == banana.x and monkey.y == banana.y:
        print('got it')

def moveLeft(event):
    monkey.x -= CELL_SIZE

def moveDown(event):
    monkey.y += CELL_SIZE
    
def moveUp(event):
    monkey.y -= CELL_SIZE

if __name__ == '__main__':
    
    #colors
    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    yellow = Color(0xFFFF00,1)
    
    jungleBox = RectangleAsset(CELL_SIZE*COLS,CELL_SIZE*ROWS,LineStyle(1,green),green)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    bananaBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,yellow),yellow)
    
    Sprite(jungleBox)
    monkey = Sprite(monkeyBox)
    banana = Sprite(bananaBox,(CELL_SIZE*COLS/2,CELL_SIZE*ROWS/2))
    
    App().listenKeyEvent('keydown','right arrow', moveRight)
    App().listenKeyEvent('keydown','left arrow', moveLeft)
    App().listenKeyEvent('keydown','down arrow', moveDown)
    App().listenKeyEvent('keydown','up arrow', moveUp)
    App().run()


