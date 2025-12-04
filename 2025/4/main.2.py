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

map = read(INPUT_FILE)
map = [list(row) for row in map]

accessible = set()
removed = True
while removed:
    removed = False
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] != "@":
                continue

            adj = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if abs(dx) + abs(dy) == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or ny >= len(map) or nx >= len(map[0]):
                        continue
                    if map[ny][nx] == "@":
                        adj += 1
            if adj < 4:
                removed = True
                map[y][x] = "."
                accessible.add((x, y))
    print(len(accessible))
answer = len(accessible)


print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
