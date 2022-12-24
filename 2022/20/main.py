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
ns = deque(read(INPUT_FILE, int))
k = 811589153 #k=1
ns = [x*k for x in ns]

#print(ns)

nsx = list(enumerate(ns))
for _ in range(10):
    for i,n in enumerate(ns):
        idx = nsx.index((i,n))
        ix = (idx + n) % (len(nsx) - 1)
        nsx.insert(ix, nsx.pop(idx))
        #print([n for i, n in nsx])
ns = [n for i, n in nsx]
answer = sum(ns[(i_ + ns.index(0)) % len(ns)] for i_ in [1000,2000,3000])

print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
exit()
