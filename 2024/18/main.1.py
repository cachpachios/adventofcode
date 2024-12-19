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

poss = [tuple(int(x) for x in l.split(",")) for l in file]

start = (0,0)
W = 70
H = 70
goal = (W,H)

corrupted = poss[:1024]

frontier = deque([(start,0)])
visited = set()

paths = []

while frontier:
    pos, steps = frontier.popleft()
    if pos == goal:
        paths.append(steps)
        continue
    if pos in visited:
        continue

    if pos in corrupted:
        continue

    visited.add(pos)
    x,y = pos
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        new_x = x + dx
        new_y = y + dy
        if 0 <= new_x <= W and 0 <= new_y <= H:
            if (new_x,new_y) not in visited:
                frontier.append(((new_x,new_y), steps+1))

answer = min(paths)
print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
