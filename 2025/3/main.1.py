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

lines = read(INPUT_FILE)

answer = 0

for bank in lines:
    volts = list(map(int, bank))
    combs = []
    for i, volt in enumerate(bank):
        max_after = max(map(int, bank[i + 1 :]), default=None)
        if max_after is None:
            continue
        combi = int(f"{volt}{max_after}")
        combs.append(combi)
    answer += max(combs)
    print(f"Bank {bank} -> {max(combs)}")

print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
