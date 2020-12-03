with open('data/my_input/3.in') as f:
    lines = [  line.strip() for line in f]

def part1(vlines):
    x,y=0,0
    count=0
    for line in vlines:
        if  line[x]=='#':
            count+=1
        x+=3
        x= x%len(line)
    return count

def slope(lines,i,j):
    count=0
    x,y=0,0
    while y<len(lines):
        if  lines[y][x]=='#':
            count+=1
        x+=i
        y+=j
        if y <len(lines):
            x= x%len(lines[y])
    return count

def part2(vlines):
    return slope(vlines,1,1)* slope(vlines,3,1)* slope(vlines,5,1)* slope(vlines,7,1)* slope(vlines,1,2)

print(part1(lines)) #164
print(part2(lines)) #5007658656