#Liam Collins
#3/22/18
#monkeybanana.py - Best game ever

from ggame import *

#constants
ROWS = 25
COLS = 50
CELL_SIZE = 25

def moveRight(event):
    monkey.x += CELL_SIZE

if __name__ == '__main__':
    
    #colors
    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    
    jungleBox = RectangleAsset(CELL_SIZE*COLS,CELL_SIZE*ROWS,LineStyle(1,green),green)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    
    Sprite(jungleBox)
    monkey = Sprite(monkeyBox)
    
    App().listenKeyEvent('keydown','right arrow', moveRight)
    App().run()


