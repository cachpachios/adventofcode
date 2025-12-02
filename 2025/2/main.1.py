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

ranges = read(INPUT_FILE)[0].split(",")

answer = 0

for r in tqdm(ranges):
    a, b = map(int, r.split("-"))
    for x in range(a, b + 1):
        s = str(x)
        if len(s) % 2 != 0:
            continue
        mid = len(s) // 2
        if s[:mid] == s[mid:]:
            answer += x

print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
