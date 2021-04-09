
def fact (i) :
    if ( i == 0) :
        return 1
    elif i == 1  :
        return 1
    else :
        return i * fact(i-1)


def sum (s):
    temp=s
    rem=0
    for range in (1,3) :
        div=s/100
        rem = rem+ s%100
    return rem



for range in (1,10):

    n=fact(range)
    m=sum(n)
    if (m/6 == 0) :
        print(range)

