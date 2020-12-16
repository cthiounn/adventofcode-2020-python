import re

with open('data/my_input/16.in') as f:
    lines = [  line.strip() for line in f]

with open('data/test/16.test') as f2:
    tests = [  test.strip() for test in f2]

with open('data/test/16_2.test') as f3:
    tests2 = [  test.strip() for test in f3]


def part1(vlines):
    di=dict()
    
    myT=False
    otT=False
    limyt=[]
    liott=[]
    num=lambda s: re.findall(r'\d+',s)
    for l in vlines:
        if otT:
            for i in num(l):
                liott.append(int(i))
        elif myT:
            for i in num(l):
                limyt.append(int(i))
        elif "your ticket:" not in l and l:
            a,b,c,d= num(l)
            cl= l.split(':')[0]
            di[cl]=(int(a),int(b),int(c),int(d)) 

        
        if "your ticket:" in l :
            myT=True
        elif "nearby tickets:" in l :
            otT=True
    lierr=[]
    for i in liott:
        test=False
        for v in di.values():
            a,b,c,d = v
            if a<=i<=b or c<=i<=d:
                test=True
        if not test:
            lierr.append(i)

    return sum(lierr)

def part2(vlines):
    di=dict()
    myT=False
    otT=False
    limyt=[]
    liott=[]
    num=lambda s: re.findall(r'\d+',s)
    for l in vlines:
        if otT:
            liott.append(num(l))
        elif myT:
            for i in num(l):
                limyt.append(int(i))
        elif "your ticket:" not in l and l:
            a,b,c,d= num(l)
            cl= l.split(':')[0]
            di[cl]=(int(a),int(b),int(c),int(d)) 

        if "your ticket:" in l :
            myT=True
        elif "nearby tickets:" in l :
            otT=True

    ligoodott=[]
    for i in liott:
        discard=False
        for j in i:
            test=False
            for v in di.values():
                a,b,c,d = v
                if a<=int(j)<=b or c<=int(j)<=d:
                    test=True
            if not test:
                discard=True
        if not discard:
            ligoodott.append(i)
        
    di2=dict()
    numberk=len(di)
    excludeindex=[]
    while len(di2)<numberk: 
        chosen=""
        for k,v in di.items():
            a,b,c,d=v
            if 0<=matcheees2(a,b,c,d,ligoodott,excludeindex):
                r=matcheees2(a,b,c,d,ligoodott,excludeindex)
                di2[k]=r
                chosen=k
                excludeindex.append(r)
        if chosen in di:
            del di[chosen]
    ind=[v for k,v in di2.items() if "departure" in k]
    results=1
    for i in range(len(limyt)):
        if i in ind:
            results*=limyt[i]
    return results

def matcheees2(a,b,c,d,li,exc):
    li2=[]
    for i in range(len(li[0])):
        if i not in exc and matcheees(a,b,c,d,li,i):
            li2.append(i)
    if len(li2)==1:
        return li2[0]
    return -1

def matcheees(a,b,c,d,li,index):
    matche=True
    for i in li:
        if not(a<=int(i[index])<=b or c<=int(i[index])<=d):
            matche=False
    return matche

print("test part1",part1(tests))
print("output part1",part1(lines)) #29878
print("test part2",part2(tests2))
print("output part2",part2(lines)) #855438643439