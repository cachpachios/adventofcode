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
W = len(file[0])
H = len(file)
answer = 0

map = [[9999 if x == "." else int(x) for x in l] for l in file]

origins = []

for y in range(H):
    for x in range(W):
        if map[y][x] == 0:
            origins.append((x, y))


def find_path(x, y):
    q = deque([(x, y, 0)])
    visited = set()
    num_9s = 0

    while q:
        x, y, steps = q.popleft()
        if (x, y) in visited:
            continue
        val = map[y][x]
        if val == 9:
            num_9s += 1

        visited.add((x, y))

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= W or ny >= H:
                continue
            if map[ny][nx] - val != 1:
                continue
            # if abs(map[ny][nx] - val) > 1:
            #     continue
            if (nx, ny) not in visited:
                q.append((nx, ny, steps + 1))

    return num_9s


for i, (x, y) in enumerate(origins):
    answer += find_path(x, y)

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
