def Factorial(n):
    prod=1
    while n>1:
        prod=prod*n
        n-=1
    return prod
n=0
while 1:
    sum=0
    r=Factorial(n)
    e=str(r)
    t=e.split()

    for i in range(len(t)):
        sum=sum+int(t[i])

    if r%sum!=0:
        break
    else:
        n+=1

print('The smallest integer is: ',n)





