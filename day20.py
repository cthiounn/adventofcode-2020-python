import collections
import re
import copy
import functools

with open('data/my_input/20.in') as f:
    lines = [  line.strip() for line in f]

with open('data/test/20.test') as f2:
    tests = [  test.strip() for test in f2]

# ************************** list utils **************************
def removeborder(li):
    m=len(li)
    ll=li[1:m-1]
    ll=rotatelist(ll)
    m=len(ll)
    ll=ll[1:m-1]
    for _ in range(3):
        ll=rotatelist(ll)
    return ll


def verticalfusli(li1,li2):
    li=[]
    if not li1:
        return li2
    if not li2:
        return li1
    li.extend(li1)
    li.extend(li2)
    return li

def fusli(li1,li2):
    li=[]
    if not li1:
        return li2
    if not li2:
        return li1
    for i in range(len(li1)):
        li.append(li1[i]+li2[i])
    return li

def rotatelist(li1):
    k=len(li1[0])
    li2=[]
    for i in range(k):
        s=""
        for j in li1:
            s+=j[i]
        li2.append(s[::-1])
    return li2

def fliplist(li1):
    return [s[::-1] for s in li1]
 
def matchleft(li1,li2):
    s=""
    for i in li1:
        s+=i[0]
    m=""
    for j in li2:
        m+=j[-1]

    return s==m

def matchup(li1,li2):
    return li1[0]==li2[-1]

def matchanyborder(li1,li2):
    l=""
    r=""
    for j in li2:
        l+=j[0]
        r+=j[-1]
    u=li2[0]
    d=li2[-1]
    l1=""
    r1=""
    for j1 in li1:
        l1+=j1[0]
        r1+=j1[-1]
    u1=li1[0]
    d1=li1[-1]
    li2border=set([l,r,u,d,l[::-1],r[::-1],u[::-1],d[::-1]])
    li1border=set([l1,r1,u1,d1]) 
    return len(li1border.intersection(li2border))==1
 

def matchwithneighbor(d,i,j,puzzle):
    leftok=(i,j-1) not in d or  ((i,j-1) in d and not (matchleft(d[(i,j-1)],puzzle)))
    rightok=(i,j+1) not in d or((i,j+1) in d and not (matchleft(puzzle,d[(i,j+1)])))
    upok=(i-1,) not in d or((i-1,j) in d and not (matchup(d[(i-1,j)],puzzle)))
    downok=(i+1,j) not in d or((i+1,j) in d and not (matchup(puzzle,d[(i+1,j)])))
    return leftok and rightok and upok and downok

# ************************** main **************************

def part1and2(vlines):
    # step1 :parse
    num=lambda l: re.findall(r'\d+',l)
    init_dict_parsed=dict()
    li=[]
    first=True
    id_number=0
    for l in vlines:
        a= num(l)
        if a:
            if first:
                first=False
                id_number=a[0]
            else:
                init_dict_parsed[id_number]=li
                id_number=a[0]
                li=[]
        elif l:
            li.append(l)
    init_dict_parsed[id_number]=li

    # step 2 : count adjacent
    number_borders_dict=collections.defaultdict(int)
    for k1,v1 in init_dict_parsed.items():
        for k2,v2 in init_dict_parsed.items():
            if k1==k2:
                continue
            if matchanyborder(v1,v2):
                number_borders_dict[k2]+=1
    mul=lambda a,b:a*b
    listangle=[i for (i,j) in number_borders_dict.items() if j==2]
    print("part1 :" , functools.reduce(mul,map(int,listangle)))
    
    # step 3 :build global picture 
    final_picture_dict=dict()
    while listangle and len(final_picture_dict)!=len(init_dict_parsed):
        queue=set()
        pos=dict()
        final_picture_dict=dict()
        idpickoneangle=listangle.pop()
        queue.add(idpickoneangle)
        pos[idpickoneangle]=(0,0)
        final_picture_dict[(0,0)]=init_dict_parsed[idpickoneangle]
        placed=set([idpickoneangle])
        while queue:
            idwork=queue.pop()
            i,j = pos[idwork]
            liwork=final_picture_dict[(i,j)]
            for aa1,bb1 in init_dict_parsed.items():
                if idwork==aa1:
                    continue
                if aa1 in placed:
                    continue
                found=False
                cc1=fliplist(bb1)
                for _ in range(4):
                    di,dj=(0,0)
                    value=[]
                    if  matchup(bb1,liwork) and matchwithneighbor(final_picture_dict,i+1,j,bb1):
                        di=1
                        value=bb1
                        found=True
                    elif matchleft(bb1,liwork) and matchwithneighbor(final_picture_dict,i,j+1,bb1):
                        dj=1
                        value=bb1
                        found=True
                    elif  matchup(cc1,liwork) and matchwithneighbor(final_picture_dict,i+1,j,cc1):
                        di=1
                        value=cc1
                        found=True
                    elif matchleft(cc1,liwork) and matchwithneighbor(final_picture_dict,i,j+1,cc1):
                        dj=1
                        value=cc1
                        found=True
                    
                    if not found:
                        bb1=rotatelist(bb1)
                        cc1=rotatelist(cc1)
                    else:
                        final_picture_dict[(i+di,j+dj)]=value
                        pos[aa1]=(i+di,j+dj)
                        if aa1 not in placed:
                            queue.add(aa1)
                            placed.add(aa1)
                        break




    # step 4 : remove border
    final_picture_dict= { k:removeborder(v) for (k,v) in final_picture_dict.items()}

    # step 5 : merge all list into one
    myfinallist=[]
    xmin = min([x for x, y in final_picture_dict])
    ymin = min([y for x, y in final_picture_dict])
    xmax = max([x for x, y in final_picture_dict])
    ymax = max([y for x, y in final_picture_dict])
    for i in range(xmin , xmax + 1):
        mylist=[]
        for j in range(ymin , ymax + 1):
            mylist=fusli(mylist,final_picture_dict[(i,j)])
        myfinallist=verticalfusli(myfinallist,mylist)

    # step 6 : rotate-flip and find monsters
    numhash="".join(myfinallist).count('#')
    flipfinallist=fliplist(myfinallist)
    licounter=set()
    for _ in range(4):
        licounter.add(countmonster(myfinallist))
        licounter.add(countmonster(flipfinallist))
        myfinallist=rotatelist(myfinallist)
        flipfinallist=rotatelist(myfinallist)
    
    print("part2 :" , numhash-15*max(licounter))

def countmonster(myfinallist):
    monster=lambda s:re.search(r'#....##....##....###',s)
    bottommonster=lambda s:re.search(r'.#..#..#..#..#..#...',s)
    counter=0
    for i,string in enumerate(myfinallist):
        ss=string
        while(monster(ss)):
            startindexofmonster=monster(ss).start()
            if i+1 in range(len(myfinallist)) and i-1 in range(len(myfinallist)):
                lup=myfinallist[i-1][startindexofmonster:][18]
                ldown=myfinallist[i+1][startindexofmonster:startindexofmonster+21]
                if lup=='#' and bottommonster(ldown):
                    counter+=1
            ss="0"*(startindexofmonster+1) +ss[startindexofmonster+1:]
    return counter
 

part1and2(tests)
part1and2(lines) # 11788777383197 and 2242


