#Liam Collins
#4/5/18
#quiz4.py

def count(b):
    for i in range(1,b+1):
        print(i)

def excitedPrint(string):
    print(string.upper(),'!!!')

def firstLetter(word):
    for ch in word:
        return ch
        break 

def repeats(a,b,c):
    if a == b:
        return True
    elif a == c:
        return True
    elif b == c:
        return True
    else:
        return False

count(4)
excitedPrint('i love programming')
print(firstLetter('smeds'))
print(repeats('smeds',5,'smeds'))


