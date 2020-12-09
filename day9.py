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

with open('data/my_input/9.in') as f:
    lines = [  line.strip() for line in f]

def correct(i , li):
    for j in li:
        for f in li :
            if f!=j and int(f)+int(j)==i:
                return True
    return False
def part1(vlines):
    i=25
    while i<len(vlines):
        num=int(vlines[i])
        li=vlines[i-25:i]
        if not correct(num,li):
            return num
        i+=1
    return 0

def part2(vlines):
    mmin=0
    mmax=0
    j=0
    while j<len(vlines):
        i=0
        while i <len(vlines):
            li=vlines[j:j+i]
            li3=vlines[j-1:j]
            li2=vlines[j-i:j+i]
            if sum(map(int,li))==10884537:
                mmin=min(li)
                mmax=max(li)
                return int(mmin)+int(mmax)
            if sum(map(int,li3))==10884537:
                mmin=min(li3)
                mmax=max(li3)
                return int(mmin)+int(mmax)
            if sum(map(int,li2))==10884537:
                mmin=min(li2)
                mmax=max(li2)
                return int(mmin)+int(mmax)
            i+=1
        j+=1

    return mmin+mmax


print(part1(lines)) #10884537
print(part2(lines)) #1261309