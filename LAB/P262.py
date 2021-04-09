BannedList=['whales','excited','championship']
f=open('TASK5.txt','r+')
q =open('TASK5OUT.txt', 'w')

for line in f:

    t=line.split(' ')
    for i in t:
        w=""

        for x in BannedList:
            if i.lower() == x:
               for a in range(len(i)):
                    w+="*"
               q = open('TASK5OUT.txt','r+')
               q.write(line.replace(i, w))
               q.close()
            else:
                continue




