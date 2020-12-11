with open('data/my_input/11.in') as f:
    lines = [  line.strip() for line in f]

def count(a,b,c,li):
    up,down,left,right='.','.','.','.'
    upl,upr,downl,downr='.','.','.','.'
    iup=a-1
    if iup<0:
        iup='.'
    ileft=b-1
    if ileft <0:
        ileft='.'
    idown=a+1
    if idown >= len(li):
        idown='.'

    iright=b+1
    if iright >= len(li[0]):
        iright='.'

    try:
        try:
            up=li[iup][b]
        except:
            up='.'
        try:
            down=li[idown][b]
        except:
            down='.'
        try:
            left=li[a][ileft]
        except:
            left='.'
        try:
            right=li[a][iright]
        except:
            right='.'
        try:
            upl=li[iup][ileft]
        except:
            upl='.'
        try:
            upr=li[iup][iright]
        except:
            upr='.'
        try:
            downl=li[idown][ileft]
        except:
            downl='.'
        try:
            downr=li[idown][iright]
        except:
            downr='.'
        
        
        
    except:
        z=0
    l=list()
    l.append(up)
    l.append(down)
    l.append(left)
    l.append(right)
    l.append(upl)
    l.append(upr)
    l.append(downl)
    l.append(downr)
    if c=='L' and '#' not in l:
        return 0
    elif c=='#' :
        return len([i for i in l if i=='#'])
    return -1
def transform(a,b,c,li):

    if c=='#' and count(a,b,c,li)>=4:
        return 'L'
    elif c=='L' and count(a,b,c,li)==0:
        return '#' 
    return c

def part1(vlines):
    i=0
    d=dict()
    d2=dict()
    stop = False
    counter=0
    li1=vlines
    li2=[]
    while not stop:
        i=0
        
        for i  in range(len(li1)):
            u=li1[i]
            s=""
            for j in range(len(u)) :
                if u[j]=='#' or u[j]=='L':
                    d2[(i,j)]=transform(i,j,u[j],li1)
                else :
                    d2[(i,j)]=u[j]
                
                s+=d2[(i,j)]
            li2.append(s)
        if d2==d:
            stop= True
        
        d.clear()
        for e in d2:
            d[e]=d2[e]
        d2.clear()
        counter+=1
        li1=li2.copy()
        li2=[]
    return  len([(k,v) for k,v in d.items() if v=='#'])

def findfirst(a,b,i,j,li):
    k=a+i
    l=b+j
    if k<0 or k >= len(li):
        k='.'
    if l<0 or l >= len(li[0]):
        l='.'
    if k=='.' or l=='.':
        return '.'
    else:
        mytile=li[k][l]
        if mytile=='.':
            return findfirst(k,l,i,j,li)
        else:
            return mytile
def count2(a,b,c,li):

    up=findfirst(a,b,-1,0,li)
    down=findfirst(a,b,1,0,li)
    left=findfirst(a,b,0,-1,li)
    right=findfirst(a,b,0,+1,li)
    upl=findfirst(a,b,-1,-1,li)
    upr=findfirst(a,b,-1,1,li)
    downl=findfirst(a,b,1,-1,li)
    downr=findfirst(a,b,1,1,li)

    l=list()
    l.append(up)
    l.append(down)
    l.append(left)
    l.append(right)
    l.append(upl)
    l.append(upr)
    l.append(downl)
    l.append(downr)
    if c=='L' and '#' not in l:
        return 0
    elif c=='#' :
        return len([i for i in l if i=='#'])
    return -1

def transform2(a,b,c,li):

    if c=='#' and count2(a,b,c,li)>=5:
        return 'L'
    elif c=='L' and count2(a,b,c,li)==0:
        return '#' 
    return c

def part2(vlines):
    i=0
    d=dict()
    d2=dict()
    stop = False
    counter=0
    li1=vlines
    li2=[]
    while not stop:
        i=0
        
        for i  in range(len(li1)):
            u=li1[i]
            s=""
            for j in range(len(u)) :
                if u[j]=='#' or u[j]=='L':
                    d2[(i,j)]=transform2(i,j,u[j],li1)
                else :
                    d2[(i,j)]=u[j]
                
                s+=d2[(i,j)]
            li2.append(s)
        if d2==d:
            stop= True
        
        d.clear()
        for e in d2:
            d[e]=d2[e]
        d2.clear()
        counter+=1
        li1=li2.copy()
        li2=[]
    return  len([(k,v) for k,v in d.items() if v=='#'])

print(part1(lines))
print(part2(lines))