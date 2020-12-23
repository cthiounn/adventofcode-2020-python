
with open('data/my_input/23.in') as f:
    lines = int(f.read())
with open('data/test/23.test') as f2:
    tests = int(f2.read())

def part1(i,round):
    ss=str(i)
    l=len(ss)
    for _ in range(round):
        v=int(ss[0])
        ref=v
        nextv=ss[1:4]
        remain=ss[4:]
        while str(ref) not in remain:
            ref-=1 
            ref%=l
            if ref==0:
                ref=l
        ii = remain.index(str(ref))
        ss=remain[0:ii+1] + nextv + remain[ii+1:] + str(v)
    ii = ss.index("1")
    print(ss[ii+1:]+ss[0:ii])
    return 0

def part2(vlines):
    return 0

print("test part1",part1(tests,10))
print("output part1",part1(lines,100))
# print("test part2",part2(tests))
# print("output part2",part2(lines))