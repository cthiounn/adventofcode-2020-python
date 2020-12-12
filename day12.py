import math
import re

with open('data/my_input/12.in') as f:
    lines = [  line.strip() for line in f]

with open('data/test/12.test') as f2:
    tests = [  test.strip() for test in f2]

def move(dir,num,angle,x,y):
    if dir =='F':
        x+=num*math.sin(math.radians(angle))
        y+=num *math.cos(math.radians(angle))
    elif dir =='L':
        angle-=num
    elif dir =='R':
        angle+=num
    elif dir =='W':
        y-=num
    elif dir =='N':
        x-=num
    elif dir =='S':
        x+=num
    elif dir =='E':
        y+=num
    return dir,num,angle,x,y
    
def part1(vlines):
    angle=0
    x,y=0,0
    for l in vlines:
        i=re.findall(r'(.)(\d+)',l)
        dir,num= i[0]
        num=int(num)
        dir,num,angle,x,y = move(dir,num,angle,x,y)
    return abs(x)+abs(y)

def move2(dir,num,x,y,xw,yw):
    an=math.radians(num)
    if dir =='F':
        x+=num*xw
        y+=num *yw
    elif dir =='L':
        xw , yw= xw*math.cos(an) - yw*math.sin(an) ,xw*math.cos(an) + yw*math.sin(an)
    elif dir =='R':
        xw , yw= xw*math.cos(an) + yw*math.sin(an) ,yw*math.cos(an) - xw*math.sin(an)
    elif dir =='W':
        yw-=num
    elif dir =='N':
        xw-=num
    elif dir =='S':
        xw+=num
    elif dir =='E':
        yw+=num
    return dir,num,x,y,xw,yw

def part2(vlines):
    x,y=0,0
    xw,yw=-1,10
    for l in vlines:
        i=re.findall(r'(.)(\d+)',l)
        dir,num= i[0]
        num=int(num)
        dir,num,x,y,xw,yw = move2(dir,num,x,y,xw,yw)
    return abs(x)+abs(y)

print(part1(tests))
print(part1(lines)) #362
print(part2(tests))
print(part2(lines)) #29895