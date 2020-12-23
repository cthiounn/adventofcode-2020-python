
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
    return ss[ii+1:]+ss[0:ii]

class N:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def part2(nums,rou):
    sNode=dict()
    prev=None
    for j in str(nums):
        p=N(int(j))
        sNode[int(j)]=p
        if prev:
            prev.next=p
        prev=p
    a=len(str(nums))

    for m in range(a+1,1000000+1):
        p=N(int(m))
        sNode[int(m)]=p
        if prev:
            prev.next=p
        prev=p
        
    for j in str(nums):
        first=sNode[int(j)]
        if prev:
            prev.next=first
        break
    
    for i in range(rou):
        second=first.next
        third=second.next
        q4=third.next
        first.next=q4.next
        ind=first.val
        forbidden=(first.val,second.val,third.val,q4.val)
        while ind  in forbidden:
            ind -= 1
            if ind == 0:
                ind = 1000000
        node_to_modified= sNode[ind]
        node_to_modified2=node_to_modified.next
        node_to_modified.next=second
        q4.next=node_to_modified2
        first=first.next
    s1=sNode[1].next
    s2=s1.next
    return s1.val*s2.val

print("test part1",part1(tests,10))
print("test part1",part1(tests,100))
print("output part1",part1(lines,100)) #39564287
print("test part2",part2(tests,10000000)) 
print("output part2",part2(lines,10000000)) #404431096944