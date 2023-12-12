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
import itertools
from dataclasses import dataclass

from functools import cache, lru_cache

INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"

file = read(INPUT_FILE)

groups = []
counts = []

for l in file:
    data, count = l.split()
    groups.append(data)
    counts.append(parse_comma([count], int)[0])

answer = 0

GLOBAL_CACHE = {}

def count_combs(curr, target):
    ckey = f'{",".join(map(str, target))}@{",".join(curr)}'
    if ckey in GLOBAL_CACHE:
        return GLOBAL_CACHE[ckey]
    
    if not target:
        return 0 if any("#" in c for c in curr) else 1
    if not curr:
        return 0
    ret = 0
    group = target[0]
    c = curr[0]
    len_cluster = len(c)
    if group > len_cluster and "#" in c:
        return 0
    for i in range(len_cluster - group + 1):
        first = c[:i]
        if "#" in first:
            continue
        right = c[i + group :]
        if right and right[0] == "#":
            continue
        ret += count_combs(([right[1:]] if len(right) > 1 else []) + curr[1:], target[1:])

    if "#" not in c:
        ret += count_combs(curr[1:], target)
    
    GLOBAL_CACHE[ckey] = ret
    
    return ret


for group,count in zip(groups,counts):
    count *= 5
    group = "?".join(5 * [group])
    group = [g for g in group.split(".") if len(g) > 0]
    answer += count_combs(group, count)

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
