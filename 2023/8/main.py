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

currs = [k for k in graph.keys() if k.endswith("A")]
answers = []
for curr in tqdm(currs):
    answer = 0
    while not curr.endswith("Z"):
        move = moves[answer % len(moves)]
        l, r = graph[curr]
        if move == "L":
            curr = l
        else:
            curr = r
        answer += 1
    answers.append(answer)

print(answers)

answer = math.lcm(*answers)
print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
