#Liam Collins
#3/26/18
#warmup11.py

def prime(x):
    i = 1
    while i <= x/2:
        if x%i == 0:
            return('True')
        i += 1

prime(3)
