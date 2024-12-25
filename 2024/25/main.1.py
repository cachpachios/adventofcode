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
answer = 0

rkeys = parse_blocks(read(INPUT_FILE))

keys = []
locks = []

for rk in rkeys:
    ke = []
    for x in range(len(rk[0])):
        col = [r[x] == "#" for r in rk]
        ke.append(sum(col) - 1)
        assert ke[-1] >= 0
    if rk[0][0] == "#":
        locks.append(ke)
    else:
        keys.append(ke)


def check(k, l):
    for c in range(len(k)):
        if l[c] > 5 - k[c]:
            print("Failed", k, l, c)
            return False
    print("Passed", k, l)
    return True


print("Keys", keys)
print("Locks", locks)

for l in locks:
    for i, k in enumerate(keys):
        if check(k, l):
            answer += 1

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
