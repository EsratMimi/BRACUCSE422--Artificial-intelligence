t=open('Tree data.txt','r')
max1=0
max2=0

for line in t:
    r=line.split('  ')
    if float(r[2]) > max1:
        max1=float(r[2])
    if float(r[3]) > max2:
        max2=float(r[3])

print('Tallest tree(s) are:')
t=open('Tree data.txt','r')
for line in t:
    r=line.split('  ')
    if max2 == float(r[3]):
        print(r[0])
print('Tree(s) with greatest diameter are:')
t=open('Tree data.txt','r')
for line in t:
    r=line.split('  ')
    if max1 == float(r[2]):
        print(r[0])

