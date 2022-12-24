from typing import Dict
from utils import *
import sys
import string
from tqdm import tqdm
from collections import Counter, defaultdict
from itertools import combinations, permutations, combinations_with_replacement
from dataclasses import dataclass

from functools import cache

INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"
file = read(INPUT_FILE)

@dataclass
class Valve:
    id: str
    n: List[str] # Valves
    fr: int


pipes = {}

for l in file:
    ws = l.split()
    vlvs = l.split("to valve")[-1].split(", ")
    vlvs[0] = vlvs[0].split()[-1]
    nms = nums(l)
    
    v = Valve(ws[1], [x.strip() for x in vlvs], nms[0])
    print(v)
    pipes[v.id] = v

@dataclass
class Path:
    ts: int
    curr: str
    curr_el: str
    pressure: int
    open: List[str]
    fr: int

paths = [Path(0, 'AA', 'AA', 0, [], 0)]

max_p = {i:-1 for i in range(27)}
max_fr = {i:-1 for i in range(27)}

max_i = 0

TQDM = tqdm(desc="Exploring")
TQDM_R = tqdm(desc="Rejected", position=1)
TQDM_B = tqdm(desc="Bases", position=2)

@cache
def explore(i, a,b, pressure, open, fr):
    global max_i, max_p, max_fr
    
    if i == 1:
        TQDM_B.update(1)
    
    last_maxp = max_p[i]
    
    max_p[i] = max(last_maxp, pressure)
    max_fr[i] = max(max_fr[i], fr)
    
    if i == 26:
        if pressure > last_maxp:
            tqdm.write(f"{i}: {pressure} {fr} {open}\t{max_p}")
            tqdm.write(f"{explore.cache_info()}")
        return
    pressure = pressure + fr
    
    
    if i > 20:
        if pressure < max_p[i]:
            TQDM_R.update(1)
            return
        if fr < max_fr[i]*0.95:
            TQDM_R.update(1)
            return
    elif i > 14:
        if pressure < max_p[i]*0.95:
            TQDM_R.update(1)
            return
        if fr < max_fr[i]*0.9:
            TQDM_R.update(1)
            return
    elif i > 6:
        if pressure < max_p[i]*0.90:
            TQDM_R.update(1)
            return
        
    TQDM.update(1)
    
    # Curr opens
    if a+',' not in open:
        # El moves    
        for v in pipes[a].n:
            explore(i+1, v, b, pressure, open + a+',', fr + pipes[a].fr)
    
    # EL opens
    if b+',' not in open and a != b:
        # Curr moves    
        for v in pipes[b].n:
            explore(i+1, v, a, pressure, open + b+',', fr + pipes[b].fr)
    
    # Both moves:
    for curr in pipes[a].n:
        for curr_el in pipes[b].n:
            explore(i+1, curr, curr_el, pressure, open, fr)

explore(0, 'AA', 'AA', 0, "", 0)

print(max_p)
answer = max(max_p.values())

print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
exit()
