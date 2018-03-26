#Liam Collins
#3/19/18
#printSquares.py

def printSquares(numRows,numCols):
    for i in range(1,numRows+1):
        print('+','- - + '*numCols)
        print('|     '*(numCols+1))
    print('+','- - + '*numCols)

printSquares(5,3)

