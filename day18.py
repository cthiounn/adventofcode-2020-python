
with open('data/my_input/18.in') as f:
    lines = [  line.strip() for line in f]
    
with open('data/test/18.test') as f2:
    tests = [  test.strip() for test in f2]

def evaluate(s):
    num=0
    num2=0
    first=False
    second=False
    operator=""
    for l in s.split():
        if l.isnumeric():
            if not first:
                num=int(l)
                first=True
            else:
                num2=int(l)
                second=True
            if second:
                if "+" in operator:
                    num= num+num2
                elif "*" in operator:
                    num= num*num2
        elif "*" in l:
            operator=l
        elif "+" in l:
            operator=l
        
        
    return str(num)

def parse(s):
    if "(" in s:
        i=s.rindex("(")
        j=s.find(")",i)
        stringevaluate=s[:i] + evaluate(s[i+1:j]) + s[j+1:]
        return int(parse(stringevaluate))
    return int(evaluate(s))

def parse2(s):
    if "(" in s:
        i=s.rindex("(")
        j=s.find(")",i)
        stringevaluate=s[:i] + evaluate2(s[i+1:j]) + s[j+1:]
        return int(parse2(stringevaluate))
    return int(evaluate2(s))

def evaluate2(s):
    if "+" in s:
        li=s.split()
        num=0
        num2=0
        first=False
        second=False
        found=False
        firstoperation=True
        operator=""
        li2=[]
        for ind,l in enumerate(li):
            if l.isnumeric():
                if not first:
                    num=int(l)
                    first=True
                else:
                    if not firstoperation:
                        num=num2
                    firstoperation=False
                    num2=int(l)
                    second=True
                if second:
                    if "+" in operator:
                        num= num+num2
                        li2.pop()
                        li2.pop()
                        li2.append(str(num))
                        li2.extend(li[ind+1:])
                        to_evaluate=" ".join(li2)
                        return evaluate2(to_evaluate)
                        
            elif "+" in l:
                found=True
                operator="+"
            li2.append(l)
    else:
        return evaluate(s)

def part1(vlines):
    return sum(map(parse,vlines))

def part2(vlines):
    return sum(map(parse2,vlines))

print("test part1",part1(tests))
print("output part1",part1(lines)) #131076645626
print("test part2",part2(tests))
print("output part2",part2(lines)) #109418509151782