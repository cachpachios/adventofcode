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
answer = 0

S = "XMAS"
SS = [S,"SAMX"]
print(SS)

def get(x, y, dx, dy):
    s = ""
    for i in range(len(S)):
        x_ = x+i*dx
        y_ = y+i*dy
        if x_ < 0 or y_ < 0 or x_ >= len(file[0]) or y_ >= len(file):
            return None
        s += file[y_][x_]
    return s

dots =[["." for x in range(len(file[0]))] for y in range(len(file))]

def set(x, y, dx, dy, s):

    for i in range(len(S)):
        x_ = x+i*dx
        y_ = y+i*dy
        dots[y_][x_] = s[i]

xys = []
for y in range(len(file)):
    for x in range(len(file[0])):
        for dx,dy in [(1,0), (0,1), (1,1), (1,-1)]:
            s = get(x,y,dx,dy)
            if s in SS:
                answer += 1
                set(x,y,dx,dy, SS[SS.index(s)])


for line in dots:
    print("".join(c for c in line))

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
