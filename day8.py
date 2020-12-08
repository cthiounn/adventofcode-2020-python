import re

with open('data/my_input/8.in') as f:
    lines = [  line.strip() for line in f]

def part1(vlines):
    i=0
    acc=0
    seen=[]
    while i<len(vlines):
        line=vlines[i]
        if i in seen: return acc
        else: seen.append(i)
        j=re.findall(r'-?\d+',line)
        if 'acc' in line: 
            acc+= int(j[0])
            i+=1
        elif 'jmp' in line: i+= int(j[0])
        elif 'nop' in line: i+=1
    return 0

def tryreplace(vlines):
    i=0
    acc=0
    seen=[]
    while i<len(vlines):
        line=vlines[i]
        if i in seen: return False
        else: seen.append(i)
        j=re.findall(r'-?\d+',line)
        if 'acc' in line: 
            acc+= int(j[0])
            i+=1
        elif 'jmp' in line: i+= int(j[0])
        elif 'nop' in line: i+=1
    return True

def calculate(vlines):
    i=0
    acc=0
    seen=[]
    while i<len(vlines):
        line=vlines[i]
        if i in seen: return acc
        else: seen.append(i)
        j=re.findall(r'-?\d+',line)
        if 'acc' in line: 
            acc+= int(j[0])
            i+=1
        elif 'jmp' in line: i+= int(j[0])
        elif 'nop' in line: i+=1
    return acc

def part2(vlines):
    for i in range(len(vlines)):
        if 'nop' in vlines[i]:
            newlines=vlines.copy()
            newlines[i]=vlines[i].replace('nop','jmp')
            if tryreplace(newlines):
                return calculate(newlines)
        elif 'jmp'in vlines[i]:
            newlines=vlines.copy()
            newlines[i]=vlines[i].replace('jmp','nop')
            if tryreplace(newlines):
                return calculate(newlines)
    return 0

print(part1(lines))
print(part2(lines))