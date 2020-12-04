import re

with open('data/my_input/4.in') as f:
    lines = [  line.strip() for line in f]

def part1(vlines):
    passportcount=0
    pidp=False
    byrp=False
    iyrp=False
    eyrp=False
    hgtp=False
    eclp=False
    hclp=False
    for line in vlines:
        if "pid:" in line:
            pidp=True
        if "byr:" in line:
            byrp=True
        if "iyr:" in line:
            iyrp=True
        if "eyr:" in line:
            eyrp=True
        if "ecl:" in line:
            eclp=True
        if "hcl:" in line:
            hclp=True
        if "hgt:" in line:
            hgtp=True
        
        if len(line.strip())==0:
            if pidp and byrp and iyrp and eyrp and hgtp and eclp and hclp :
                passportcount+=1
            pidp=False
            byrp=False
            iyrp=False
            eyrp=False
            hgtp=False
            eclp=False
            hclp=False
    if pidp and byrp and iyrp and eyrp and hgtp and eclp and hclp :
                passportcount+=1
    return passportcount

def part2(vlines):
    passportcount=0
    pidp=False
    byrp=False
    iyrp=False
    eyrp=False
    hgtp=False
    eclp=False
    hclp=False
    for line in vlines:
        if "pid:" in line:
            pidp= checkpid(line)
        if "byr:" in line:
            byrp= checkbyr(line)
        if "iyr:" in line:
            iyrp= checkiyr(line)
        if "eyr:" in line:
            eyrp= checkeyr(line)
        if "ecl:" in line:
            eclp= checkecl(line)
        if "hcl:" in line:
            hclp= checkhcl(line)
        if "hgt:" in line:
            hgtp= checkhgt(line)
        
        if len(line.strip())==0:
            if pidp and byrp and iyrp and eyrp and hgtp and eclp and hclp :
                passportcount+=1
            pidp=False
            byrp=False
            iyrp=False
            eyrp=False
            hgtp=False
            eclp=False
            hclp=False
    if pidp and byrp and iyrp and eyrp and hgtp and eclp and hclp :
                passportcount+=1
    return passportcount


def checkbyr(s):
    a= re.compile(r'.*byr:([a-zA-Z0-9]+)', re.IGNORECASE)
    b=a.match(s) 
    return 1920<=int(b.groups()[0])<= 2002
def checkiyr(s):
    a= re.compile(r'.*iyr:([a-zA-Z0-9]+)', re.IGNORECASE)
    b=a.match(s)
    return  b and 2010<=int(b.groups()[0])<= 2020
def checkeyr(s):
    a= re.compile(r'.*eyr:([a-zA-Z0-9]+)', re.IGNORECASE)
    b=a.match(s)
    return b and  2020<=int(b.groups()[0])<= 2030
def checkhgt(s):
    a= re.compile(r'.*hgt:([a-zA-Z0-9]+)', re.IGNORECASE)
    b=a.match(s)
    if b :
        if 'cm' in b.groups()[0]:
            w=b.groups()[0].split('cm')[0]
            if  150<=int(w)<=193:
                return True
        elif 'in' in b.groups()[0]:
            w=b.groups()[0].split('in')[0]
            if  59<=int(w)<=76:
                return True
    return False
def checkpid(s):
    a= re.compile(r'.*pid:([0-9]+)', re.IGNORECASE)
    b=a.match(s) 
    return b and len(b.groups()[0])==9
fs=frozenset(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
def checkecl(s):
    a= re.compile(r'.*ecl:([a-zA-Z0-9]+)', re.IGNORECASE)
    b=a.match(s) 
    return b and b.groups()[0] in fs
def checkhcl(s):
    a= re.compile(r'.*hcl:(#[a-f0-9]+)', re.IGNORECASE) 
    return a.match(s) 
    
print(part1(lines)) #233
print(part2(lines)) #111