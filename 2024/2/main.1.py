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
lines = [list(map(int, l.split())) for l in file]

answer = 0

for l in lines:
    diff = [l[i] - l[i-1] for i in range(1,len(l))]
    signs = list(map(sign, diff))
    if all(abs(x) > 0 and abs(x) <= 3 for x in diff) and all(sign(x) == s for s in signs for x in diff):
        print(l, diff, "Safe", list(abs(x) > 0 and abs(x) <= 3 for x in diff))
        answer += 1
    else:
        print(l, diff, "Unsafe", list(abs(x) > 0 and abs(x) <= 3 for x in diff))

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
