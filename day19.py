import re

with open('data/my_input/19.in') as f:
    lines = [  line.strip() for line in f]

with open('data/test/19.test') as f2:
    tests = [  test.strip() for test in f2]

def part1and2(vlines,part2):
    dd=dict()
    myinput=list()
    for l in vlines:
        if ":" in l :
            a,b=l.split(":")
            aaaa=list()
            if "|" in b:
                c,d=b.split("|")
                aaaa.append(list(map(int,c.strip().split(" "))))
                aaaa.append(list(map(int,d.strip().split(" "))))
            else:
                b=b.replace('\"','')
                v=b.strip().split(" ")
                if "a" not in v and "b" not in v:
                    aaaa.append(list(map(int,v)))
                else:
                    aaaa.append(v)
            dd[int(a)]=aaaa
        else:
            myinput.append(l)
    if part2:
        dd[8]=[[42],[42,8]]
        dd[11]=[[42,31],[42,11,31]]

    def verify(l, licheck):
        if not licheck: 
            return len(l)==0
        else:
            checkkey=licheck.pop(0)
            nextcheck = dd[checkkey]
            if nextcheck ==[['a']] or nextcheck==[['b']]: 
                return l.startswith(nextcheck[0][0])and verify(l[1:],licheck)
            else: 
                return any(verify(l,n+licheck) for n in nextcheck)
    return sum(verify(l,[0]) for l in myinput)

print("test part1",part1and2(tests,False)) 
print("output part1",part1and2(lines,False)) #139
print("test part2",part1and2(tests,True))
print("output part2",part1and2(lines,True)) #289