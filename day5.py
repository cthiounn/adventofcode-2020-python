import math

with open('data/my_input/5.in') as f:
    lines = [  line.strip() for line in f]

def calculate(poss , i, j):
    mn = i
    mx = j
    for l in poss:
        if l=='F' or l=='L':
            mn=mn
            mx= mx - math.ceil((mx-mn)/2)
        elif l=='B' or l=='R':
            mx=mx
            mn= mn+ math.ceil((mx-mn)/2)
        if mx==mn:
            return mn

def part1(vlines):
    s=list()
    for line in vlines:
        pos=line[0:7]
        post=line[7:]
        p=calculate(pos,0,127)
        j=calculate(post,0,7)
        ap=p*8+j
        s.append(ap)
        
    return max(s)

def part2(vlines):
    row=list()
    d=dict()
    for line in vlines:
        pos=line[0:7]
        post=line[7:]
        p=calculate(pos,0,127)
        j=calculate(post,0,7)
        row.append(p)
        ap=p*8+j
        d[ap]=(p,j)
    mm= max(row) 
    mm2= min(row) 
    aa = sorted([ k for k,v in d.items() if v[0]!= mm and v[0]!=mm2])
    for i in range(min(aa),max(aa)):
        if i not in aa:
            return i
    return 0

print(part1(lines)) #906
print(part2(lines)) #519