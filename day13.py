# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

with open('data/my_input/13.in') as f:
    lines = [  line.strip() for line in f]

with open('data/test/13.test') as f2:
    tests = [  test.strip() for test in f2]

def part1(vlines):
    fi,sec=vlines
    li=list()
    u=int(fi)
    for j in sec.split(','):
        if 'x' not in j:
            i=0
            while u >= i*int(j):
                i+=1
            if u <= i*int(j):
                li.append((i*int(j),int(j)* (i*int(j)-u)))
    return min(li)[1]

def part2(vlines):
    fi,sec=vlines
    li1=[]
    li2=[]
    for i,j in enumerate(sec.replace(',',' ').split(' ')):
        if 'x' not in j:
            li1.append(int(j))
            li2.append(int(j)-i)
    return chinese_remainder(li1,li2)

print("test part1",part1(tests))
print("output part1",part1(lines)) #2995
print("test part2",part2(tests))
print("output part2",part2(lines)) #1012171816131114