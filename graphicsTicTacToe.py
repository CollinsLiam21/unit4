#Liam Collins
#4/4/18
#graphicsTicTacToe.py

from ggame import *

'''def isEmpty(numSquare):
    if numSquare == 1:'''
        

if __name__=='__main__':
    
    
    
    #color codes
    black = Color(0x000000,1)
    
    #graphics
    boxLeft = RectangleAsset(25,525,LineStyle(1,black))
    boxRight = RectangleAsset(25,525,LineStyle(1,black))
    boxTop = RectangleAsset(525,25,LineStyle(1,black))
    boxBottom = RectangleAsset(525,25,LineStyle(1,black))
    line1 = LineAsset(50,50,LineStyle(1,black))
    line2 = LineAsset(-50,50,LineStyle(1,black))
    
    Sprite(boxLeft, (150,0))
    Sprite(boxRight, (350,0))
    Sprite(boxTop, (0,150))
    Sprite(boxBottom, (0,350))
    Sprite(line1)
    Sprite(line2, (0,0))
    
    App().run()
    
