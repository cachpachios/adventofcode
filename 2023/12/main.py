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

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid # https://github.com/brean/python-pathfinding/blob/main/docs/01_basic_usage.md
from pathfinding.core.graph import Graph # https://github.com/brean/python-pathfinding/blob/main/docs/03_graphs.md
from pathfinding.core.node import Node
from pathfinding.finder.a_star import AStarFinder
from functools import cache, lru_cache

INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"

file = read(INPUT_FILE)

groups = []
counts = []

for l in file:
    data, count = l.split()
    groups.append(data)
    counts.append(parse_comma([count], int)[0])

def count_groups_wihout_unclearity(s: str):
    # Count groups of # separated by .
    # Example ..##..###. -> 2, 3
    a = s.split(".")
    return [len(i.replace(".", "")) for i in a if "#" in i and "?" not in i]

def count_groups(s: str):
    # Count groups of # separated by .
    # Example ..##..###. -> 2, 3
    a = s.split(".")
    return sorted([len(i.replace(".", "")) for i in a if "#" in i])

answer = 0

def contenders(qg: str):
    idx = [i for i, ltr in enumerate(qg) if ltr == "?"]
    contenders = []
    done_strs = set()
    for comb in itertools.product(".#", repeat=len(idx)):
        new = list(qg)
        for i, c in zip(idx, comb):
            new[i] = c
        new = "".join(new)
        if new in done_strs:
            continue
        done_strs.add(new)
        contender = count_groups(new)
        if contender:
            contenders.append((contender,new))
    return contenders

for group, count in (list(zip(groups, counts))):
    for_group = 0

    qgroups = []
    qidx = []
    si = -1
    for i,c in enumerate(group):
        if c == "?":
            if si == -1:
                si = i
        elif c == ".":
            if si != -1:
                qgroups.append(group[si:i])
                qidx.append((si, i))
                si = -1
    if si != -1:
        qgroups.append(group[si:])
        qidx.append((si, len(group)))
    qidx = [(i[0] if qgroups[j][-1] != "." else i[0]+1, i[1] if qgroups[j][0] != "." else i[1]-1) for j, i in enumerate(qidx)]
    qgroups = [g.replace(".", "") for g in qgroups]
    unaffectable = count_groups_wihout_unclearity(group)
    count_full = count.copy()
    for u in unaffectable:
        count.remove(u)
    count.sort()
    print(group, unaffectable,count_full,count)

    max_count = max(count)
    qgc = [[] for _ in qgroups]
    for k, qg in enumerate(qgroups):
            for contender in contenders(qg):
                if max(contender, key=lambda x: x[0]) <= max_count:
                    qgc[k].append(contender)
    
    for comb in itertools.product(*qgc):
        contender = sorted(flatten2(comb))
        if contender == count:
            print(contender)
            for_group += 1
    print(group, for_group)
    input()
    answer += for_group
print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
