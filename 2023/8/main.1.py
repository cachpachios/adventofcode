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

moves, lines = parse_blocks(file)
moves = moves[0]

graph = {}

for line in lines:
    l, r = line[line.index("(")+1:line.index(")")].split(",")
    l = l.strip()
    r = r.strip()
    src = line[:3]
    graph[src] = (l, r)

curr = "AAA"
answer = 0
while curr != "ZZZ":
    move = moves[answer % len(moves)]
    l, r = graph[curr]
    print(curr, move, l, r)
    if move == "L":
        curr = l
    else:
        curr = r
    answer += 1

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
