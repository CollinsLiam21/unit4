#Liam Collins
#3/9/18
#functionDemo.py - How to write our own functions

def hw():
    print('Hello, World')
    
def double(thingToDouble):
    print(thingToDouble*2)

def bigger(a,b):
    if a>b:
        print(a)
    else:
        print(b)

def slope(x1, y1, x2, y2):
    print((y2-y1)/(x2-x1))

slope(2,3,4,5)
bigger(100,5)
bigger('smedinghoff','christo')
bigger(True,False)
#double(12) #test of double function
#double('w') #test of double with string
#double(True) #test of double with a boolean
