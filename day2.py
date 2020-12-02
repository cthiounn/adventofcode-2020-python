from collections import Counter
import re

with open('data/my_input/2.in') as f:
    lines = [  line.strip() for line in f]

def test(l):
    least=l[0]
    most=l[1]
    lett=l[2]
    string=l[3]
    d=[ v for (k,v) in Counter(string).items() if k==lett] 
    if len(d) >=1 and int(least)<=int(d[0]) and int(d[0]) <= int(most) : 
        return True

    return False

def test2(l):
    least=l[0]
    most=l[1]
    lett=l[2]
    string=l[3] 
    if string[int(least)-1]==lett and string[int(most)-1]==lett:
        return False
    if string[int(least)-1]==lett or string[int(most)-1]==lett:
        return True
    return False

def part1(vlines):
    num=lambda s : re.findall('(\d+)-(\d+) (.): (.*)',s) 
    counter=0
    
    for line in vlines:
        l=num(line) 
        if test(l[0]):
             counter+=1
    return counter

def part2(vlines):
    num=lambda s : re.findall('(\d+)-(\d+) (.): (.*)',s) 
    counter=0
    
    for line in vlines:
        l=num(line)  
        if test2(l[0]):
             counter+=1 
    return counter

print(part1(lines))
print(part2(lines))