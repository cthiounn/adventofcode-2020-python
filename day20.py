import collections
import re
import copy
import functools

with open('data/my_input/20.in') as f:
    lines = [  line.strip() for line in f]

with open('data/test/20.test') as f2:
    tests = [  test.strip() for test in f2]

def rotatelist(li1):
    k=len(li1[0])
    li2=[]
    for i in range(k):
        s=""
        for j in li1:
            s+=j[i]
        li2.append(s[::-1])
    return li2

def fliplist(li1):
    return [s[::-1] for s in li1]

def itr(li1,i):
    li2=copy.deepcopy(li1)
    for _ in range(i):
        li2=rotatelist(li2)
    return li2


def matchanyrotation(li1,li2,fff):
    return any(fff(li1,itr(li2,j)) for j in range(4))

def matchleft(li1,li2):
    s=""
    for i in li1:
        s+=i[0]
    m=""
    for j in li2:
        m+=j[-1]

    return s==m

def matchup(li1,li2):
    return li1[0]==li2[-1]

def matchanyborder(li1,li2):
    l=""
    r=""
    for j in li2:
        l+=j[0]
        r+=j[-1]
    u=li2[0]
    d=li2[-1]
    l1=""
    r1=""
    for j1 in li1:
        l1+=j1[0]
        r1+=j1[-1]
    u1=li1[0]
    d1=li1[-1]
    li2border=set([l,r,u,d,l[::-1],r[::-1],u[::-1],d[::-1]])
    li1border=set([l1,r1,u1,d1]) 
    return len(li1border.intersection(li2border))>=1

def part1(vlines):
    num=lambda l: re.findall(r'\d+',l)
    d=dict()
    li=[]
    first=True
    ii=0
    for l in vlines:
        a= num(l)
        if a:
            if first:
                first=False
                ii=a[0]
            else:
                d[ii]=li
                ii=a[0]
                li=[]
        elif l:
            li.append(l)
    d[ii]=li
    d2=collections.defaultdict(int)
    for aa,bb in d.items():
        for aa1,bb1 in d.items():
            if aa==aa1:
                continue
            if matchanyborder(bb1,bb):
                d2[aa1]+=1
    mul=lambda a,b:a*b
    bordertiles=[int(i) for (i,j) in d2.items() if j==2]
    return functools.reduce(mul,bordertiles)

def matchwithneighbor(d,i,j,puzzle):
    leftok=(i,j-1) not in d or  ((i,j-1) in d and not (matchleft(d[(i,j-1)],puzzle)))
    rightok=(i,j+1) not in d or((i,j+1) in d and not (matchleft(puzzle,d[(i,j+1)])))
    upok=(i-1,) not in d or((i-1,j) in d and not (matchup(d[(i-1,j)],puzzle)))
    downok=(i+1,j) not in d or((i+1,j) in d and not (matchup(puzzle,d[(i+1,j)])))
    return leftok and rightok and upok and downok
    
def part2(vlines):
    num=lambda l: re.findall(r'\d+',l)
    d=dict()
    li=[]
    first=True
    ii=0
    for l in vlines:
        a= num(l)
        if a:
            if first:
                first=False
                ii=a[0]
            else:
                d[ii]=li
                ii=a[0]
                li=[]
        elif l:
            li.append(l)
    d[ii]=li
    d2=collections.defaultdict(int)
    for aa,bb in d.items():
        for aa1,bb1 in d.items():
            if aa==aa1:
                continue
            if matchanyborder(bb1,bb):
                d2[aa1]+=1
    idpickoneangle=[i for (i,j) in d2.items() if j==2][1] 
    queue=set()
    queue.add(idpickoneangle)
    pos=dict()
    pos[idpickoneangle]=(0,0)
    dfinalpict=dict()
    dfinalpict[(0,0)]=d[idpickoneangle]
    placed=set([idpickoneangle])
    while queue:
        
        idwork=queue.pop()
        i,j = pos[idwork]
        liwork=dfinalpict[(i,j)]
        for aa1,bb1 in d.items():
            if idwork==aa1:
                continue
            if aa1 in placed:
                continue
            found=False
            cc1=fliplist(bb1)
            for _ in range(4):
                if  matchup(bb1,liwork) and matchwithneighbor(dfinalpict,i+1,j,bb1):
                    dfinalpict[(i+1,j)]=bb1
                    pos[aa1]=(i+1,j)
                    if aa1 not in placed:
                        queue.add(aa1)
                        placed.add(aa1)
                        found=True
                elif matchleft(bb1,liwork) and matchwithneighbor(dfinalpict,i,j+1,bb1):
                    dfinalpict[(i,j+1)]=bb1
                    pos[aa1]=(i,j+1)
                    if aa1 not in placed:
                        queue.add(aa1)
                        placed.add(aa1)
                    found=True
                elif  matchup(cc1,liwork) and matchwithneighbor(dfinalpict,i+1,j,cc1):
                    dfinalpict[(i+1,j)]=cc1
                    pos[aa1]=(i+1,j)
                    if aa1 not in placed:
                        queue.add(aa1)
                        placed.add(aa1)
                        found=True
                elif matchleft(cc1,liwork) and matchwithneighbor(dfinalpict,i,j+1,cc1):
                    dfinalpict[(i,j+1)]=cc1
                    pos[aa1]=(i,j+1)
                    if aa1 not in placed:
                        queue.add(aa1)
                        placed.add(aa1)
                    found=True
                elif not found:
                    bb1=rotatelist(bb1)
                    cc1=rotatelist(cc1)

    for i,llll in dfinalpict.items():
        dfinalpict[i]=removeborder(llll)
    myfinallist=[]
    xmin = min([x for x, y in dfinalpict])
    ymin = min([y for x, y in dfinalpict])
    xmax = max([x for x, y in dfinalpict])
    ymax = max([y for x, y in dfinalpict])
    for i in range(xmin , xmax + 1):
        mylist=[]
        for j in range(ymin , ymax + 1):
            li =[]
            if (i,j) in dfinalpict:
                li=dfinalpict[(i,j)]
            mylist=fusli(mylist,li)
        myfinallist=verticalfusli(myfinallist,mylist)

    numhash="".join(myfinallist).count('#')
    myfinallist=rotatelist(rotatelist(rotatelist((myfinallist))))
    
    monster=lambda s:re.search(r'#....##....##....###',s)
    bottommonster=lambda s:re.search(r'.#..#..#..#..#..#...',s)
    count=0
    for i,llllll in enumerate(myfinallist):
        ss=llllll
        while(monster(ss)):
            startindexofmonster=monster(ss).start()
            if i+1 in range(len(myfinallist)) and i-1 in range(len(myfinallist)):
                lup=myfinallist[i-1][startindexofmonster:][18]
                ldown=myfinallist[i+1][startindexofmonster:startindexofmonster+21]
                if lup=='#' and bottommonster(ldown):
                    count+=1
            ss="0"*(startindexofmonster+1) +ss[startindexofmonster+1:]
    return numhash-15*count

def removeborder(li):
    m=len(li)
    ll=li[1:m-1]
    ll=rotatelist(ll)
    m=len(ll)
    ll=ll[1:m-1]
    for _ in range(3):
        ll=rotatelist(ll)
    return ll


def printmap(d2):
    xmin = min([x for x, y in d2])
    ymin = min([y for x, y in d2])
    xmax = max([x for x, y in d2])
    ymax = max([y for x, y in d2])

    print(xmin, ymin, xmax, ymax)
    myfinallist=[]
    for i in range(xmin , xmax + 1):
        mylist=[]
        for j in range(ymin , ymax + 1):
            li =[]
            if (i,j) in d2:
                li=d2[(i,j)]
            mylist=fusli(mylist,li)
        myfinallist=verticalfusli(myfinallist,mylist)
    print(printm(myfinallist))

def verticalfusli(li1,li2):
    li=[]
    if not li1:
        return li2
    if not li2:
        return li1
    li.extend(li1)
    li.extend(li2)
    return li

def fusli(li1,li2):
    li=[]
    if not li1:
        return li2
    if not li2:
        return li1
    for i in range(len(li1)):
        li.append(li1[i]+li2[i])
    return li
def printm(ll):
    for i in ll:
        print(i)

print("test part1",part1(tests))
print("output part1",part1(lines)) #11788777383197
#print("test part2",part2(tests))
print("output part2",part2(lines)) #2242


