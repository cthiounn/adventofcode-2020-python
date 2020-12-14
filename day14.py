import re

with open('data/my_input/14.in') as f:
    lines = [  line.strip() for line in f]

with open('data/test/14.test') as f2:
    tests = [  test.strip() for test in f2]

with open('data/test/14_2.test') as f3:
    tests2 = [  test.strip() for test in f3]

def calculate(number,mask):
    bi="{0:b}".format(int(number))
    bi=bi.zfill(36)
    mys=""
    for ind,i in enumerate(mask):
        if "X" not in i:
            mys+=i
        else:
            mys+=bi[ind]
    return int(mys,2)

def part1(vlines):
    mask=''
    num=lambda s: re.findall(r'\d+',s)
    d=dict()
    ss=0
    for l in vlines:
        if 'mask' in l:
            mask=l.split(' ')[2]
        else:
            pos,number=num(l)
            d[pos]=calculate(number,mask)
    ss+=sum(d.values())
    return ss

def part2(vlines):
    mask=''
    num=lambda s: re.findall(r'\d+',s)
    d=dict()
    for l in vlines:
        if 'mask' in l:
            mask=l.split(' ')[2]
        else:
            pos,number=num(l)
            if pos not in d:
                write(d,calculate2(number,mask,"{0:b}".format(int(pos)).zfill(36)),int(number))
            else:
                write(d,calculate2(number,mask,"{0:b}".format(d[pos]).zfill(36)),int(number))
    return sum([v for v in d.values()])

def write(d,s,number):
    num=s.count("X")
    if num==0:
        d[int(s,2)]=number
    else:
        xc=s
        x=s
        write(d,x.replace('X','0',1),number)
        write(d,xc.replace('X','1',1),number)

 
def calculate2(number,mask,number2):
    bi="{0:b}".format(int(number))
    bi=bi.zfill(36)
    mys=""
    for ind,i in enumerate(mask):
        if "X"  in i:
            mys+="X"
        elif "1" in i:
            mys+="1"
        elif "0" in i:
            mys+=number2[ind]
    return mys

print("test part1",part1(tests))
print("output part1",part1(lines)) #10885823581193
print("test part2",part2(tests2))
print("output part2",part2(lines)) #3816594901962