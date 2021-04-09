a="thermi"
b="tretwi"
r=0
for i in range(len(a)):
    if a[i]!=b[i]:
        r+=1
print("Hamming Distance:",r)