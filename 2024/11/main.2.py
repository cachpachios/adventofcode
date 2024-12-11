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

@lru_cache(maxsize=None)
def simul(s, i=0):
    if i == 75:
        return 1
    
    if s == 0:
        return simul(1, i+1)

    
    if len(ss := str(s)) % 2 == 0:
        return simul(int(ss[:len(ss)//2]),i+1) + simul(int(ss[len(ss)//2:]),i+1)

    return simul(2024*s,i+1)

for s in stones:
    answer += simul(s)


print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
