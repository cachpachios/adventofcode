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
from itertools import combinations, permutations, combinations_with_replacement, product
from dataclasses import dataclass

from multiprocessing import Pool

from functools import cache, lru_cache

INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"

file = read(INPUT_FILE)
answer = 0

designs, piles = parse_blocks(file)
designs = designs[0].split(", ")
print(designs, piles)

@lru_cache(None)
def test(p):
    if not p:
        return 1
    
    valids = 0
    for d in designs:
        if p.startswith(d):
            valids += test(p[len(d):])
    return valids

# def test(p):
#     frontier = deque([(0,[])])
#     answers = []
#     while frontier:
#         i, dsd = frontier.pop()
#         print(i, dsd)
#         assert i <= len(p)
#         if i == len(p):
#             answers.append(dsd)
#             continue
#         for d in designs:
#             if p.startswith(d, i):
#                 frontier.append((i + len(d), dsd + [d]))
#     return answers

for p in tqdm(piles):
    answer += test(p)

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
