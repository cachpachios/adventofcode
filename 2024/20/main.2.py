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

map = [list(s) for s in file]

start = None

for y, row in enumerate(map):
    for x, c in enumerate(row):
        if c == "S":
            start = (x, y)
        if c == "E":
            goal = (x, y)


frontier = deque([(start, 0, [start])])
visited = set()
paths = []

#Find all paths
while frontier:
    pos, t, path = frontier.popleft()
    x,y = pos
    if (x, y) in visited:
        continue
    visited.add((x, y))
    if (x, y) == goal:
        paths.append((t, path))
        continue
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= x + dx < len(map[0]) and 0 <= y + dy < len(map):
            if map[ny][nx] != "#":
                frontier.append(((nx,ny), t + 1, (path + [(x + dx, y + dy)])))


min_path = min(paths, key=lambda x: x[0])
path_t = min_path[0]
path = min_path[1]

saved_by_cheating = []

for t_start, (x, y) in tqdm(enumerate(path), total=len(path)):
    reachable_within_t = set()
    frontier = deque([(0, (x, y))])
    visited = set()
    while frontier:
        t, pos = frontier.popleft()
        if t > 20:
            continue
        if pos in visited:
            continue
        visited.add(pos)
        if t > 0 and pos in path:
            reachable_within_t.add((pos, t))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = pos[0] + dx, pos[1] + dy
            # if t == 0 and map[ny][nx] != "#":
            #     continue
            if 0 <= nx < len(map[0]) and 0 <= ny < len(map):
                frontier.append((t + 1, (nx, ny)))
    for r, rt in reachable_within_t:
        t_end = path.index(r)
        if t_end - t_start - rt > 0:
            saved_by_cheating.append(t_end - t_start - rt)
        
print([x for x in sorted(Counter(saved_by_cheating).most_common(), key=lambda x: x[0]) if x[0] >= 50])
answer = sum(1 for s in saved_by_cheating if s >= 100)

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
