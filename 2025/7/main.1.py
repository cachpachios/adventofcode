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

beams = []

for y, row in enumerate(map):
    for x, c in enumerate(row):
        if c == "S":
            beams.append((x, y))

answer = 0
activated_splitters = set()

while beams:
    x, y = beams.pop()
    map[y][x] = "|"

    # print map
    #for row in map:
    #    print("".join(row))
    #input()

    ny = y + 1
    if ny >= len(map):
        continue

    val = map[ny][x]
    if val in ["."]:
        beams.append((x, ny))
    elif val == "^":
        activated_splitters.add((x, ny))
        for nx in [x - 1, x + 1]:
            if 0 <= nx < len(map[0]):
                beams.append((nx, ny))
            else:
                print("Out of bounds", nx, ny)
    else:
        continue
answer = len(activated_splitters)
print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
