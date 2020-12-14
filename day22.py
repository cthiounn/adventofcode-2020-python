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

with open('data/my_input/22.in') as f:
    lines = [  line.strip() for line in f]
    # dlines = { (x,y): cell for x,row in enumerate(lines) for y,cell in enumerate(row) }

with open('data/test/22.test') as f2:
    tests = [  test.strip() for test in f2]

def part1(vlines):
    return 0

def part2(vlines):
    return 0

print("test part1",part1(tests))
print("output part1",part1(lines))
print("test part2",part2(tests))
print("output part2",part2(lines))