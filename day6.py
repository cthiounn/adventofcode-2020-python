import functools

with open('data/my_input/6.in') as f:
    lines = f.read().split('\n\n')

def part1(vlines):
    return sum(map(len,[set(l.replace('\n','')) for l in vlines]) )

def part2(vlines):
    lll=[l.strip().split('\n') for l in vlines]
    a= lambda c,d : c&d
    return sum([ len(i) for i in [functools.reduce(a,list(map(set,j))) for j in lll]])

print(part1(lines))
print(part2(lines))