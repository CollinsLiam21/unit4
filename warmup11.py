#Liam Collins
#3/26/18
#warmup11.py

def prime(x):
    i = 2
    while i < x:
        if x%i == 0:
            return False
        i += 1
    return True

print(prime(7))
