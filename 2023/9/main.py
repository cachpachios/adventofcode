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

filsnum = numsl(file)
filsnum = [l[::-1] for l in filsnum]

window_history = []

answer = 0
for line in filsnum:
    windows = [line]
    while any([w != 0 for w in windows[-1]]):
        windows.append(window_diff(windows[-1]))
    assert not any([w < 0 for w in windows[-1]]), windows[-1]
    window_history.append(windows)
for line, history in zip(filsnum, window_history):
    val = 0
    for hist in history[::-1]:
        val += hist[-1]
    print(line, val)
    answer += val


print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
