from multiprocessing import Pool
import pprint
from typing import Dict
from utils import *
from enum import Enum
import sys
import string
from tqdm import tqdm
import math
import numpy as np
from collections import Counter, defaultdict, deque
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid # https://github.com/brean/python-pathfinding/blob/main/docs/01_basic_usage.md
from pathfinding.core.graph import Graph # https://github.com/brean/python-pathfinding/blob/main/docs/03_graphs.md
from pathfinding.core.node import Node
from pathfinding.finder.a_star import AStarFinder
from itertools import combinations, permutations, combinations_with_replacement
from dataclasses import dataclass

from functools import cache, lru_cache

INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"

file = read(INPUT_FILE)
answer = 0

blocks = parse_blocks(file)

seeds = nums(blocks[0][0])

maps = {}

@dataclass
class Range:
    target: int
    source: int
    length: int
    target_name: str | None = None

for block in blocks[1:]:
    key = block[0]
    key = key.split(" ")[0].split("-to-")
    maps[key[0]] = []
    for line in block[1:]:
        ns = nums(line)
        maps[key[0]].append(Range(ns[0], ns[1], ns[2], key[1]))

def find():
    final_targets = []
    for seed in seeds:
        source = "seed"
        last_targets = [seed]
        while source != "location":
            target = maps[source]
            targets = []
            for val in last_targets:
                any_targets = False
                for tr in target:
                    if tr.source <= val <= tr.source+tr.length-1:
                        targets.append(tr.target + val - tr.source)
                        any_targets = True         
                if not any_targets:
                    targets.append(val)
            source = target[0].target_name
            last_targets = targets
        final_targets.append(last_targets)
    return final_targets
final_ranges = find()
answer = min(final_ranges, key=lambda x: min(x))[0]
print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
