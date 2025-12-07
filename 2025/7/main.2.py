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

map =  [list(x) for x in read(INPUT_FILE)]

start = (-1, -1)

for y, row in enumerate(map):
    for x, c in enumerate(row):
        if c == "S":
            start = (x, y)
            break

@lru_cache(None)
def simulate(x, y):
    ny = y
    while map[ny][x] != "^":
        ny = ny + 1
        if ny >= len(map):
            return 1
    return simulate(x + 1, ny) + simulate(x - 1, ny)

answer = simulate(start[0], start[1])

print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
