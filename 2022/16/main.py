from typing import Dict
from utils import *
import sys
import string
from tqdm import tqdm
from collections import Counter, defaultdict
from itertools import combinations, permutations, combinations_with_replacement
from dataclasses import dataclass

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
    path: List[str]
    pressure: int
    open: List[str]

    def curr(self):
        return self.path[-1]

paths = [Path(0, ['AA'], 0, [])]

max_p = 0
max_fr = 0

for i in tqdm(range(26), miniters=1):
    new_paths = []
    max_fr = max([sum([pipes[k].fr for k in path.open]) for path in paths])
    print(len(paths), max_p, max_fr, max_p + max_fr*(30-i))
    for i, path in enumerate(paths):
        path.ts += 1
                
        for k in path.open: # Add pressure to path
            path.pressure += pipes[k].fr
        max_p = path.pressure if path.pressure > max_p else max_p
        
        
        if path.ts > 9:
            if path.pressure < max_p*0.8:
                continue
            if path.ts > 20 and sum([pipes[k].fr for k in path.open]) < max_fr*0.8:
                continue
            # Filter stuff...
        
        if path.curr() not in path.open:
            stays = Path(path.ts, path.path, path.pressure, path.open.copy() + [path.curr()])
            new_paths.append(stays)
        else:
            new_paths.append(path)
        if len(path.open) < len(pipes):
            moved = [
                    Path(path.ts, path.path.copy() + [v], path.pressure, path.open)
                    for v in pipes[path.curr()].n
                ]
            new_paths.extend(moved)
        
    paths = new_paths
    
best_path = max(paths, key=lambda x: x.pressure)
print(best_path)

answer = best_path.pressure
print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
exit()
