import functools

direction = {'e':(1,0),'se':(1,1),'sw':(0,1),'w':(-1,0),'nw':(-1,-1),'ne':(0,-1)}
dxy= {(0,1),(1,1),(1,-1),(0,-1),(-1,-1),(-1,1)}
with open('data/my_input/24.in') as f:
    lines = [  line.strip() for line in f]

with open('data/test/24.test') as f2:
    tests = [  test.strip() for test in f2]

def part1(vlines):
    d=dict()
    for l in vlines:
        i=0
        li=[]
        while i < len(l):
            if l[i] in direction.keys():
                li.append(direction[l[i]])
                i+=1
            elif i+1 in range(len(l)) and l[i:i+2] in direction.keys():

                li.append(direction[l[i:i+2]])
                i+=2
            else:
                i+=1
        mytuple=functools.reduce(lambda a,b: (a[0]+b[0],a[1]+b[1]) , li)
        if mytuple in d:
            d[mytuple]=1+d[mytuple]
        else:
            d[mytuple]=1
    
    return sum([1 for k,v in d.items() if v%2==1 ])

def part2(vlines):
    d=dict()
    for l in vlines:
        i=0
        li=[]
        while i < len(l):
            if l[i] in direction.keys():
                li.append(direction[l[i]])
                i+=1
            elif i+1 in range(len(l)) and l[i:i+2] in direction.keys():

                li.append(direction[l[i:i+2]])
                i+=2
            else:
                i+=1
        mytuple=functools.reduce(lambda a,b: (a[0]+b[0],a[1]+b[1]) , li)
        if mytuple in d:
            d[mytuple]=1+d[mytuple]
        else:
            d[mytuple]=1
    for _ in range(100):
        d=play(d)
    return sum([1 for k,v in d.items() if v%2==1 ])

def play(d):
    d2=dict()
    done=set()
    for k,v in d.items():
        if k not in done :
            if v%2==1:
                if numblackneig(k,d)>2 or numblackneig(k,d)==0:
                    d2[k]=0
                else :
                    d2[k]=1
            else:
                if numblackneig(k,d)==2:
                    d2[k]=1
                else :
                    d2[k]=0
            done.add(k)
        
        for i,j in direction.items():
            u=(j[0]+k[0],j[1]+k[1])
            if u not in done and u not in d:
                if numblackneig(u,d)==2:
                    d2[u]=1
                done.add(u)
    return d2

def numblackneig(k,d):
    counter=0 
    for i in direction.values():
        if (k[0]+i[0],k[1]+i[1]) in d and d[(k[0]+i[0],k[1]+i[1])]%2==1:
            counter+=1
    return counter

print("test part1",part1(tests))
print("output part1",part1(lines)) #434
print("test part2",part2(tests))
print("output part2",part2(lines)) #3955