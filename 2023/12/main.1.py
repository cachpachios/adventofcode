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
import itertools
from dataclasses import dataclass

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid # https://github.com/brean/python-pathfinding/blob/main/docs/01_basic_usage.md
from pathfinding.core.graph import Graph # https://github.com/brean/python-pathfinding/blob/main/docs/03_graphs.md
from pathfinding.core.node import Node
from pathfinding.finder.a_star import AStarFinder
from functools import cache, lru_cache

INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"

file = read(INPUT_FILE)

groups = []
counts = []

for l in file:
    data, count = l.split()
    groups.append(data)
    counts.append(parse_comma([count], int)[0])

def count_groups(s: str):
    # Count groups of # separated by .
    # Example ..##..###. -> 2, 3
    a = s.split(".")
    return [len(i.replace(".", "")) for i in a if "#" in i]

answer = 0

for group, count in tqdm(list(zip(groups, counts))):
    for_group = 0
    idx = [i for i, ltr in enumerate(group) if ltr == "?"]

    for comb in itertools.product(".#", repeat=len(idx)):
        new = list(group)
        for i, c in zip(idx, comb):
            new[i] = c
        new = "".join(new)
        if count_groups(new) == count:
            for_group += 1
    answer += for_group
print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
