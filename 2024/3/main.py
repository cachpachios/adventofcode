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

splits = line.split("mul")
enabled = True


def swap_do_donts(s: str) -> bool:
    global enabled
    first_do = s.find("do()")
    first_dont = s.find("don't()")
    print(s, first_do, first_dont)
    if first_do == -1 and first_dont == -1:
        return
    if first_do != -1 and first_dont != -1:
        if first_do < first_dont:
            enabled = True
            print("ENABLED")
            swap_do_donts(s[first_do + 3 :])
            return
        else:
            print("DISABLED")
            enabled = False
            swap_do_donts(s[first_dont + 6 :])
            return
    if first_do != -1 and first_dont == -1:
        enabled = True
        print("ENABLED")
        swap_do_donts(s[first_do + 3 :])
        return
    if first_do == -1 and first_dont != -1:
        enabled = False
        print("DISABLED")
        swap_do_donts(s[first_dont + 6 :])
        return
    raise Exception("Should not be here")


swap_do_donts(splits[0])

for begin in splits[1:]:
    if begin[0] != "(":
        swap_do_donts(begin)
        continue
    end = begin.find(")")
    if end == -1:
        swap_do_donts(begin)
        continue

    s = begin[1:end]
    if s.count(",") != 1:
        swap_do_donts(begin)
        continue
    x, y = s.split(",")
    try:
        x = int(x)
        y = int(y)
    except:
        swap_do_donts(begin)
        continue
    print(x, y, enabled)
    if enabled:
        answer += x * y
    swap_do_donts(begin)

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
