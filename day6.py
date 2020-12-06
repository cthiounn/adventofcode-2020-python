with open('data/my_input/6.in') as f:
    lines = [  line.strip() for line in f]

def part1(vlines):
    d=set()
    counter=0
    for line in vlines:
        if len(line.strip())==0:
            counter+=len(list(d))
            d=set()
        else:
            for i in line:
                d.add(i)
    counter+=len(list(d))   
        

    return counter

def part2(vlines):
    counter=0
    s=set("azertyuiopqsdfghjklmwxcvbn")
    for line in vlines:
        if len(line.strip())==0:
            counter+=len(s)
            s=set("azertyuiopqsdfghjklmwxcvbn")
        else: 
            s=s&set(line)
    
    counter+=len(s)
    return counter

print(part1(lines))
print(part2(lines))