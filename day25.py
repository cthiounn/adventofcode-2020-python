

with open('data/my_input/25.in') as f:
    lines = [  int(line.strip()) for line in f]
 
with open('data/test/25.test') as f2:
    tests = [  int(test.strip()) for test in f2]

def findloopnum_or_calculate(cpk,subjectnumber,calculate):
    loopsize=1
    initvalue=1
    while True:
        if calculate:
            test =(initvalue* cpk)%20201227
        else:
            test =(initvalue* subjectnumber)%20201227
        if not calculate and cpk==test :
            return loopsize
        elif calculate and loopsize==subjectnumber:
            return test
        initvalue=test
        loopsize+=1
    
    
def part1(vlines):
    cpk,dpk= vlines
    a,b= findloopnum_or_calculate(cpk,7,False),findloopnum_or_calculate(dpk,7,False)
    return findloopnum_or_calculate(cpk,b,True)
 
print("test part1",part1(tests)) #14897079
print("output part1",part1(lines)) #12929