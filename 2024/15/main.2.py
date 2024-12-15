from copy import deepcopy
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

rmap, rmoves = parse_blocks(inpt)
rmap = [list(x) for x in rmap]

map = {"map": []}

for l in rmap:
    ll = []
    for c in l:
        if c == "#":
            ll.append("#")
            ll.append("#")
        elif c == "O":
            ll.append("[")
            ll.append("]")
        elif c == ".":
            ll.append(".")
            ll.append(".")
        elif c == "@":
            ll.append("@")
            ll.append(".")
        else:
            raise Exception(f"Invalid character {c}")
    map["map"].append(ll)

def print_map():
    for y in range(len(map["map"])):
        print("".join(map["map"][y]))

print_map()

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
for y in range(len(map["map"])):
    for x in range(len(map["map"][0])):
        if map["map"][y][x] == "@":
            robot_pos = (x, y)
            break
assert robot_pos is not None

def push(x,y,dx,dy, self):
    c = map["map"][y][x]
    nx, ny = x+dx, y+dy
    nc = map["map"][ny][nx]

    assert c == self, f"Expected {self} at {x},{y} but got {map["map"][y][x]}"
    assert nc != "@", f"Expected not @ at {nx},{ny} but got {map["map"][ny][nx]}"
    if nc == "#":
        return False
    if nc == ".":
        map["map"][ny][nx] = self
        map["map"][y][x] = "."
        return True

    if nc in "[]":
        ox, oy = nx + (1 if nc == "[" else -1), ny
        oc = map["map"][oy][ox]
        assert oc in "[]", f"Expected [] at {ox},{oy} but got {map["map"][oy][ox]}"
        mcpy = deepcopy(map["map"])
        pushed_other = push(ox, oy, dx, dy, oc)
        if not pushed_other:
            return False

        if push(nx, ny, dx, dy, nc):
            map["map"][ny][nx] = self
            map["map"][y][x] = "."
            return True
        else:
            map["map"] = mcpy
        return False
    raise Exception(f"Invalid move {map["map"][ny][nx]} at {nx},{ny}")

for i,move in enumerate(moves):
    # print_map()
    # print("Move", move,"\n")
    # input()
    rx, ry = robot_pos
    dx, dy = move
    if push(rx, ry, dx, dy, "@"):
        robot_pos = (rx+dx, ry+dy)

print_map()

for y, r in enumerate(map["map"]):
    for x, c in enumerate(r):
        if c == "[":
            answer += y*100 + x


print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
