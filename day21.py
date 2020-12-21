with open('data/my_input/21.in') as f:
    lines = [  line.strip() for line in f]

with open('data/test/21.test') as f2:
    tests = [  test.strip() for test in f2]
  
def part1and2(vlines):
    d=dict()
    li=list()
    sse=set()
    queue=set()
    ailments=set()
    allergens=set()
    possible=dict()
    for ind,l in enumerate(vlines):
        ingredient, allergen= l.replace(",","").replace("(","").replace(")","").split("contains")
        for i in ingredient.split():
            ailments.add(i)
        for j in allergen.split():
            allergens.add(j)
        d[ind]=(set(ingredient.split()),set(allergen.split()))
    for allergen in allergens: 
        l=set()
        for it in d.values():

            k,v = it
            if allergen in v :
                if not l:
                    l=k
                else:
                    l=l.intersection(k)
        
        possible[allergen]=l
    
    forbidden=set()
    equiv=dict()
    while len(forbidden)!=len(possible):
        for k,v in possible.items():
            myl= [i for i in v if i not in forbidden]
            if len(myl)==1:
                food=myl[0]
                forbidden.add(food)
                equiv[k]=food
    exclusion = [ i for i in ailments if i not in forbidden]
    counter=0
    for j in exclusion:
        counter += sum([ 1 for l in vlines if j in l.split()])
    print( "part1",counter)
    mylist=sorted([(k,v) for k,v in equiv.items()],key= lambda s: s[0])
    
    
    print("part2" ,",".join(list(map(lambda s:s[1],mylist))))
 
part1and2(tests)
part1and2(lines)
# 2324
# bxjvzk,hqgqj,sp,spl,hsksz,qzzzf,fmpgn,tpnnkc