import re

with open('data/my_input/14.in') as f:
    lines = [  line.strip() for line in f]

with open('data/test/14.test') as f2:
    tests = [  test.strip() for test in f2]

with open('data/test/14_2.test') as f3:
    tests2 = [  test.strip() for test in f3]

def to_bit_and_pad(s):
    return "{0:b}".format(int(s)).zfill(36)

def calculate(number,mask,bpart1):
    bi=to_bit_and_pad(number)
    mys=""
    for ind,i in enumerate(mask):
            if bpart1 :
                if "X" not in i:
                    mys+=i
                else:
                    mys+=bi[ind]
            else:
                if "X"  in i:
                    mys+="X"
                elif "1" in i:
                    mys+="1"
                elif "0" in i:
                    mys+=bi[ind]
    return mys


def part1and2(vlines,bpart1):
    mask=''
    num=lambda s: re.findall(r'\d+',s)
    d=dict()
    for l in vlines:
        if 'mask' in l:
            mask=l.split()[2]
        else:
            pos,number=num(l)
            if bpart1:
                d[pos]=int(calculate(number,mask,True),2)
            else:
                if pos not in d:
                    write(d,calculate(pos,mask,False),int(number))
                else:
                    write(d,calculate(d[pos],mask,False),int(number))
    return sum(d.values())

def write(d,s,number):
    num=s.count("X")
    if num==0:
        d[int(s,2)]=number
    else:
        write(d,s.replace('X','0',1),number)
        write(d,s.replace('X','1',1),number)

 


print("test part1",part1and2(tests,True))
print("output part1",part1and2(lines,True)) #10885823581193
print("test part2",part1and2(tests2,False))
print("output part2",part1and2(lines,False)) #3816594901962