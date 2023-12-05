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

# Put seeds into pair of tuples
seeds = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

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
print(seeds)
def find():
    final_ranges = []
    for seed in seeds:
        source = "seed"
        current_ranges = [seed]
        while source != "location":
            target = maps[source]
            target_ranges = []
            for range in current_ranges:
                no_target = True
                for tr in target:
                    match_start = max(tr.source, range[0])
                    match_end = min(tr.source+tr.length-1, range[0] + range[1] - 1)
                    if match_start <= match_end:
                        target_ranges.append((tr.target - tr.source + match_start, match_end - match_start))
                        no_target = False
                if no_target:
                    target_ranges.append(range)
            current_ranges = target_ranges
            source = target[0].target_name
            print(seed, source, current_ranges)
        final_ranges.append(current_ranges)
    return final_ranges
final_ranges = find()
answer = min(final_ranges, key=lambda x: min(x, key=lambda y: y[0]))[0][0]
print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
