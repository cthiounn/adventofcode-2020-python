import math
import re

with open('data/my_input/12.in') as f:
    lines = [  line.strip() for line in f]

with open('data/test/12.test') as f2:
    tests = [  test.strip() for test in f2]

def move(direction,num,angle,x,y):
    if direction =='F':
        x+=num*math.sin(math.radians(angle))
        y+=num *math.cos(math.radians(angle))
    elif direction =='L':
        angle-=num
    elif direction =='R':
        angle+=num
    elif direction =='W':
        y-=num
    elif direction =='N':
        x-=num
    elif direction =='S':
        x+=num
    elif direction =='E':
        y+=num
    return direction,num,angle,x,y
    
def part1(vlines):
    angle=0
    x,y=0,0
    for l in vlines:
        i=re.findall(r'(.)(\d+)',l)
        direction,num= i[0]
        num=int(num)
        direction,num,angle,x,y = move(direction,num,angle,x,y)
    return abs(x)+abs(y)

def move2(direction,num,x,y,xw,yw):
    an=math.radians(num)
    if direction =='F':
        x+=num*xw
        y+=num *yw
    elif direction =='L':
        xw , yw= xw*math.cos(an) - yw*math.sin(an) ,xw*math.cos(an) + yw*math.sin(an)
    elif direction =='R':
        xw , yw= xw*math.cos(an) + yw*math.sin(an) ,yw*math.cos(an) - xw*math.sin(an)
    elif direction =='W':
        yw-=num
    elif direction =='N':
        xw-=num
    elif direction =='S':
        xw+=num
    elif direction =='E':
        yw+=num
    return direction,num,x,y,xw,yw

def part2(vlines):
    x,y=0,0
    xw,yw=-1,10
    for l in vlines:
        i=re.findall(r'(.)(\d+)',l)
        direction,num= i[0]
        num=int(num)
        direction,num,x,y,xw,yw = move2(direction,num,x,y,xw,yw)
    return abs(x)+abs(y)

print(part1(tests))
print(part1(lines)) #362
print(part2(tests))
print(part2(lines)) #29895