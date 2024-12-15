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

inpt = read(INPUT_FILE)
answer = 0

map, rmoves = parse_blocks(inpt)
map = [list(x) for x in map]
moves = []

for l in rmoves:
    for m in l:
        if m == ">":
            moves.append((1, 0))
        elif m == "<":
            moves.append((-1, 0))
        elif m == "^":
            moves.append((0, -1))
        elif m == "v":
            moves.append((0, 1))
        else:
            raise Exception(f"Invalid move \"{m}\"")

robot_pos = None
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == "@":
            robot_pos = (x, y)
            break

def push(x,y,dx,dy, self):
    nx, ny = x+dx, y+dy
    assert map[y][x] == self, f"Expected {self} at {x},{y} but got {map[y][x]}"
    assert map[ny][nx] != "@", f"Expected not @ at {nx},{ny} but got {map[ny][nx]}"
    if map[ny][nx] == "#":
        return False
    if map[ny][nx] == ".":
        map[ny][nx] = self
        map[y][x] = "."
        return True

    if map[ny][nx] == "O":
        if push(nx, ny, dx, dy, "O"):
            map[ny][nx] = self
            map[y][x] = "."
            return True
        return False
    raise Exception(f"Invalid move {map[ny][nx]} at {nx},{ny}")

def print_map():
    for y in range(len(map)):
        print("".join(map[y]))

for i,move in enumerate(moves):
    # print_map()
    # print("Move", move,"\n")
    # input()
    rx, ry = robot_pos
    dx, dy = move
    if push(rx, ry, dx, dy, "@"):
        robot_pos = (rx+dx, ry+dy)

for y, r in enumerate(map):
    for x, c in enumerate(r):
        if c == "O":
            answer += y*100 + x


print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
