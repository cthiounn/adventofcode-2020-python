# from collections import Counter
# from collections import deque
# import asyncio
# import itertools
# import json
# import math
# import re
# import string
# import sys
# import unittest

with open('data/my_input/15.in') as f:
    lines = [  line.strip() for line in f]
    # dlines = { (x,y): cell for x,row in enumerate(lines) for y,cell in enumerate(row) }

with open('data/test/15.test') as f2:
    tests = [  test.strip() for test in f2]

def part1(vlines,num):
    d=dict()
    li= ''.join(vlines).split(",")
    r=1
    
    lastindex=dict()
    for i,j in enumerate(li):
        lastindex[int(j)]=i+1
        prev=int(j)
        r=i+1

    new=True
    while r!=num:
        r+=1
        if new :
            
            #speak
            prev=0
            
            #precalculate
            if prev in lastindex:
                d[prev]=r-lastindex[prev]
                new=False
            else:
                new=True
            
            
            #record
            lastindex[prev]=r

        else:
            #speak
            prev=d[prev]

            #precalculate
            if prev in lastindex:
                new=False
                d[prev]=r-lastindex[prev]
            else:
                new=True

            #record
            lastindex[prev]=r
        
    return prev


print("test part1",part1(tests,2020))
print("output part1",part1(lines,2020))
print("test part2",part1(tests,30000000))
print("output part2",part1(lines,30000000))