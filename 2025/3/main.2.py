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
    picked = []
    for n in range(11, -1, -1):
        available_n = len(volts)
        min_needed_remaining = available_n - n
        print(picked, volts, n, min_needed_remaining, available_n)
        max_in_available = max(volts[:min_needed_remaining])
        picked.append(max_in_available)
        # Remove all before the picked digit
        index_of_picked = volts.index(max_in_available)
        volts = volts[index_of_picked + 1 :]

    answer += int("".join(map(str, picked)))
    print(f"Bank {bank} -> {int(''.join(map(str, picked)))}")

print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
