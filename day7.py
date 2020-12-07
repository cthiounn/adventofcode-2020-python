import re

# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
with open('data/my_input/7.in') as f:
    lines = [  line.strip() for line in f]


m= lambda s: re.findall(r'\d+',s)
z= lambda s: re.findall(r'\d+ ([a-z ]+) bag[s]*[.]*',s)
def parseline(line,d):
    li=line.split('contain')
    i=li.pop(0)
    d[i]=li
def count(it,d):
    return [(k,v) for k,v in d.items() if it in ''.join(v)]

def part1(vlines):
    d=dict()
    for line in vlines:
        parseline(line,d)
    queue=[]
    visited=[]
    queue.append("shiny gold bag")
    counter=0
    while queue:
        it=queue.pop()
        if it not in visited:
            counter+=1
            visited.append(it)
            for j in count(it,d):
                queue.append(j[0].strip()[:-1])
    return counter-1

def numbbad(it,d):
    if it not in d :
        return 1
    elif  (it in d and 'no other' not in ''.join(d[it])):
        k=d[it]
        for j in k:
            if "," in j:
                j.split(",")
            numb=m(j)
            bags=z(j)
        
        counter=0

        for i in range(len(bags)):
            st= bags[i] + ' bags '
            counter+= int(numb[i]) * numbbad(st,d) +int(numb[i])
        return counter
    return 0

def part2(vlines):
    d=dict()
    for line in vlines:
        parseline(line,d)
    return numbbad("shiny gold bags ",d)

print(part1(lines)) #337
print(part2(lines)) #50100