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
T = 100

pos = []

quad_counts = [0,0,0,0]

map = [[0 for _ in range(W)] for _ in range(H)]

for i, (p,v) in enumerate(robots):
    px = p[0] + v[0] * T
    py = p[1] + v[1] * T

    px = px % W
    py = py % H

    map[py][px] += 1

    if px < W//2 and py < H//2:
        quad_counts[0] += 1
    elif px > W//2 and py < H//2:
        quad_counts[1] += 1
    elif px < W//2 and py > H//2:
        quad_counts[2] += 1
    elif px > W//2 and py > H//2:
        quad_counts[3] += 1
    else:
        map[py][px] = 999

for y in range(H):
    print("".join([(("#" if map[y][x] == 999 else str(map[y][x]))if map[y][x] != 0 else ".") for x in range(W)]))

answer = 1
for q in quad_counts:
    answer *= q

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
