
def HammingDist (st,str):
    i=0
    count=0
    ch  = split(st)
    cha  = split(str)
    while i < len(st) :
        if ch[i] != cha[i] :
            count=count+1
        i=i+1

    return count


def split(word):
    return list(word)


print(HammingDist("cse422labisfun","cse471labisfun"))
