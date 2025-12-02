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

dail = 50
answer = 0

for line in lines:
    dir = 1 if line[0] == "R" else -1
    new_dail = dail + dir * int(line[1:])
    if dir == 1:
        answer += new_dail // 100 - dail // 100
    else:
        answer += (dail - 1) // 100 - (new_dail - 1) // 100
    dail = new_dail % 100
    print(line, ", Dail:", dail, "Answer:", answer)

print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
