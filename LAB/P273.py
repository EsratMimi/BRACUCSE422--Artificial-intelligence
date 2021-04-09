


n=3


def dotProduct( vect_A, vect_B ):
    pro=0
    for i in range (0,n):
        pro+= vect_A[i] * vect_B[i]

    return pro

def crossProduct ( vect_A, vect_B, cross ) :
    cross.append(vect_A[1] * vect_B[2] - vect_A[2] * vect_B[1])
    cross.append(vect_A[0] * vect_B[2] - vect_A[2] * vect_B[0])
    cross.append(vect_A[0] * vect_B[1] - vect_A[1] * vect_B[0])


vect_A = [3,-5,4]
vect_B = [2,6,5]
cross = []


print("Dot Product : ",dotProduct(vect_A,vect_B))

print("Cross Product : ", end="")
crossProduct(vect_A,vect_B,cross)

for i in range(0, n):
    print(cross[i], end=" ")


