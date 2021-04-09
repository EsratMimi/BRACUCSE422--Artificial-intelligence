
i = [ 56, 78 , 96 , 74 , 2 , 58]

small = i[0]
large = i[0]

for a in i:
    if a > large:
        large = a
        
for a in i:
    if a < small:
        small = a
        
print ("Sum of Small and Large: " , small + large)
