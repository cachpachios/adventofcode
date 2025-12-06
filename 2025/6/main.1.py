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

ops = lines[-1].split()
numbers = np.array([list(map(int, line.split())) for line in lines[:-1]])

op_map = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
}


answer = 0

for j, row in enumerate(numbers.transpose()):
    res = row[0]
    for i in range(1, len(row)):
        print("Applying", ops[j], "to", res, "and", row[i])
        res = op_map[ops[j]](res, row[i])
    print(res)
    answer += res


print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
