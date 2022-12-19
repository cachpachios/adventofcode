from multiprocessing import Pool
from types import NoneType
from typing import Dict
from utils import *
from enum import Enum
import sys
import string
from tqdm import tqdm
import math
import numpy as np
from collections import Counter, defaultdict
from itertools import combinations, permutations, combinations_with_replacement
from dataclasses import dataclass

from functools import cache, lru_cache

INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"
file = read(INPUT_FILE)

blocks = parse_blocks(file)

blueprints = []

ingredients = list(reversed(["ore", "clay", "obsidian", "geode"]))
ii = {k: i for i,k in enumerate(ingredients)}



@dataclass
class RobotBP:
    pi: int 
    produces: np.array
    costs: np.array
    


for block in blocks:
    blueprint = []
    for line in block[1:]:
        splt = line.split("costs")

        robot = RobotBP(None, np.zeros(len(ingredients), dtype=np.int32), np.zeros(len(ingredients), dtype=np.int32))
        for ingredient in ingredients:
            if ingredient in splt[0]:
                robot.pi = ii[ingredient]
                robot.produces[ii[ingredient]] = 1
                break
        csplt = splt[1].split()
        for i, s in enumerate(csplt):
            for ing in ingredients:
                if ing in s:
                    robot.costs[ii[ing]] = int(csplt[i-1])
            
        blueprint.append(robot)
    blueprints.append(list(reversed(blueprint)))

print(blueprints)
#pbars = [tqdm(position=i, desc=f"i={i+1}") for i in range(23)]

MAX_TIME = 32

#pbars = [tqdm(position=i+1, desc=f"i={i+1}") for i in range(MAX_TIME)]
GEODE = ii["geode"]

def maxgeode(i, incr, stuff, best_geodes, blueprints: List[RobotBP], needed, memo):
    if needed == None:
        max_needed = np.array([max(bp.costs[i] for bp in blueprints) for i in range(len(ingredients))], dtype=np.int32)
        min_needed = np.array([min(bp.costs[i] if bp.costs[i] != 0 else 9999 for bp in blueprints) for i in range(len(ingredients))], dtype=np.int32)
        needed = (max_needed, None)
        print(needed)
    
    if memo == None:
        memo = {}
    
    if i >= MAX_TIME:
        return stuff[GEODE], (incr, stuff)
    #pbars[i].update(1)
    
    if stuff[GEODE] + incr[GEODE]*(MAX_TIME-i-1) < best_geodes[i]:
        return -1, None
    
    key = (i, ','.join(str(x) for x in incr), ','.join(str(x) for x in stuff))
    if key in memo:
        return memo[key]
    
    best_geodes[i] = max(best_geodes[i], stuff[GEODE])
    
    geodes = []
    
    for bp in blueprints:
        if bp.pi != GEODE:
            if incr[bp.pi] >= needed[0][bp.pi]:
                continue
        offset = stuff - bp.costs
        wait_time = 0
        #print(offset)
        for k, v in enumerate(offset):
            if v >= 0: # Has enough of this ingredient
                continue
            elif incr[k] == 0: # This ingredient is not produced
                wait_time = -1
                break
            wait_time = max(wait_time, int(math.ceil(-v/incr[k])))
        if wait_time >= 0 and wait_time + i + 1 < MAX_TIME:
            new_incr = incr + bp.produces
            new_stuff = stuff - bp.costs + (wait_time+1)*incr
            assert (new_stuff >= 0).all()
            new_i = i + wait_time + 1
            #print(i+1, wait_time, new_i+1)
            #print(stuff,new_stuff)
            #print(incr, new_incr)
            
            geodes.append(maxgeode(new_i, new_incr, new_stuff, best_geodes, blueprints, needed, memo))
    #print(i, stuff, incr)
    geodes.append(maxgeode(i+1, incr, stuff + incr, best_geodes, blueprints, needed, memo))
    memo[key] = max(geodes, key=lambda x: x[0])
    return max(geodes, key=lambda x: x[0])


def run_maxgeode(b):
    res = maxgeode(0, np.array([0,0,0,1], dtype=np.int32), np.zeros(len(ingredients), dtype=np.int32), {i: 0 for i in range(MAX_TIME)}, b, None, None)
    print(res)
    return res


#print(maxgeode(0, np.array([0,0,0,1], dtype=np.int32), np.zeros(len(ingredients), dtype=np.int32), {i: 0 for i in range(MAX_TIME)}, blueprints[0], None, None))
blueprints = blueprints[:3]
print(len(blueprints))
with Pool(min([16, len(blueprints)])) as p:
    geo_count = p.map(run_maxgeode, blueprints)

print(geo_count)

    
answer = product([x[0] for x in geo_count])
print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
exit()
