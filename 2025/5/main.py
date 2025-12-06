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

ragnes, xs = parse_blocks(read(INPUT_FILE))
xs = list(map(int, xs))

ranges = [tuple(map(int, r.split("-"))) for r in ragnes]
print(ranges)
answer = 0

merged = True

while merged:
    merged = False
    ranges.sort()
    new_ranges = []
    cur_start, cur_end = ranges[0]
    for start, end in ranges[1:]:
        if start <= cur_end + 1:
            cur_end = max(cur_end, end)
            merged = True
        else:
            new_ranges.append((cur_start, cur_end))
            cur_start, cur_end = start, end
    new_ranges.append((cur_start, cur_end))
    ranges = new_ranges
print(ranges)

answer = sum(r[1] - r[0] + 1 for r in ranges)

print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
