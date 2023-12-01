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


WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six" : 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0
}

answer = 0

def strtonums(s):
    ns = []
    for i in range(len(s)):
        ssub = s[i:]
        try:
            ns.append(int(ssub[0]))
        except:
            pass

        for word, num in WORDS.items():
            if ssub.startswith(word):
                ns.append(num)
                break

    return ns

numbers = [strtonums(l) for l in file]

for n in numbers:
    print(n,f"{n[0]}{n[-1]}")
    n = "".join(str(x) for x in n)
    answer += int(f"{n[0]}{n[-1]}")


print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
