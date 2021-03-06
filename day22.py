import re
import copy

with open('data/my_input/22.in') as f:
    lines = [  line.strip() for line in f]

with open('data/test/22.test') as f2:
    tests = [  test.strip() for test in f2]

def part1and2(vlines):
    num=lambda s: re.findall(r'\d+',s)
    li=[]
    d=dict()
    first=True
    for l in vlines:
        if "Player" in l: 
            if first:
                first=False
                idplayer=int(num(l)[0])
            d[idplayer]=li
            idplayer=int(num(l)[0])
            li=[]
        elif num(l):
            li.append(int(num(l)[0]))
    d[idplayer]=li
    
    li1=copy.deepcopy(d[1])
    li2=copy.deepcopy(d[2])

    while li1 and li2 :
        n1=li1.pop(0)
        n2=li2.pop(0)
        if n1<n2:
            li2.append(n2)
            li2.append(n1)
        elif n1>n2:
            li1.append(n1)
            li1.append(n2)
    counter=0
    if li2:
        counter=0
        c=len(li2)
        for j,n in  enumerate(li2):
            counter+= n* (c-j)
    if li1:
        counter=0
        c=len(li1)
        for j,n in  enumerate(li1):
            counter+= n* (c-j)
    print("Part 1 :",counter) 

    li1=d[1]
    li2=d[2]
 
    playedgame=dict()
    counter=0
    if playsubgame(li1,li2,playedgame)==1:
        c=len(li2)
        for j,n in  enumerate(li2):
            counter+= n* (c-j)
    else:
        c=len(li1)
        for j,n in  enumerate(li1):
            counter+= n* (c-j)
    print("Part 2 :",counter) 

def playsubgame(li1,li2,playedgame):
    seen=[]
    while li1 and li2 :
        ssli1="".join(map(str,li1))
        ssli2="".join(map(str,li2))
        if ssli1+"!"+ssli2 in seen:
            return -1
        else:
            seen.append(ssli1+"!"+ssli2)
        n1=li1.pop(0)
        n2=li2.pop(0)
        ln1=len(li1)
        ln2=len(li2)
        if n1<=ln1 and n2<=ln2 and ln1!=0 and ln2!=0:
            sli1="".join(map(str,li1[:n1]))
            sli2="".join(map(str,li2[:n2]))
            if (sli1,sli2) not in  playedgame:
                playedgame[(sli1,sli2)]=playsubgame(li1[:n1],li2[:n2],playedgame)
            
            if playedgame[(sli1,sli2)]==1:
                li2.append(n2)
                li2.append(n1)
            else:
                li1.append(n1)
                li1.append(n2)

        else:
            if n1<n2:
                li2.append(n2)
                li2.append(n1)
            elif n1>n2:
                li1.append(n1)
                li1.append(n2)
    if li1:
        return -1
    if li2:
        return 1




part1and2(tests)
part1and2(lines) # 32824 36515