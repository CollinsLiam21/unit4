#Liam Collins
#4/4/18
#graphicsTicTacToe.py

from ggame import *

'''def isEmpty(numSquare):
    if numSquare == 1:'''

def mouseClick(event):
    if event.x < 150 and event.y < 350:
        Sprite(x, (10,10))

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
    Sprite(o, (200,0))
    
    App().run()
    
