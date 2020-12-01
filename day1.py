# from collections import Counter
# from collections import deque
# import asyncio
# import itertools
# import json
# import math
# import re
# import string
# import sys
# import unittest

with open('data/my_input/1.in') as f:
    lines = [  line.strip() for line in f]

def part1(vlines):
    for line in vlines:
        for line2 in vlines:
            if line!=line2 and int(line)+int(line2)==2020:
                return int(line)*int(line2)
    return 0

def part2(vlines):
    
    for line in vlines:
        for line2 in vlines:
            for line3 in vlines:
                if line!=line2 and line!=line3 and line2!=line3 and  int(line3)+int(line)+int(line2)==2020:
                    return int(line3)*int(line)*int(line2)
    return 0

print(part1(lines))
print(part2(lines))