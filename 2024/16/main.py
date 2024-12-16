from copy import deepcopy
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

map = [list(x) for x in inpt]

ROT = {
    "E": (1,0),
    "N": (0,1),
    "W": (-1,0),
    "S": (0,-1)
}
ROTs = list(ROT.keys())

start = None
end = None
for y,l in enumerate(map):
    for x,c in enumerate(l):
        if c == "S":
            start = (x,y)
        if c == "E":
            end = (x,y)


frontier = deque([(start, 0, [start], "E")])
visited = {}

points = []
scores = []

while frontier:
    pos, score, steps, r = frontier.popleft()
    # print(pos, r, frontier)
    if (pos,r) in visited and visited[(pos,r)] < score:
        continue
    if score > min(scores, default=9999999):
        continue
    visited[(pos,r)] = score

    if pos == end:
        points.append(steps)
        scores.append(score)
        continue
    
    x,y = pos
    dx,dy = ROT[r]
    nx,ny = x+dx, y+dy
    nricw = (ROTs.index(r) + 1) % 4
    nriccw = (ROTs.index(r) - 1) % 4
    nrcw = ROTs[nricw]
    nrccw = ROTs[nriccw]

    if map[ny][nx] != "#":    
        frontier.append(((nx,ny), score + 1, steps + [(nx,ny)], r))
    frontier.append(((x,y), score + 1000, steps, nrccw))
    frontier.append(((x,y), score + 1000, steps, nrcw))

ms = min(scores)

min_pts = set()

for s, pts in zip(scores, points):
    if s == ms:
        print(s, scores)
        min_pts.update(pts)

for p in min_pts:
    x,y = p
    map[y][x] = "O"

for l in map:
    print("".join(l))

answer = len(min_pts)


print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
