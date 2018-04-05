#Liam Collins
#4/4/18
#graphicsTicTacToe.py

from ggame import *

'''def isEmpty(numSquare):
    if numSquare == 1:'''



if __name__=='__main__':
    
    
    
    #color codes
    black = Color(0x000000,1)
    blue = Color(0x0000FF,1)
    
    #graphics
    boxLeft = RectangleAsset(100,100,LineStyle(1,black),blue)
    boxRight = RectangleAsset(100,100,LineStyle(1,black),blue)
    boxTop = RectangleAsset(525,25,LineStyle(1,black))
    boxBottom = RectangleAsset(525,25,LineStyle(1,black))
    x = TextAsset('X',fill=black,style='bold 100pt Times')
    o = TextAsset('O',fill=black,style='bold 100pt Times')
    
    Sprite(boxLeft, (0,0))
    Sprite(boxRight, (100,0))
    Sprite(boxRight, (200,0))
    Sprite(boxRight, (0,100))
    Sprite(boxRight, (100,100))
    Sprite(boxRight, (100,200))
    Sprite(boxRight, (200,100))
    Sprite(boxRight, (0,200))
    Sprite(boxRight, (200,200))
    Sprite(boxTop, (0,150))
    Sprite(boxBottom, (0,350))
    Sprite(x)
    Sprite(o, (200,0))
    
    App().run()
    
