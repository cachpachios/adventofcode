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

map = np.zeros((len(file), max([len(x) for x in file])), dtype=np.int8) - 1
print(map.shape)
for i,row in enumerate(file):
    for j, c in enumerate(row):
        if c == ".":
            map[i,j] = 0
        elif c == "#":
            map[i,j] = 1

inner = map
offset = 200
map = np.zeros((map.shape[0]+offset, map.shape[1]+offset), dtype=np.int8)
hoffset = offset//2
map[hoffset:hoffset+inner.shape[0], hoffset:hoffset+inner.shape[1]] = inner


# for i in range(map.shape[0]):
#     for j in range(map.shape[1]):
#         c = map[i,j]
#         if c == 0:
#             print(".", end="")
#         if c == 1:
#             print("#", end="")
#     print()

deltas = [(0,1), (0,-1), (1,0), (-1,0)]

cons = [(0,1,2), (3,4,5), (6,2,5), (7,1,4)]
dirs = [(-1,0), (1,0), (0,-1), (0,1)]

for i in tqdm(range(20000)):
    moves = {}
    attempted_moves = 0
    for y in range(map.shape[0]):
        for x in range(map.shape[1]):
            if map[y,x] != 1:
                continue
            adj_N = map[y-1,x] #0
            adj_NE = map[y-1,x+1] # 1
            adj_NW = map[y-1,x-1] # 2
            adj_S = map[y+1,x] # 3
            adj_SE = map[y+1,x+1] # 4
            adj_SW = map[y+1,x-1] # 5
            adj_W = map[y,x-1] # 6
            adj_E = map[y,x+1] # 7
            
            ajds = [adj_N, adj_NE, adj_NW, adj_S, adj_SE, adj_SW, adj_W, adj_E]
            
            if adj_N + adj_NE + adj_NW + adj_S + adj_SE + adj_SW + adj_W + adj_E == 0:
                moves[f"{y},{x}"] = moves.get(f"{y},{x}", []) + [(y,x)]
                continue
            for j in range(len(cons)):
                con = cons[(j+i)%len(cons)]
                dir = dirs[(j+i)%len(dirs)]
                if sum([ajds[i] for i in con]) == 0:
                    moves[f"{y+dir[0]},{x+dir[1]}"] = moves.get(f"{y+dir[0]},{x+dir[1]}", []) + [(y,x)]
                    attempted_moves += 1
                    break
            else:
                moves[f"{y},{x}"] = moves.get(f"{y},{x}", []) + [(y,x)]
    map[:,:] = 0
    
    for new,olds in moves.items():
        if len(olds) > 1:
            for o in olds:
                attempted_moves -= 1
                map[o[0], o[1]] = 1
        else:
            nn  = new.split(",")
            map[int(nn[0]), int(nn[1])] = 1
    if attempted_moves == 0:
        print("NO ATTEMPTED MOVES ", i)
        break
# min_y,max_y,min_x,max_x = 1000000,0,1000000,0

# for y in range(map.shape[0]):
#     for x in range(map.shape[1]):
#         if map[y,x] == 1:
#             min_y = min(min_y, y)
#             max_y = max(max_y, y)
#             min_x = min(min_x, x)
#             max_x = max(max_x, x)

# print(min_y, max_y, min_x, max_x)

# map = map[min_y:max_y+1, min_x:max_x+1]

# for i in range(map.shape[0]):
#     for j in range(map.shape[1]):
#         c = map[i,j]
#         if c == 0:
#             print(".", end="")
#         if c == 1:
#             print("#", end="")
#     print()

# answer = map.shape[0]*map.shape[1] - map.sum()

answer = i+1

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
exit()
