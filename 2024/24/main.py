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
from itertools import combinations, permutations, combinations_with_replacement, product
from dataclasses import dataclass

from multiprocessing import Pool

from functools import cache, lru_cache

INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"
answer = 0

devices_, gates_ = parse_blocks(read(INPUT_FILE))

devices = {}

for d in devices_:
    t, v = d.split(": ")
    devices[t] = int(v)

xs = ""
ys = ""

for k, v in sorted(devices.items(), key=lambda x: x[0], reverse=True):
    if k[0] == "x":
        xs += str(v)
    if k[0] == "y":
        ys += str(v)
x = int(xs, 2)
y = int(ys, 2)
z = x + y
zs = f"{z:b}"

print(xs, "+", ys, "=", zs)

OPS = {
    "AND": lambda a, b: a & b,
    "OR": lambda a, b: a | b,
    "XOR": lambda a, b: a ^ b,
}
OPS_STR = {
    "AND": "&",
    "OR": "|",
    "XOR": "^",
}

# NOTE: This was done manual, one by one.
SWAPS = {
    "z10": "kmb",
    "z15": "tvp",
    "z25": "dpg",
    "mmf": "vdk",
}

for k, v in SWAPS.copy().items():
    SWAPS[v] = k

gates = deque()

for g in gates_:
    op, out = g.split(" -> ")
    a, op, b = op.split(" ")
    gates.append((a, op, b, out))

devices_out = {}
devices_red = {}
renames = {}

while gates:
    a, op, b, out = gates.popleft()

    if a[0] == "x" and b[0] == "y" or a[0] == "y" and b[0] == "x" and out[0] != "z":
        if op == "AND":
            renames[out] = f"r{a[1:]}"
        if op == "XOR":
            renames[out] = f"a{a[1:]}"
    if a not in devices or b not in devices:
        gates.append((a, op, b, out))
        continue
    out = SWAPS.get(out, out)
    devices[out] = OPS[op](devices[a], devices[b])

    devices_out[out] = (devices_out.get(a, a), op, devices_out.get(b, b))
    devices_red[out] = (a, op, b)

s = ""

printed = []


def pk(k):
    if k in printed:
        return
    a, op, b = devices_red[k]
    print(renames.get(k, k), "=", renames.get(a, a), op, renames.get(b, b))
    printed.append(k)
    if a in devices_red:
        pk(a)
    if b in devices_red:
        pk(b)


for k, v in sorted(devices_out.items(), key=lambda x: x[0], reverse=False):
    if k[0] != "z":
        continue
    ki = int(k[1:])
    zi = len(zs) - ki - 1
    val = devices[k]
    if str(val) == zs[zi]:
        a, op, b = devices_red[k]
        print("OK", renames.get(k, k), "=", renames.get(a, a), op, renames.get(b, b))
        continue

    print("\nMismatch", k, val, zs[zi])
    pk(k)
    print()

if renames:
    print("\nRENAMES:")
    for r, k in renames.items():
        print(k, "=", r)

joined_swaps = set()
for k, v in SWAPS.items():
    joined_swaps.add(k)
    joined_swaps.add(v)

answer = ",".join(sorted(joined_swaps))


print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
