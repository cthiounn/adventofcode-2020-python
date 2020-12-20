# from collections import Counter
# from collections import deque
# import asyncio
# import itertools
# import json
# import math
import collections
import re
import copy
# import string
# import sys
# import unittest

with open('data/my_input/20.in') as f:
    lines = [  line.strip() for line in f]
    # dlines = { (x,y): cell for x,row in enumerate(lines) for y,cell in enumerate(row) }

with open('data/test/20.test') as f2:
    tests = [  test.strip() for test in f2]

def rotatelist(li1):
    k=len(li1)
    li2=[]

    for i in range(k):
        s=""
        for j in li1:
            s+=j[i]
        li2.append(s)
    return li2

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
    
    li1border=set([l1,r1,u1,d1,l1[::-1],r1[::-1],u1[::-1],d1[::-1]])
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
    print(ii,li)
    d2=collections.defaultdict(int)
    for aa,bb in d.items():
        for aa1,bb1 in d.items():
            if aa==aa1:
                continue
            print(aa,aa1)
            if matchanyborder(bb1,bb):
                print("ok")
                d2[aa1]+=1
                
        # if matchanyrotation(li,bb,matchup):
        #     print(ii,aa)
        # elif matchanyrotation(bb,li,matchup):
        #     print("d",ii,aa)
        # elif matchanyrotation(li,bb,matchleft):
        #     print("l",ii,aa)
        # elif matchanyrotation(bb,li,matchleft):
        #     print("r",ii,aa)
    
    print([i for (i,j) in d2.items() if j==2])
    return 0

def part2(vlines):
    return 0

print("test part1",part1(tests))
print("output part1",part1(lines))
# print("test part2",part2(tests))
# print("output part2",part2(lines))

def printmap(d2):
    xmin = min([x for x, y in d2])
    ymin = min([y for x, y in d2])
    xmax = max([x for x, y in d2])
    ymax = max([y for x, y in d2])

    # print(xmin, ymin, xmax, ymax)
    for i in range(xmin - 1, xmax + 2):
        sprint = ""
        for j in range(ymin - 1, ymax + 2):
            sprint += str(d2[i, j]) if (i, j) in d2 else "."
        print(sprint.replace("1", "O").replace("0", " "))