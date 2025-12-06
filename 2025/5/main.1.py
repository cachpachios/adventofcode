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


for x in xs:
    for r in ranges:
        if r[0] <= x <= r[1]:
            answer += 1
            break

print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
