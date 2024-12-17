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
from itertools import combinations, permutations, combinations_with_replacement, product
from dataclasses import dataclass

from multiprocessing import Pool

from functools import cache, lru_cache

INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"

file = read(INPUT_FILE)
answer = 0

rrregs, rprgm = parse_blocks(file)


prog = []
regs = {}

for r in rrregs:
    t, v = r.split(": ")
    regs[t[-1]] = int(v)

rprgm = rprgm[0].split(": ")[-1].split(",")
for r in rprgm:
    prog.append(int(r))


def cmb(v, regs):
    if v in range(0, 4):
        # print(v)
        return v
    if v == 4:
        # print("A")
        return regs["A"]
    if v == 5:
        # print("B")
        return regs["B"]
    if v == 6:
        # print("C")
        return regs["C"]
    raise ValueError("Invalid value " + str(v))


output = []

# B = (A % 8) ^ (A >> ((A % 8) ^ 3)) ^ 6
# A = A >> 3
# out B % 8

B = lambda A: (A % 8) ^ (A >> ((A % 8) ^ 3)) ^ 6

res = [0]
for p in reversed(prog):
    res_ = []
    for a in res:
        for i in range(8):
            test = (a << 3) + i
            print(test, B(test), B(test) % 8, p, res)
            if B(test) % 8 == p:
                res_.append(test)
    res = res_
print(res)
answer = min(res)


print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
