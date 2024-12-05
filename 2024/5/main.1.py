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
answer = 0

mid = file.index("")
orders = [x.split("|") for x in file[:mid]]
all_updates = [x.split(",") for x in file[mid+1:]]

def validate(update: list[int]):
    for i,x in enumerate(update):
        for order in orders:
            left, right = order
            try:
                li = update.index(left)
                ri = update.index(right)
            except:
                continue

            if ri < li:
                print("Invalid", update, order)
                return False
    return True
    

for update in all_updates:
    if validate(update):
        print("Valid", update)
        answer += int(update[len(update)//2])


print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
