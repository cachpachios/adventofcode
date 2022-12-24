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

@dataclass
class Bliz:
    y: int
    x: int
    fwrd: complex
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Bliz):
            return self.y == __o.y and self.x == __o.x and self.fwrd == __o.fwrd
        return False

    def __hash__(self) -> int:
        return hash((self.y, self.x, self.fwrd))

map = np.zeros((len(file), max([len(x) for x in file])), dtype=np.int32)
blizzards = []
print(map.shape)
for i,row in enumerate(file):
    for j, c in enumerate(row):
        if c == ".":
            map[i,j] = 0
        elif c == "#":
            map[i,j] = -1
        elif c == ">":
            blizzards.append(Bliz(y=i,x=j,fwrd=1))
        elif c == "<":
            blizzards.append(Bliz(y=i,x=j,fwrd=-1))
        elif c == "v":
            blizzards.append(Bliz(y=i,x=j,fwrd=1j))
        elif c == "^":
            blizzards.append(Bliz(y=i,x=j,fwrd=-1j))

blizzards = tuple(blizzards)            

BLIZZARDS = {
    1: '>',
    -1: '<',
    1j: 'v',
    -1j: '^'
}
            
ENTER = 1
EXIT = map.shape[0]-2 + (map.shape[1]-1)*1j

def simulateBlizzard(blizzards):
    new_blizzards = []
    for bliz in blizzards:
        ny = int(bliz.y + bliz.fwrd.imag)
        nx = int(bliz.x + bliz.fwrd.real)
        
        if ny==0:
            ny = map.shape[0] - 2
        if ny == map.shape[0] - 1:
            ny = 1
        if nx==0:
            nx = map.shape[1] - 2
        if nx == map.shape[1] - 1:
            nx = 1
        
        bliz.x = nx
        bliz.y = ny
        new_blizzards.append(bliz)
    return tuple(new_blizzards)

print(blizzards)
LIMIT = 240 if "-pr" in sys.argv else 20
frontier = [(0,1, 0, (map.shape[0]-1, map.shape[1]-2), 0)]
new_frontier = frontier
ends = []
while frontier:
    frontier = new_frontier
    new_frontier = []
    blizrds = np.zeros((map.shape[0]-2, map.shape[1]-2), dtype=np.int32)
    for b in blizzards:
        blizrds[b.y-1, b.x-1] += 1
    for (y,x,steps,goal,back) in frontier:
        if y == goal[0] and x == goal[1]:
            if back >= 2:
                ends.append(steps)
                print("Finished", steps, back)
                break
            else:
                new_goal = (0,1)
                if goal[0] == 0 and goal[1] == 1:
                    new_goal = (map.shape[0]-1, map.shape[1]-2)
                print("Going back", goal, new_goal)
                if steps < LIMIT*4:
                    new_frontier.append((y,x,steps+1, new_goal,back+1))
                
                if goal[0] > 0:
                    new_frontier.append((y-1,x,steps+1, new_goal,back+1))
                else:
                    new_frontier.append((y+1,x,steps+1, new_goal,back+1))
                
                continue
        elif y == map.shape[0]-1 and x == map.shape[1]-2:
            if steps < LIMIT*4:
                new_frontier.append((y,x,steps+1,goal,back))
            new_frontier.append((y-1,x,steps+1,goal,back))
        elif y == 0 and x == 1:
            if steps < LIMIT*4:
                new_frontier.append((y,x,steps+1,goal,back))
            new_frontier.append((y+1,x,steps+1,goal,back))
            
            
        if y == 0 or x == 0 or y == map.shape[0]-1 or x == map.shape[1]-1:
            continue
        
        if map[y,x] != 0:
            continue
        
        
        if blizrds[y-1,x-1] > 0:
            continue       
        
        if steps > LIMIT+20 and back == 0:
            continue
        elif steps > LIMIT*3 and back < 2:
            continue
        elif steps > LIMIT*4:
            continue
        
        if (y,x,steps+1,goal,back) not in new_frontier:
            new_frontier.append((y,x,steps+1,goal,back))
        if (y+1,x,steps+1,goal,back) not in new_frontier:        
            new_frontier.append((y+1,x,steps+1,goal,back))
        if (y,x+1,steps+1,goal,back) not in new_frontier:
            new_frontier.append((y,x+1,steps+1,goal,back))
        if (y-1,x,steps+1,goal,back) not in new_frontier:
            new_frontier.append((y-1,x,steps+1,goal,back))
        if (y,x-1,steps+1,goal,back) not in new_frontier:
            new_frontier.append((y,x-1,steps+1,goal,back))
    print(steps)
    blizzards = simulateBlizzard(blizzards)
        
    
print(ends)

answer = min(ends)

print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
exit()
