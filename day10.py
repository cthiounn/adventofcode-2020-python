from collections import Counter
# from collections import deque
# import asyncio
# import itertools
# import json
# import math
import re
# import string
# import sys
# import unittest
import collections
import math

with open('data/my_input/10.in') as f:
    lines = [line.strip() for line in f]

def part1(vlines):
    li=list()
    for line in vlines:
        li.append(int(line))
    li.append(max(li)+3)
    li2=sorted(li)
    chargingoutlet=0
    
    counter1=0
    counter2=0
    counter3=0
    while li2:
        element=li2.pop(0)
        if abs(element-chargingoutlet)==1:
            counter1+=1
            chargingoutlet=element
        elif abs(element-chargingoutlet)==2:
            counter2+=1
            chargingoutlet=element
        elif abs(element-chargingoutlet)==3:
            counter3+=1
            chargingoutlet=element
    return counter1*counter3

def part2(vlines):
    myli=list()
    for line in vlines:
        myli.append(int(line))
    device=max(myli)+3 
    li2=sorted(myli)
    d=dict()
    def recursive(mylist,a,b): 
        if a in d:
            return d[a]
        counter=0
        if b-a<=3:
            counter+=1
        if  len(mylist)>0:
            i=mylist[0]
            counter += recursive(mylist[1:], a, b)
            if i - a <= 3:
                counter += recursive(mylist[1:], i, b)
        d[a] = counter
        return counter
    
    return recursive(li2,0,device)
 
print(part1(lines)) #1625
print(part2(lines)) #3100448333024

#3100448333024