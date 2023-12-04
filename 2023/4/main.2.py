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

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid # https://github.com/brean/python-pathfinding/blob/main/docs/01_basic_usage.md
from pathfinding.core.graph import Graph # https://github.com/brean/python-pathfinding/blob/main/docs/03_graphs.md
from pathfinding.core.node import Node
from pathfinding.finder.a_star import AStarFinder
from functools import cache, lru_cache

INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"

file = read(INPUT_FILE)
answer = 0

card_possestions = {i:1 for i in range(len(file))}

for i,line in enumerate(file):
    card = line.split(":")[1].split("|")

    winning = nums(card[0])
    mine = nums(card[1])

    curr = 0
    for n in winning:
        if n in mine:
            curr += 1

    for j in range(curr):
        card_possestions[i+j+1] += card_possestions[i]

answer = sum(card_possestions.values())
print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
