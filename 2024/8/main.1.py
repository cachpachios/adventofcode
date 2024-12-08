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
from itertools import combinations, permutations, combinations_with_replacement,product
from dataclasses import dataclass

from multiprocessing import Pool

from functools import cache, lru_cache

INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"

file = read(INPUT_FILE)
W = len(file[0])
H = len(file)
answer = 0

nodes = {}

for y, l in enumerate(file):
    for x, c in enumerate(l):
        if c == ".":
            continue
        nodes[c] = nodes.get(c, [])
        nodes[c].append((x, y))

anodes = []

for k, v in nodes.items():
    for a, b in combinations(v, 2):
        a = np.array(a)
        b = np.array(b)

        aa = a + (a - b)
        bb = b + (b - a)

        if aa[0] >= 0 and aa[0] < W and aa[1] >= 0 and aa[1] < H:
            anodes.append(aa)
            
        if bb[0] >= 0 and bb[0] < W and bb[1] >= 0 and bb[1] < H:
            anodes.append(bb)

answer = len(set(map(tuple, anodes)))


print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
