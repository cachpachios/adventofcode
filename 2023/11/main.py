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

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid # https://github.com/brean/python-pathfinding/blob/main/docs/01_basic_usage.md
from pathfinding.core.graph import Graph # https://github.com/brean/python-pathfinding/blob/main/docs/03_graphs.md
from pathfinding.core.node import Node
from pathfinding.finder.a_star import AStarFinder
from functools import cache, lru_cache

INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"
answer = 0

file = read(INPUT_FILE)

emptyCols = []


for x in range(len(file[0])):
    empty =True
    for line in file:
        if line[x] == "#":
            empty = False
            break
    if empty:
        emptyCols.append(x)

glxies = []
y = 0
for line in (file):
    x = 0
    hasGalaxy = False
    for j,c in enumerate(line):
        if j in emptyCols:
            x += 1000000
            continue
        elif c == "#":
            hasGalaxy = True
            glxies.append((x, y))
        x += 1
    if hasGalaxy:
        y += 1
    else:
        y += 1000000
dist = []


for glx, glx2 in combinations(glxies, 2):
    dx = abs(glx[0] - glx2[0])
    dy = abs(glx[1] - glx2[1])
    dist.append(dx + dy)
answer = sum(dist)

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
