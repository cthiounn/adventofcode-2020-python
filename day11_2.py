with open('data/my_input/11.in') as f:
    lines = [  line.strip() for line in f]
    D = { (x,y): cell for x,row in enumerate(lines) for y,cell in enumerate(row) }

def part2count(di,i,j):
    l=[]
    for ii in range(-1,2):
        for jj in range(-1,2):
            if  ii==jj==0:
                continue
            io=1
            while (i+io*ii,j+io*jj) in di    :
                if  di[(i+io*ii,j+io*jj)] in 'L#':
                    l.append(di[(i+io*ii,j+io*jj)])
                    break
                io+=1
    return ''.join(l).count('#')

def transform(s,di,tol,part2,i,j):
    if part2:
        numhash=part2count(di,i,j)
    else:
        numhash=''.join([ di[(i+ii,j+jj)] for ii in range(-1,2) for jj in range(-1,2) if not (ii==jj==0) and (i+ii,j+jj) in di ]).count('#')
    if numhash==0 and 'L' in s :
        return '#'
    elif numhash >=tol and '#' in s :
        return 'L'
    return s


def calculate(di,k,tol,part2):
    s=di[k]
    if s in "#L":
        return transform(s,di,tol,part2,*k)
    return '.'

def run(di,tol,part2):
    return { i: calculate(di,i,tol,part2) for i in di.keys()}

def part1and2(di,tol,part2):
    while True:
        d2=run(di,tol,part2)
        if di==d2:
            print(''.join(di.values()).count('#'))
            break
        di,d2=d2,{} 
    

part1and2(D,4,False) #2113
part1and2(D,5,True) #1865
 