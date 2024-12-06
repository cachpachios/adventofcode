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

from multiprocessing import Pool

from functools import cache, lru_cache

INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"

file = read(INPUT_FILE)
answer = 0

obst = []
start = None

for y, line in enumerate(file):
    for x, c in enumerate(line):
        if c == "#":
            obst.append((x, y))
        if c == "^":
            start = (x, y)


dirs = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}


def run(obst):
    def find_obs(x, y, dx, dy):
        while (x, y) not in obst:
            if x < 0 or y < 0 or x >= len(file[0]) or y >= len(file):
                raise StopIteration("Out of bounds")
            x += dx
            y += dy
        return (x - dx, y - dy)

    direction = 0
    try:
        pos = find_obs(*start, *dirs[direction])
    except StopIteration:
        return True
    visited = set()
    while (*pos, direction) not in visited:
        visited.add((*pos, direction))
        direction = (direction + 1) % 4
        try:
            pos = find_obs(*pos, *dirs[direction])
        except StopIteration:
            return True
    print(visited)
    return False


pbar = tqdm(total=len(file) * len(file[0]))
with Pool(64) as p:
    for y in range(len(file)):
        obsts = []
        for x in range(len(file[0])):
            if (x, y) in obst or (x, y) == start:
                continue
            obsts.append(obst + [(x, y)])

        r = list(p.imap_unordered(run, obsts))
        answer += sum(not x for x in r)
        pbar.update(len(file[0]))

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
