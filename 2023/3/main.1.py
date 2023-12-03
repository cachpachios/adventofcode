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

answer = 0
file = read(INPUT_FILE)

@dataclass
class Num:
    y: int
    x0: int
    x1: int
    val: int


numbers = []
for j,line in enumerate(file):
    start = -1
    for i,c in enumerate(line):
        if c in string.digits:
            if start == -1:
                start = i
        elif start != -1:
                numbers.append(Num(j, start, i, int(line[start:i])))
                start = -1
    if start != -1:
        numbers.append(Num(j, start, len(line), int(line[start:])))

C_VAL = None
valSet = set()

def isSymbol(x, y):
    if x < 0 or y < 0 or y >= len(file) or x >= len(file[y]):
        return False
    val = file[y][x]
    ret = val != "."
    if ret:
        valSet.add(val)
    return ret

part_numbers = []

for n in numbers:
    symbol = False
    C_VAL = n.val
    symbol = isSymbol(n.x0-1, n.y) or symbol
    symbol = isSymbol(n.x1, n.y) or symbol
    for i in range(n.x0-1, n.x1+1):
        symbol = isSymbol(i, n.y-1) or symbol
        symbol = isSymbol(i, n.y+1) or symbol

    if symbol:
        part_numbers.append(n.val)

    # else:
        # print(n.val)

answer = sum((part_numbers))

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
