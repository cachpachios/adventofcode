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

file = read(INPUT_FILE)
answer = 0

eqs = []

for f in file:
    ss = f.split(": ")
    ss2 = ss[1].split(" ")
    eqs.append((int(ss[0]), list(map(int, ss2))))


def opadd(a, b):
    return a+b

def opmul(a, b):
    return a*b

def eval(ops, vals):
    r = vals[0]
    for o, v in zip(ops, vals[1:]):
        r = o(r, v)
    return r

for (ans, vals) in eqs:
    for ops in product([opadd, opmul], repeat=len(vals)-1):
        r = eval(ops, vals)
        print(vals,r)
        if r == ans:
            print(ans, "MATCH")
            answer += ans
            break
            


print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
