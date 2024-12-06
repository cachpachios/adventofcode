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

visited = set([start])

left_area = False


def find_obs(x, y, dx, dy):
    print(y, x, dy, dx)
    while (x, y) not in obst:
        if x < 0 or y < 0 or x >= len(file[0]) or y >= len(file):
            print("Out of bounds")
            global left_area
            left_area = True
            return (x, y)
        visited.add((x, y))
        x += dx
        y += dy
    print("Obs:", y, x, "\n")
    return (x - dx, y - dy)


dirs = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}

direction = 0
pos = find_obs(*start, *dirs[direction])
first = pos
direction = (direction + 1) % 4
pos = find_obs(*pos, *dirs[direction])

while pos != first and not left_area:
    pos = find_obs(*pos, *dirs[direction])
    direction = (direction + 1) % 4

answer = len(visited)
print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
