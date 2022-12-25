from multiprocessing import Pool
from typing import Dict
from utils import *
from enum import Enum
import sys
import string
from tqdm import tqdm
import math
import numpy as np
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, combinations_with_replacement
from dataclasses import dataclass

from functools import cache, lru_cache

INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"

file = read(INPUT_FILE)

numbers = []

for line in file:
    num = []
    for c in line:
        if c.isnumeric():
            num.append(int(c))
        elif c == "-":
            num.append(-1)
        elif c == "=":
            num.append(-2)
    numbers.append(sum([num[i]*(5**(len(num)-i-1)) for i in range(len(num))]))

print(numbers)

n = sum(numbers)

dig = []

while n:
    dig.append(int(n % 5))
    n //= 5

dig = dig[::-1]
print(dig)
while any(d > 2 for d in dig):
    for i,d in enumerate(dig[1:]):
        if d == 3:
            dig[i+1] = -2
            dig[i] += 1
        elif d == 4:
            dig[i+1] = -1
            dig[i] += 1
        elif d == 5:
            dig[i] += 1
            
    if dig[0] == 3:
        dig[0] = -2
        dig.insert(0,1)
    elif dig[0] == 4:
        dig[0] = -1
        dig.insert(0,1)
    elif dig[0] == 5:
        dig.insert(0,1)

print(dig)

answer = ""

for d in dig:
    if d >= 0:
        answer += str(d)
    elif d == -1:
        answer += "-"
    elif d == -2:
        answer += "="

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
exit()
