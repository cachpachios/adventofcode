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
from itertools import combinations, permutations, combinations_with_replacement,product
from dataclasses import dataclass

from multiprocessing import Pool

from functools import cache, lru_cache

INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"

inpt = read(INPUT_FILE)
answer = 0

stones = [int(x) for x in inpt[0].split()]

def blink():
    global stones
    new_stones = []
    for s in stones:
        if s == 0:
            new_stones.append(1)
            continue

        if len(ss := str(s)) % 2 == 0:
            new_stones.append(int(ss[:len(ss)//2]))
            new_stones.append(int(ss[len(ss)//2:]))
            continue
        
        new_stones.append(s*2024)
    stones = new_stones

for i in range(25):
    blink()
    print(stones)

answer = len(stones)

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
