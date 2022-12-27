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

file = read(INPUT_FILE, strip=False)

rawmap, instr = parse_blocks(file)
instr_ = instr[0]
instr = ""
for l in instr_:
    if l.isnumeric():
        instr += l
    else:
        instr += " " + l + " "
map = np.zeros((len(rawmap), max([len(x) for x in rawmap])), dtype=np.int8) - 1
map_x_bounds = []
print(map.shape)
for i,row in enumerate(rawmap):
    first_el = -1
    last_el = -1
    for j, c in enumerate(row):
        if c == ".":
            if first_el == -1:
                first_el = 0
            map[i,j] = 0
            last_el = 0
        elif c == "#":
            if first_el == -1:
                first_el = 1
            map[i,j] = 1
            last_el = 1
        else:
            map[i,j] = -1
    map_x_bounds.append((first_el, last_el))
map_y_bounds = [map[:,i] != -1 for i in range(map.shape[1])]
map_y_bounds = [(list(x).index(True), len(x) - list(reversed(x)).index(True) - 1) for x in map_y_bounds]


sides = {} # Side index is from the example

hyper_map = None
if "-pr" in sys.argv:
    #    [a][b]
    #    [c]
    # [d][e]
    # [f]
    hyper_map = [[-1, 0,5], 
                 [-1, 3, -1], 
                 [2,4, -1], 
                 [1, -1,-1]]
else:
    #       [a]
    # [b][c][d]
    #       [e][f]
    hyper_map = [[-1,-1, 0, -1], 
                 [1,2,3, -1], 
                 [-1,-1, 4,5]]

direction = 1 + 0j

def right(frwd): # Turn right
    return frwd * 1j
def left(frwd): # Turn left
    return frwd * -1j
def back(frwd): # Turn around
    return -frwd
def forward(frwd):
    return frwd

edges = {
    (2, 0, 1): (1, left),
    (1, 1, 0): (2, right),

    (1, 0, 1): (4, back),
    (4, 0, 1): (1, back),

    (4, 1, 0): (5, right),
    (5, 0, 1): (4, left),

    (3, -1, 0): (2, right),
    (2, 0, -1): (3, left),

    (0, 0, -1): (3, back),
    (3, 0, -1): (0, back),

    (5, 1, 0): (1, forward),
    (1, -1, 0): (5, forward),

    (5, 0, -1): (0, left),
    (0, -1, 0): (5, right)
  }

side_length = 50 if "-pr" in sys.argv else 4

for y in range(len(hyper_map)):
    for x in range(len(hyper_map[y])):
        val = hyper_map[y][x]
        if val == -1:
            continue
        sides[val] = map[y*side_length:(y+1)*side_length, x*side_length:(x+1)*side_length]
    
    
print(sides)

forward = 1

side = 0
pos = (0, 0)
for ins in instr.split():
    if ins.isnumeric():
        print(f"Moving forward {ins} steps.")
        for s in range(int(ins)):
            ny, nx = (pos[0] + forward.imag, pos[1] + forward.real)
            ny = int(ny)
            nx = int(nx)
            
            if ny >= side_length:
                
    elif ins == "R":
        forward *= 1j
        print("Rotating right", forward)
    elif ins == "L":
        print("Rotating left", forward)
        forward *= -1j
    else:
        raise Exception("??")

print(pos, forward)

facing_score = 2 * int(forward.real == -1) + int(forward.imag == 1) + 3*int(forward.imag == -1)
print(facing_score)
answer = 1000*(pos[0]+1) + (pos[1]+1)*4 + facing_score

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
exit()
