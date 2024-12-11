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

@dataclass
class File:
    id: int
    size: int

@dataclass
class FreeSpace:
    size: int


inpt = read(INPUT_FILE)
answer = 0

disk = []
fi = 0
tggl = True
for c in inpt[0]:
    if tggl:
        disk.append(File(fi, int(c)))
        fi += 1
    else:
        disk.append(FreeSpace(int(c))) 
    tggl = not tggl


# Defrag, move left to most right freespace
print("===============")
for d in disk:
    print(d)

def prd(disk):
    for d in disk:
        if isinstance(d, File):
            print(str(d.id) * d.size, end="")
        else:
            print("." * d.size, end="")
    print()

def defrag_once():
    # for i in range(len(disk)-1, 0, -1):
    i = len(disk)-1
    while i >= 0:
        if isinstance(disk[i], File):
            print(disk[i].id, ": ", end="")
            for j in range(i):
                if isinstance(disk[j], FreeSpace):
                    file = disk[i]
                    free = disk[j]
                    if file.size > free.size:
                        continue
                    disk[j] = File(file.id, file.size)
                    if isinstance(disk[i-1], FreeSpace):
                        disk[i-1].size += file.size
                        disk.pop(i)
                    elif isinstance(disk[i+1], FreeSpace):
                        disk[i+1].size += file.size
                        disk.pop(i)
                    else:
                        disk[i] = FreeSpace(file.size)
                    if free.size > file.size:
                        if isinstance(disk[j+1], FreeSpace):
                            disk[j+1].size += free.size - file.size
                        else:
                            disk.insert(j+1, FreeSpace(free.size - file.size))
                    break
            # prd(disk)
        
        i -= 1

defrag_once()

i = 0
for f in disk:
    if isinstance(f, File):
        for j in range(f.size):
            answer += i*f.id
            print(f"{i}*{f.id}")
            i += 1
    else:
        i += f.size

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
