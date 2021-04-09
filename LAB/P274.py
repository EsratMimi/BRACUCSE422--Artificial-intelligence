
import math
def rea (n,s):
    a = (s * math.degrees(math.atan(3.1416 / n))) / 2
    return a

def area (n,s,h):

    ar=(n*s*rea(n,s))/2

    return ar

def heigth (n,s,h):
    l=math.sqrt(h*h + rea(n,s)*rea(n,s))
    return l

def calV (n,s,h):
    v=(area (n,s,h)*h) /3
    return v

def calS (n,s,h):
    s=area (n,s,h) + (n*s*heigth(n,s,h))/2
    return s

n=6
h= 80
s=10
a=rea (n,s)
print(calV(n,s,h))
print(calS(n,s,h))




