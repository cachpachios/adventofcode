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

inpt = read(INPUT_FILE)
answer = 0

robots = []

for l in inpt:
    p,v = [([int(x) for x in s.split("=")[1].split(",")]) for s in l.split()]
    robots.append((p,v))

W = 101
H = 103

pos = []

# assume we need to find where y=0, x=W//2 has a single robot
Ts = []
for i, (p,v) in enumerate(robots):
    ty0 = (0 - p[1]) / v[1]
    ty1 = (H - p[1]) / v[1]
    if ty0 < 0 and ty1 < 0:
        continue
    print(ty0, ty1)

for j in range(1000000):
    map = [[0 for _ in range(W)] for _ in range(H)]
    for i, (p,v) in enumerate(robots):
        p[0] += v[0]
        p[1] += v[1]

        p[0] %= W
        p[1] %= H
        px = p[0]
        py = p[1]
        map[py][px] += 1

    if (np.array(map) <= 1).all():
        for y in range(H):
            print("".join([(str(map[y][x])if map[y][x] != 0 else ".") for x in range(W)]))
        answer = j+1
        break

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
