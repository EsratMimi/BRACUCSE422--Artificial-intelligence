

def HailstoneNumbers (Num, count) :
    print(Num , end = " ")
    if (Num == 1 and count == 0 ) :
        return count;
    elif (Num==1 and count != 0 ) :
        count=count+1
    elif (Num % 2 == 0 ) :
        count+=1
        c = HailstoneNumbers((int)(Num/2),count)

    elif (Num % 2 != 0) :
        count+=1
        c = HailstoneNumbers((3*Num) + 1, count)

    return count

N=5
print(HailstoneNumbers(N,0))
