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

dail = 50
answer = 0

for line in lines:
    # L11
    dir = 1 if line[0] == "R" else -1
    dail += dir * int(line[1:])
    dail = (dail + 100) % 100
    print(line, dail)
    if dail == 0:
        answer += 1

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
