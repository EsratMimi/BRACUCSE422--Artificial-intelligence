import math

def DoubleFactorial(h):
    if h==2:
        return 2
    if h==1:
        return 1
    else:
        return h*DoubleFactorial(h-2)
n=int(input("Give a number please!:"))
x=DoubleFactorial(n)
print(x)




