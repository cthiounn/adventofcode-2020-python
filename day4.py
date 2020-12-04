# from collections import Counter
# from collections import deque
# import asyncio
# import itertools
# import json
# import math
import re
# import string
# import sys
# import unittest

#c=[ v for (k,v) in  Counter(line).items()  if k in 'aeiou']
# double_letter_with_something = re.compile(r'.*(..).*\1.*', re.IGNORECASE)
#     match2= double_letter_with_something.match(line)
#     if match and match2:
#         return 1
# num=lambda s : re.findall('\d+',s)

# #
# hgt:161cm iyr:1962
# pid:394421140
# ecl:gry
# cid:209 hcl:#efcc98 byr:2001
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
    if 1920<=int(b.groups()[0])<= 2002:
        return True
    return False
def checkiyr(s):
    a= re.compile(r'.*iyr:([a-zA-Z0-9]+)', re.IGNORECASE)
    b=a.match(s)
    if b and 2010<=int(b.groups()[0])<= 2020:
        return True
    return False
def checkeyr(s):
    a= re.compile(r'.*eyr:([a-zA-Z0-9]+)', re.IGNORECASE)
    b=a.match(s)
    if b and  2020<=int(b.groups()[0])<= 2030:
        return True
    return False
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
    if b and len(b.groups()[0])==9:
        return True
    return False
def checkecl(s):
    a= re.compile(r'.*ecl:([a-zA-Z0-9]+)', re.IGNORECASE)
    b=a.match(s)
    if b:
        if 'amb' in b.groups()[0] or 'blu' in b.groups()[0] or 'brn' in b.groups()[0] or 'gry'  in b.groups()[0] or'grn'  in b.groups()[0] or'hzl' in b.groups()[0] or 'oth' in b.groups()[0] :
            return True
    return False
def checkhcl(s):
    a= re.compile(r'.*hcl:(#[a-f0-9]+)', re.IGNORECASE)
    b=a.match(s)
    if b :
        return True
    return False
print(part1(lines)) #233
print(part2(lines)) #111