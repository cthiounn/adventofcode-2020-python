with open('data/my_input/11.in') as f:
    lines = [  line.strip() for line in f]

def part1and2(vlines,part2,tol):
    stop = False
    li1,li2=vlines,[]
    while not stop:
        for i,u  in enumerate(li1):
            s=""
            for j,v in enumerate(u) :
                if v in '#L':
                    s+=transform(i,j,v,li1,part2,tol)
                else :
                    s+=v
            li2.append(s)
        if li1==li2:
            return  ("".join(li1)).count('#')
        li1,li2=li2,[]

def findfirst(a,b,i,j,li,part2):
    k,l=a+i,b+j
    m,n=len(li),len(li[0])
    if k not in range(m) or l not in range(n):
        return '.'
    else:
        mytile=li[k][l]
        if mytile=='.':
            if part2:
                return findfirst(k,l,i,j,li,part2)
            else:
                return mytile
        else:
            return mytile

def count2(a,b,c,li,part2):
    l=list()
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if not i==j==0:
                l.append(findfirst(a,b,i,j,li,part2))
    return ''.join(l).count('#')

def transform(a,b,c,li,part2,tol):
    if c=='#' and count2(a,b,c,li,part2)>=tol:
        return 'L'
    elif c=='L' and count2(a,b,c,li,part2)==0:
        return '#' 
    return c
 
print(part1and2(lines,False,4)) #2113
print(part1and2(lines,True,5)) #1865