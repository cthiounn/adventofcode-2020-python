# from collections import Counter
# from collections import deque
# import asyncio
# import itertools
# import json
# import math
import re
import functools
# import string
# import sys
# import unittest

with open('data/my_input/22.in') as f:
    lines = [  line.strip() for line in f]
    # dlines = { (x,y): cell for x,row in enumerate(lines) for y,cell in enumerate(row) }

with open('data/test/22.test') as f2:
    tests = [  test.strip() for test in f2]

def part1(vlines):
    num=lambda s: re.findall(r'\d+',s)
    mul=lambda a,b : a*b
    
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
    
    li1=d[1]
    li2=d[2]

    while li1 and li2 :
        n1=li1.pop(0)
        n2=li2.pop(0)
        if n1<n2:
            li2.append(n2)
            li2.append(n1)
        elif n1>n2:
            li1.append(n1)
            li1.append(n2)
    print(li1,li2)
    
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
    return counter

def part2(vlines):
    return 0

print("test part1",part1(tests))
print("output part1",part1(lines))
# print("test part2",part2(tests))
# print("output part2",part2(lines))