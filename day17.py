with open('data/my_input/17.in') as f:
    lines = [  line.strip() for line in f]
    dlines = { (x,y,0): cell for x,row in enumerate(lines) for y,cell in enumerate(row) }

with open('data/test/17.test') as f2:
    tests = [  test.strip() for test in f2]
    dlines2 = { (x,y,0): cell for x,row in enumerate(tests) for y,cell in enumerate(row) }
 
def part1(vlines):
    #init parse
    lihash=set()
    for i,l in enumerate(vlines):
        for j,k in enumerate(l):
            if '#' in k:
                lihash.add((i,j,0))
    x=lambda s: s[0]
    y=lambda s: s[1]
    z=lambda s: s[2]
    
    for _ in range(6):
        newlihash=set()
        for zz in range(min(map(z,lihash))-1,max(map(z,lihash))+2):
            for xx in range(min(map(x,lihash))-1,max(map(x,lihash))+2):
                for yy in range(min(map(y,lihash))-1,max(map(y,lihash))+2):
                    cc=0
                    for dz in [-1,0,1]:
                        for dx in [-1,0,1]:
                            for dy in [-1,0,1]:
                                if (dz,dx,dy)==(0,0,0):
                                    continue
                                
                                if (xx+dx,yy+dy,zz+dz) in lihash:
                                    cc+=1
                    if (cc==3 or cc==2) and (xx,yy,zz) in lihash:
                        newlihash.add((xx,yy,zz))
                    elif cc==3 and (xx,yy,zz) not in lihash:
                        newlihash.add((xx,yy,zz))
        lihash=newlihash
    return len(lihash)

def part2(vlines):
    #init parse
    lihash=set()
    for i,l in enumerate(vlines):
        for j,k in enumerate(l):
            if '#' in k:
                lihash.add((i,j,0,0))
    x=lambda s: s[0]
    y=lambda s: s[1]
    z=lambda s: s[2]
    dd=lambda s: s[3]
    
    for _ in range(6):
        newlihash=set()
        for ddd in range(min(map(dd,lihash))-1,max(map(dd,lihash))+2):
            for zz in range(min(map(z,lihash))-1,max(map(z,lihash))+2):
                for xx in range(min(map(x,lihash))-1,max(map(x,lihash))+2):
                    for yy in range(min(map(y,lihash))-1,max(map(y,lihash))+2):
                        cc=0
                        for dz in [-1,0,1]:
                            for dx in [-1,0,1]:
                                for dy in [-1,0,1]:
                                    for dddd in [-1,0,1]:
                                        if (dz,dx,dy,dddd)==(0,0,0,0):
                                            continue
                                        
                                        if (xx+dx,yy+dy,zz+dz,ddd+dddd) in lihash:
                                            cc+=1
                        if (cc==3 or cc==2) and (xx,yy,zz,ddd) in lihash:
                            newlihash.add((xx,yy,zz,ddd))
                        elif cc==3 and (xx,yy,zz,ddd) not in lihash:
                            newlihash.add((xx,yy,zz,ddd))
        lihash=newlihash
    return len(lihash)

print("test part1",part1(tests))
print("output part1",part1(lines)) #306
print("test part2",part2(tests))
print("output part2",part2(lines)) #2572