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

times = nums(file[0])
distances = nums(file[1])
answers = []

for i, (rt, rd) in enumerate(zip(times, distances)):
    tmp = 0
    for hold in range(1, rt):
        max_distance = (rt - hold) * hold
        print(i, hold, max_distance, max_distance >= rd)
        if max_distance <= rd:
            continue
        tmp += 1
    answers.append(tmp)

print(answers)
answer = product(answers)

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
