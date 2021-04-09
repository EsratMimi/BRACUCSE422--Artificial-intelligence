import math

def HailstoneSequence(n,r):
    if n==1:
        r += 1
        print("Stopping Time: ", r)
        return r
    if n % 2==0:
        a=n/2
        print(a)
        r+=1
        HailstoneSequence(a,r)
    if n % 2 !=0:
         b=3*n+1
         print(b)
         r += 1
         HailstoneSequence(b,r)

h=int(input("Give a number: "))
x=HailstoneSequence(h,0)

