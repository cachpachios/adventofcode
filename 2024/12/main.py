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

chrs = set("".join(inpt))
areas = {}
visited = set()

for y in range(len(inpt)):
    for x in range(len(inpt[0])):
        if (x, y) in visited:
            continue
        c = inpt[y][x]
        frontier = [(x, y)]
        region = []
        prmtr = 0
        sides_y = {}
        sides_x = {}
        while frontier:
            x_, y_ = frontier.pop()
            if (x_, y_) in region:
                continue
            region.append((x_, y_))
            for (dx, dy) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                xd, yd = x_ + dx, y_ + dy
                if xd < 0 or yd < 0 or xd >= len(inpt[0]) or yd >= len(inpt):
                    prmtr += 1
                    if dx != 0:
                        sides_x[(xd, dx)] = sides_x.get((xd, dx),set()) | {yd}
                    if dy != 0:
                        sides_y[(yd, dy)] = sides_y.get((yd, dy),set()) | {xd}
                    continue
                if inpt[yd][xd] != c:
                    prmtr += 1
                    if dx != 0:
                        sides_x[(xd, dx)] = sides_x.get((xd, dx),set()) | {yd}
                    if dy != 0:
                        sides_y[(yd, dy)] = sides_y.get((yd, dy),set()) | {xd}
                    continue
                frontier.append((xd, yd))
        visited |= set(region)
        sides_total = 0
        for ss in [sides_x,sides_y]:
            for v in ss.values():
                v = sorted(list(v))
                sides_total += 1
                for i in range(1,len(v)):
                    if v[i] - v[i-1] != 1:
                        sides_total += 1

        print(c, sides_total, sides_x, sides_y)
        areas[c] = areas.get(c,[]) + [(len(region),sides_total , len(region)*sides_total)]
        answer += len(region) * sides_total
for k in areas:
    print(k, areas[k])
print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
