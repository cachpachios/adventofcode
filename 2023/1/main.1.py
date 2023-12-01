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

# lines = parse(file, int)
# lines = parse()

answer = 0

numbers = numsl(file)

for n in numbers:
    n = "".join(str(x) for x in n)
    print(f"{n[0]}{n[-1]}")
    answer += int(f"{n[0]}{n[-1]}")




print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
