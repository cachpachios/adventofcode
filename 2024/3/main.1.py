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
line = "".join(file)


answer = 0

# find all "mul" in string

splits = line.split("mul")[1:]
for begin in splits:
    if begin[0] != "(":
        continue
    end = begin.find(")")
    if end == -1:
        continue

    s = begin[1:end]
    if s.count(",") != 1:
        continue
    x, y = s.split(",")
    try:
        x = int(x)
        y = int(y)
    except:
        continue
    answer += x * y

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
